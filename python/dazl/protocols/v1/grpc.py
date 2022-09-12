# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Support for the gRPC-based Ledger API.
"""
from asyncio import gather
from datetime import datetime
from threading import Event
from time import sleep
from typing import TYPE_CHECKING, AbstractSet, Iterable, Mapping, Optional, Sequence, cast
import warnings

from grpc import (
    Channel,
    RpcError,
    StatusCode,
    insecure_channel,
    secure_channel,
    ssl_channel_credentials,
)

from ... import LOG
from ..._gen.com.daml.ledger.api import v1 as lapipb
from ..._gen.com.daml.ledger.api.v1 import admin as lapiadminpb, testing as lapitestingpb
from ...damlast.daml_lf_1 import PackageRef
from ...damlast.parse import parse_archive_payload
from ...ledger.aio.pkgloader_compat import PackageLoader
from ...prim import Party, TimeDeltaLike, datetime_to_timestamp, to_party, to_timedelta
from ...scheduler import Invoker, RunLevel
from ...util.io import read_file_bytes
from ...util.typing import safe_cast
from .._base import LedgerClient, LedgerConnectionOptions, _LedgerConnection
from ..errors import ConnectionTimeoutError, UserTerminateRequest
from .pb_parse_event import (
    BaseEventDeserializationContext,
    serialize_acs_request,
    serialize_transactions_request,
    to_acs_events,
    to_transaction_events,
)

with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)

    if TYPE_CHECKING:
        from ...client.commands import CommandPayload
        from ...client.ledger import LedgerMetadata
        from ...model.network import HTTPConnectionSettings
        from ...model.reading import BaseEvent, ContractFilter, TransactionFilter
        from ...model.types_store import PackageProvider, PackageStore


__all__ = [
    "GRPCv1LedgerClient",
    "grpc_set_time",
    "grpc_upload_package",
    "grpc_detect_ledger_id",
    "grpc_main_thread",
    "GRPCPackageProvider",
    "grpc_package_sync",
    "grpc_create_channel",
    "GRPCv1Connection",
]


class GRPCv1LedgerClient(LedgerClient):
    def __init__(self, connection: "GRPCv1Connection", ledger: "LedgerMetadata", party: Party):
        self.connection = safe_cast(GRPCv1Connection, connection)
        self.ledger = ledger
        self.party = to_party(party)

    async def commands(self, command_payload: "CommandPayload") -> None:
        from .pb_ser_command import ProtobufSerializer

        serializer = cast(ProtobufSerializer, self.ledger.serializer)
        request = serializer.serialize_command_request(command_payload)
        await self.connection.invoker.run_in_executor(
            lambda: self.connection.command_service.SubmitAndWait(request)
        )
        return None

    async def commands_transaction(self, __1: "CommandPayload") -> lapipb.Transaction:
        from .pb_ser_command import ProtobufSerializer

        serializer = cast(ProtobufSerializer, self.ledger.serializer)
        request = serializer.serialize_command_request(__1)
        response = await self.connection.invoker.run_in_executor(
            lambda: self.connection.command_service.SubmitAndWaitForTransaction(request)
        )
        return response.transaction

    async def commands_transaction_tree(self, __1: "CommandPayload") -> lapipb.TransactionTree:
        from .pb_ser_command import ProtobufSerializer

        serializer = cast(ProtobufSerializer, self.ledger.serializer)
        request = serializer.serialize_command_request(__1)
        response = await self.connection.invoker.run_in_executor(
            lambda: self.connection.command_service.SubmitAndWaitForTransactionTree(request)
        )
        return response.transaction

    async def active_contracts(self, contract_filter: "ContractFilter") -> "Sequence[BaseEvent]":
        with LOG.info_timed("ACS request serialization"):
            request = serialize_acs_request(contract_filter, self.ledger.ledger_id, self.party)
            context = BaseEventDeserializationContext(
                None,
                self.connection.options.lookup,
                self.ledger._store,
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
            acs_responses = list(acs_stream)

        with LOG.info_timed("ACS find all required packages"):
            pkg_refs = {
                create_evt.template_id.package_id
                for acs_response_pb in acs_responses
                for create_evt in acs_response_pb.active_contracts
            }

        if pkg_refs:
            with LOG.info_timed(f"ACS load {len(pkg_refs)} new package(s)"):
                # Preload packages that are DIRECTLY referenced by packages in the message
                await gather(
                    *(self.ledger.package_loader.load(PackageRef(pkg_ref)) for pkg_ref in pkg_refs)
                )

        with LOG.info_timed("ACS transform the message"):
            # Now load all the events. Note that do_with_retry is still required because the
            # packages that contained templates might have references to other packages that are
            # also required to understand the individual fields in a template.
            return await self.ledger.package_loader.do_with_retry(
                lambda: to_acs_events(context, acs_responses)
            )

    async def events(self, transaction_filter: "TransactionFilter") -> "Sequence[BaseEvent]":
        request = serialize_transactions_request(
            transaction_filter, self.ledger.ledger_id, self.party
        )
        context = BaseEventDeserializationContext(
            None,
            self.connection.options.lookup,
            self.ledger._store,
            self.party,
            self.ledger.ledger_id,
        )

        tx_future = self.connection.invoker.run_in_executor(
            lambda: self.connection.transaction_service.GetTransactions(request)
        )

        tt_stream = None  # type: Optional[Iterable[lapipb.GetTransactionTreesResponse]]
        if transaction_filter.templates is None:
            # Filtering by package must disable the ability to handle exercise nodes; we may want to
            # consider dropping client-side support for exercise events anyway because they are not
            # widely used
            tt_stream = await self.connection.invoker.run_in_executor(
                lambda: self.connection.transaction_service.GetTransactionTrees(request)
            )

        tx_stream = await tx_future

        return await self.ledger.package_loader.do_with_retry(
            lambda: to_transaction_events(
                context, tx_stream, tt_stream, transaction_filter.destination_offset
            )
        )

    async def events_end(self) -> str:
        request = lapipb.GetLedgerEndRequest(ledger_id=self.ledger.ledger_id)
        return await self.connection.invoker.run_in_executor(
            lambda: self.connection.transaction_service.GetLedgerEnd(request).offset.absolute
        )


def grpc_set_time(connection: "GRPCv1Connection", ledger_id: str, new_datetime: datetime) -> None:
    get_request = lapitestingpb.GetTimeRequest(ledger_id=ledger_id)
    get_response = connection.time_service.GetTime(get_request)
    ts = next(iter(get_response))

    set_request = lapitestingpb.SetTimeRequest(
        ledger_id=ledger_id,
        current_time=ts.current_time,
        new_time=datetime_to_timestamp(new_datetime),
    )
    connection.time_service.SetTime(set_request)
    LOG.info("Time on the server changed by the local client to %s.", new_datetime)


def grpc_upload_package(connection: "GRPCv1Connection", dar_contents: bytes) -> None:
    request = lapiadminpb.UploadDarFileRequest(dar_file=dar_contents)
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
                lapipb.GetLedgerIdentityRequest()
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


# noinspection PyDeprecation
def grpc_main_thread(connection: "GRPCv1Connection", ledger_id: str) -> "Iterable[LedgerMetadata]":
    from ...client.ledger import LedgerMetadata
    from .pb_ser_command import ProtobufSerializer

    LOG.info("grpc_main_thread...")

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        from ...model.types_store import PackageStore

        store = PackageStore.empty()

        package_provider = GRPCPackageProvider(connection, ledger_id)

        if connection.options.eager_package_fetch:
            grpc_package_sync(package_provider, store)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        package_loader = PackageLoader(
            package_lookup=connection.options.lookup,
            conn=package_provider,
            timeout=connection.options.connect_timeout,
        )

    yield LedgerMetadata(
        ledger_id=ledger_id,
        store=store,
        package_loader=package_loader,
        serializer=ProtobufSerializer(connection.options.lookup),
        protocol_version="v1",
    )

    # poll for package updates once a second
    while not connection._closed.wait(1):
        try:
            if connection.options.eager_package_fetch:
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", DeprecationWarning)
                    grpc_package_sync(package_provider, store)
        except Exception as ex:
            if not isinstance(ex, RpcError) or ex.code() != StatusCode.CANCELLED:
                LOG.warning("Package syncing raised an exception.", exc_info=True)

    LOG.debug("The gRPC monitor thread is now shutting down.")


class GRPCPackageProvider:
    def __init__(self, connection: "GRPCv1Connection", ledger_id: str):
        self.connection = connection
        self.ledger_id = ledger_id

    def package_ids(self, *, timeout: Optional[TimeDeltaLike] = None) -> AbstractSet[PackageRef]:
        timeout_secs = to_timedelta(timeout).total_seconds() if timeout is not None else None
        request = lapipb.ListPackagesRequest(ledger_id=self.ledger_id)
        response = self.connection.package_service.ListPackages(request, timeout=timeout_secs)
        return frozenset([PackageRef(p) for p in response.package_ids])

    def package_bytes(
        self, package_id: PackageRef, *, timeout: Optional[TimeDeltaLike] = None
    ) -> bytes:
        timeout_secs = to_timedelta(timeout).total_seconds() if timeout is not None else None
        request = lapipb.GetPackageRequest(ledger_id=self.ledger_id, package_id=package_id)
        package_info = self.connection.package_service.GetPackage(request, timeout=timeout_secs)
        return package_info.archive_payload

    def get_package_ids(self) -> "AbstractSet[PackageRef]":
        return self.package_ids()

    def fetch_package(self, package_id: "PackageRef") -> bytes:
        return self.package_bytes(package_id)

    def get_all_packages(self) -> "Mapping[PackageRef, bytes]":
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            return {pkg_id: self.fetch_package(pkg_id) for pkg_id in self.get_package_ids()}


# noinspection PyDeprecation
def grpc_package_sync(package_provider: "PackageProvider", store: "PackageStore") -> "None":
    warnings.warn(
        "grpc_package_sync is deprecated; there is no replacement", DeprecationWarning, stacklevel=2
    )

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        from .pb_parse_metadata import find_dependencies, parse_daml_metadata_pb

        LOG.debug("grpc_package_sync started...")

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        all_package_ids = package_provider.get_package_ids()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            loaded_package_ids = {a.hash for a in store.archives()}
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            expected_package_ids = store.expected_package_ids()

        def should_load(p: str) -> bool:
            # TODO: Filtering by expected package IDs may cause packages to never fully load due to
            #  transitive dependencies; here we put the onus on the app writer to ensure that they
            #  supply the complete graph, and we don't even warn them if there is an issue (but
            #  we could only actually warn them if we parse the archive, which is the expensive
            #  operation we're trying to avoid).
            return (
                expected_package_ids is None or p in expected_package_ids
            ) and p not in loaded_package_ids

        metadatas_pb = {}
        for package_id in all_package_ids:
            if should_load(package_id):
                archive_payload = package_provider.fetch_package(package_id)
                metadatas_pb[package_id] = parse_archive_payload(package_id, archive_payload)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        adr = find_dependencies(metadatas_pb, loaded_package_ids)

    for package_id, archive_bytes in adr.sorted_archives.items():
        m = parse_daml_metadata_pb(package_id, archive_bytes)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            store.register_all(m)

    LOG.debug("grpc_package_sync ended.")


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
        self._closed = Event()
        self._channel = grpc_create_channel(settings)
        self.active_contract_set_service = lapipb.ActiveContractsServiceStub(self._channel)
        self.command_service = lapipb.CommandServiceStub(self._channel)
        self.transaction_service = lapipb.TransactionServiceStub(self._channel)
        self.package_service = lapipb.PackageServiceStub(self._channel)
        self.package_management_service = lapiadminpb.PackageManagementServiceStub(self._channel)
        self.ledger_identity_service = lapipb.LedgerIdentityServiceStub(self._channel)
        self.time_service = lapitestingpb.TimeServiceStub(self._channel)

    def close(self):
        try:
            LOG.info("Closing a GRPCv1Connection channel...")
            self._closed.set()
            self._channel.close()
        except:
            LOG.warning("An exception was thrown when trying to close down connections.")
        finally:
            super().close()

    @property
    def closed(self) -> bool:
        return self._closed.is_set()
