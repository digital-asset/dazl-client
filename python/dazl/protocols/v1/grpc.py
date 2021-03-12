# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Support for the gRPC-based Ledger API.
"""
from asyncio import gather
from datetime import datetime
from threading import Event
from typing import TYPE_CHECKING, AbstractSet, Iterable, Optional, Sequence
import warnings

from grpc import Channel, RpcError, insecure_channel, secure_channel, ssl_channel_credentials

from ... import LOG
from ...damlast.daml_lf_1 import PackageRef
from ...prim import Party, datetime_to_timestamp, to_party
from ...scheduler import Invoker, RunLevel
from ...util.io import read_file_bytes
from ...util.typing import safe_cast
from .._base import LedgerClient, LedgerConnectionOptions, _LedgerConnection
from ..errors import ConnectionTimeoutError, UserTerminateRequest
from ..events import BaseEvent, ContractFilter, TransactionFilter
from .pb_parse_event import (
    BaseEventDeserializationContext,
    serialize_acs_request,
    serialize_transactions_request,
    to_acs_events,
    to_transaction_events,
)

if TYPE_CHECKING:
    from ...client._conn_settings import HTTPConnectionSettings
    from ...client.commands import CommandPayload
    from ...client.ledger import LedgerMetadata


class GRPCv1LedgerClient(LedgerClient):
    def __init__(self, connection: "GRPCv1Connection", ledger: "LedgerMetadata", party: "Party"):
        from ...client.ledger import LedgerMetadata

        self.connection = safe_cast(GRPCv1Connection, connection)
        self.ledger = safe_cast(LedgerMetadata, ledger)
        self.party = to_party(party)

    def commands(self, commands: "CommandPayload") -> None:
        serializer = self.ledger.serializer
        request = serializer.serialize_command_request(commands)
        return self.connection.invoker.run_in_executor(
            lambda: self.connection.command_service.SubmitAndWait(request)
        )

    async def active_contracts(self, contract_filter: "ContractFilter") -> "Sequence[BaseEvent]":
        with LOG.info_timed("ACS request serialization"):
            request = serialize_acs_request(contract_filter, self.ledger.ledger_id, self.party)
            context = BaseEventDeserializationContext(
                None,
                self.connection.options.lookup,
                self.party,
                self.ledger.ledger_id,
            )

        with LOG.info_timed("ACS request initial stream"):
            acs_stream = await self.connection.invoker.run_in_executor(
                lambda: self.connection.active_contract_set_service.GetActiveContracts(request)
            )

        with LOG.info_timed("ACS request consume full stream"):
            # Consume a stream of events from the Active Contract Set service and store these results fully
            # in memory; return the full set of events as well as a set of package IDs that need to be
            # available in order to fully understand the contents of the Active Contract Set service.
            acs_stream = list(acs_stream)

        with LOG.info_timed("ACS find all required packages"):
            pkg_refs = {
                create_evt.template_id.package_id
                for acs_response_pb in acs_stream
                for create_evt in acs_response_pb.active_contracts
            }

        if pkg_refs:
            with LOG.info_timed(f"ACS load {len(pkg_refs)} new package(s)"):
                # Preload packages that are DIRECTLY referenced by packages in the message
                await gather(*(self.ledger.package_loader.load(pkg_ref) for pkg_ref in pkg_refs))

        with LOG.info_timed("ACS transform the message"):
            # Now load all the events. Note that do_with_retry is still required because the
            # packages that contained templates might have references to other packages that are
            # also required to understand the individual fields in a template.
            return await self.ledger.package_loader.do_with_retry(
                lambda: to_acs_events(context, acs_stream)
            )

    async def events(self, transaction_filter: "TransactionFilter") -> "Sequence[BaseEvent]":
        request = serialize_transactions_request(
            transaction_filter, self.ledger.ledger_id, self.party
        )
        context = BaseEventDeserializationContext(
            None,
            self.connection.options.lookup,
            self.party,
            self.ledger.ledger_id,
        )

        tx_future = self.connection.invoker.run_in_executor(
            lambda: self.connection.transaction_service.GetTransactions(request)
        )

        if transaction_filter.templates is None:
            # Filtering by package must disable the ability to handle exercise nodes; we may want to
            # consider dropping client-side support for exercise events anyway because they are not
            # widely used
            tt_stream = await self.connection.invoker.run_in_executor(
                lambda: self.connection.transaction_service.GetTransactionTrees(request)
            )
        else:
            tt_stream = None

        tx_stream = await tx_future

        return await self.ledger.package_loader.do_with_retry(
            lambda: to_transaction_events(
                context, tx_stream, tt_stream, transaction_filter.destination_offset
            )
        )

    async def events_end(self) -> str:
        from . import model as G

        request = G.GetLedgerEndRequest(ledger_id=self.ledger.ledger_id)
        return await self.connection.invoker.run_in_executor(
            lambda: self.connection.transaction_service.GetLedgerEnd(request).offset.absolute
        )


def grpc_upload_package(connection: "GRPCv1Connection", dar_contents: bytes) -> None:
    from . import model as G

    request = G.UploadDarFileRequest(dar_file=dar_contents)
    connection.package_management_service.UploadDarFile(request)


GRPC_KNOWN_RETRYABLE_ERRORS = (
    "DNS resolution failed",
    "failed to connect to all addresses",
    "no healthy upstream",
)


def grpc_detect_ledger_id(connection: "GRPCv1Connection") -> str:
    """
    Return the ledger ID from the remote server when it becomes available. This method blocks until
    a ledger ID has been successfully retrieved, or the timeout is reached (in which case an
    exception is thrown).
    """
    from time import sleep

    from . import model as G

    LOG.debug("Starting a monitor thread for connection: %s", connection)

    start_time = datetime.utcnow()
    connect_timeout = connection.options.connect_timeout

    while connect_timeout is None or (datetime.utcnow() - start_time) < connect_timeout:
        if connection.invoker.level >= RunLevel.TERMINATE_GRACEFULLY:
            raise UserTerminateRequest()
        if connection.closed:
            raise Exception("connection closed")

        try:
            response = connection.ledger_identity_service.GetLedgerIdentity(
                G.GetLedgerIdentityRequest()
            )
        except RpcError as ex:
            details_str = ex.details()

            # suppress some warning strings because they're not particularly useful and just clutter
            # up the logs
            if details_str not in GRPC_KNOWN_RETRYABLE_ERRORS:
                LOG.exception(
                    "An unexpected error occurred when trying to fetch the "
                    "ledger identity; this will be retried."
                )
            sleep(1)
            continue

        return response.ledger_id

    raise ConnectionTimeoutError(
        f"connection timeout exceeded: {connect_timeout.total_seconds()} seconds"
    )


def grpc_main_thread(connection: "GRPCv1Connection", ledger_id: str) -> "Iterable[LedgerMetadata]":
    from dazl.ledger.pkgloader_aio_compat import PackageLoader

    from ...client.ledger import LedgerMetadata
    from .pb_ser_command import ProtobufSerializer

    LOG.info("grpc_main_thread...")

    package_provider = GRPCPackageProvider(connection, ledger_id)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        yield LedgerMetadata(
            ledger_id=ledger_id,
            package_loader=PackageLoader(
                package_lookup=connection.options.lookup,
                conn=package_provider,
                timeout=connection.options.connect_timeout,
            ),
            serializer=ProtobufSerializer(connection.options.lookup),
            protocol_version="v1",
        )

    while not connection._closed.wait(1):
        pass

    LOG.debug("The gRPC monitor thread is now shutting down.")
    yield None


class GRPCPackageProvider:
    def __init__(self, connection: "GRPCv1Connection", ledger_id: str):
        self.connection = connection
        self.ledger_id = ledger_id

    def package_ids(self) -> "AbstractSet[PackageRef]":
        from . import model as G

        request = G.ListPackagesRequest(ledger_id=self.ledger_id)
        response = self.connection.package_service.ListPackages(request)
        return frozenset(response.package_ids)

    def package_bytes(self, package_id: "PackageRef") -> bytes:
        from . import model as G

        request = G.GetPackageRequest(ledger_id=self.ledger_id, package_id=package_id)
        package_info = self.connection.package_service.GetPackage(request)
        return package_info.archive_payload

    def get_package_ids(self) -> "AbstractSet[PackageRef]":
        return self.package_ids()

    def fetch_package(self, package_id: "PackageRef") -> bytes:
        return self.package_bytes(package_id)


def grpc_create_channel(settings: "HTTPConnectionSettings") -> Channel:
    target = f"{settings.host}:{settings.port}"
    options = [("grpc.max_send_message_length", -1), ("grpc.max_receive_message_length", -1)]

    if not settings.enable_http_proxy:
        options.append(("grpc.enable_http_proxy", 0))

    if settings.oauth:
        from google.auth.transport.grpc import secure_authorized_channel
        from google.auth.transport.requests import Request as RefreshRequester
        from google.oauth2.credentials import Credentials as OAuthCredentials

        LOG.debug("Using a secure gRPC connection over OAuth:")

        credentials = OAuthCredentials(
            token=settings.oauth.token,
            refresh_token=settings.oauth.refresh_token,
            id_token=settings.oauth.id_token,
            token_uri=settings.oauth.token_uri,
            client_id=settings.oauth.client_id,
            client_secret=settings.oauth.client_secret,
        )

        ssl_credentials = None
        if settings.ssl_settings:
            cert_chain = read_file_bytes(settings.ssl_settings.cert_file)
            cert = read_file_bytes(settings.ssl_settings.cert_key_file)
            ca_cert = read_file_bytes(settings.ssl_settings.ca_file)

            LOG.debug("Using a secure gRPC connection:")
            LOG.debug("    target: %s", target)
            LOG.debug("    root_certificates: contents of %s", settings.ssl_settings.ca_file)
            LOG.debug("    private_key: contents of %s", settings.ssl_settings.cert_key_file)
            LOG.debug("    certificate_chain: contents of %s", settings.ssl_settings.cert_file)

            ssl_credentials = ssl_channel_credentials(
                root_certificates=ca_cert, private_key=cert, certificate_chain=cert_chain
            )
        return secure_authorized_channel(
            credentials,
            RefreshRequester(),
            target,
            ssl_credentials=ssl_credentials,
            options=options,
        )

    if settings.ssl_settings:
        cert_chain = read_file_bytes(settings.ssl_settings.cert_file)
        cert = read_file_bytes(settings.ssl_settings.cert_key_file)
        ca_cert = read_file_bytes(settings.ssl_settings.ca_file)

        LOG.debug("Using a secure gRPC connection:")
        LOG.debug("    target: %s", target)
        LOG.debug("    root_certificates: contents of %s", settings.ssl_settings.ca_file)
        LOG.debug("    private_key: contents of %s", settings.ssl_settings.cert_key_file)
        LOG.debug("    certificate_chain: contents of %s", settings.ssl_settings.cert_file)

        credentials = ssl_channel_credentials(
            root_certificates=ca_cert, private_key=cert, certificate_chain=cert_chain
        )
        return secure_channel(target, credentials, options)
    else:
        LOG.debug("Using an insecure gRPC connection...")
        return insecure_channel(target, options)


class GRPCv1Connection(_LedgerConnection):
    def __init__(
        self,
        invoker: "Invoker",
        options: "LedgerConnectionOptions",
        settings: "HTTPConnectionSettings",
        context_path: "Optional[str]",
    ):
        super(GRPCv1Connection, self).__init__(invoker, options, settings, context_path)
        from . import model as G

        self._closed = Event()
        self._channel = grpc_create_channel(settings)
        self.active_contract_set_service = G.ActiveContractsServiceStub(self._channel)
        self.command_service = G.CommandServiceStub(self._channel)
        self.transaction_service = G.TransactionServiceStub(self._channel)
        self.package_service = G.PackageServiceStub(self._channel)
        self.package_management_service = G.PackageManagementServiceStub(self._channel)
        self.ledger_identity_service = G.LedgerIdentityServiceStub(self._channel)
        self.time_service = G.TimeServiceStub(self._channel)

    def close(self):
        try:
            self._closed.set()
            self._channel.close()
        except:
            LOG.warning("An exception was thrown when trying to close down connections.")
        finally:
            super().close()

    @property
    def closed(self) -> bool:
        return self._closed.is_set()
