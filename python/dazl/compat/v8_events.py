# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, NoReturn, Optional, Union
import warnings

from . import NotSupportedError, _messages
from ..damlast.protocols import SymbolLookup
from ..model.core import ContractContextualData
from ..prim import ContractData, ContractId
from ..protocols.core import ArchiveEvent, CreateEvent

if TYPE_CHECKING:
    from ..model.types import TypeReference
    from .v8_client_aio import AIOPartyClient


class BaseEvent:
    """
    Base class for an event hierarchy that exposes the same API as dazl.model.reading events, but
    with appropriate deprecation warnings that help guide consumers to better alternatives.
    """

    def __init__(self, client: "AIOPartyClient"):
        self._client = client

    @property
    def client(self) -> "AIOPartyClient":
        return self._client

    @property
    def party(self):
        """
        Return the party for the connection that triggered this event.

        Note that with multi-party submissions, there may not be a such thing as a singular "Party"
        for a connection any more; if you are using this property, you will need to find another
        mechanism for identifying the relevant Party in order to be compatible with multi-party
        submissions. As such, this property is deprecated.
        """
        warnings.warn(
            "reading `party` from a connection is ambiguous when multi-party submissions are "
            "being used; consider an alternate way of determining the relevant party",
            DeprecationWarning,
            stacklevel=2,
        )
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            return self._client.party

    @property
    def time(self) -> "None":
        warnings.warn("time is not exposed in the new API", DeprecationWarning, stacklevel=2)
        return None

    @property
    def ledger_id(self) -> str:
        """
        Return the ledger ID of the connected ledger.
        """
        return self._client._conn.config.access.ledger_id

    @property
    def lookup(self) -> "SymbolLookup":
        """
        Return the :class:`SymbolLookup` that provides access to package metadata.
        """
        warnings.warn("use Connection.codec.lookup instead", DeprecationWarning, stacklevel=2)
        # noinspection PyProtectedMember
        return self._client._conn.codec.lookup

    @property
    def package_store(self) -> "NoReturn":
        warnings.warn("package_store is not supported", DeprecationWarning, stacklevel=2)
        raise NotSupportedError("package_store is not supported")

    def acs_find_active(self, template: "Union[TypeReference, str]", match=None):
        warnings.warn("ACS functions are deprecated", DeprecationWarning, stacklevel=2)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            return self.client.find_one(template, match)

    def acs_find_by_id(self, cid: "Union[str, ContractId]") -> "Optional[ContractContextualData]":
        warnings.warn("ACS functions are deprecated", DeprecationWarning, stacklevel=2)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            return self.client.find_by_id(cid)

    def acs_find_one(self, template: "Union[TypeReference, str]", match=None):
        warnings.warn("ACS functions are deprecated", DeprecationWarning, stacklevel=2)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            return self.client.find_one(template, match=match)

    def acs_find_historical(self, template: "Union[TypeReference, str]", match=None):
        warnings.warn("ACS functions are deprecated", DeprecationWarning, stacklevel=2)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            return self.client.find_historical(template, match)

    def acs_find_nonempty(self, template: "Union[TypeReference, str]", match=None):
        warnings.warn("ACS functions are deprecated", DeprecationWarning, stacklevel=2)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            # noinspection PyDeprecation
            return self.client.find_nonempty(template, match=match)


class InitEvent(BaseEvent):
    pass


class OffsetEvent(BaseEvent):
    @property
    def offset(self) -> "NoReturn":
        warnings.warn("offset is no longer accessible in the new API")
        raise NotSupportedError("offset is no longer accessible in the new API")


class ReadyEvent(OffsetEvent):
    pass


class ContractEvent(OffsetEvent):
    @property
    def command_id(self) -> "NoReturn":
        """
        Raises NotSupportedError; ``command_id`` is no longer accessible in the new API.
        """
        warnings.warn(_messages.COMMAND_ID, DeprecationWarning, stacklevel=2)
        raise NotSupportedError(_messages.COMMAND_ID)

    @property
    def workflow_id(self) -> "NoReturn":
        """
        Raises NotSupportedError; ``workflow_id`` is no longer accessible in the new API.
        """
        warnings.warn(_messages.WORKFLOW_ID, DeprecationWarning, stacklevel=2)
        raise NotSupportedError(_messages.WORKFLOW_ID)

    @property
    def event_id(self) -> "NoReturn":
        """
        Raises NotSupportedError; ``event_id`` is no longer accessible in the new API.
        """
        warnings.warn(_messages.EVENT_ID, DeprecationWarning, stacklevel=2)
        raise NotSupportedError(_messages.EVENT_ID)

    @property
    def witness_parties(self) -> "NoReturn":
        """
        Raises NotSupportedError; ``witness_parties`` is no longer accessible in the new API.
        """
        warnings.warn(_messages.WITNESS_PARTIES, DeprecationWarning, stacklevel=2)
        raise NotSupportedError(_messages.WITNESS_PARTIES)


class ContractCreateEvent(ContractEvent):
    def __init__(self, client: "Any", base_event: "CreateEvent"):
        super().__init__(client)
        self._base_event = base_event

    @property
    def cid(self) -> "ContractId":
        return self._base_event.cid

    @property
    def cdata(self) -> "ContractData":
        return self._base_event.cdata


class ContractArchiveEvent(ContractEvent):
    def __init__(self, client: "Any", base_event: "ArchiveEvent"):
        super().__init__(client)
        self._base_event = base_event

    @property
    def cid(self) -> "ContractId":
        return self._base_event.cid
