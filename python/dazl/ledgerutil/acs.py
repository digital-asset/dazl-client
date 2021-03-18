# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from collections.abc import MutableMapping
from operator import delitem, setitem
from typing import Dict, Iterator, Optional, TypeVar, Union

from ..damlast.daml_lf_1 import TypeConName
from ..ledger.grpc.conn_aio import QueryStream
from ..prim import ContractData, ContractId

__all__ = ["ACS"]

from ..query import ContractMatch, is_match

T = TypeVar("T")


class ACS(MutableMapping):
    """
    An accumulation of active contracts up to a certain point in time over a provided stream.

    This class is meant to represent a _local_ in-memory view of an active contract set. It is _not_
    a direct wrapper over the API; it is merely offered as a simple utility class to avoid
    repetitive code that looks like this:

    .. code-block: python

        class MyService:
            def __init__(self, conn):
                self._conn = conn
                self._widgets = dict()

            async def run(self):
                async with self._conn.stream("WidgetMod:Widget") as stream:
                    async for ev in stream.events():
                        if isinstance(ev, CreateEvent):
                            self._widgets[ev.contract_id] = ev.payload
                        elif isinstance(ev, ArchiveEvent):
                            self._widgets.pop(ev.contract_id)

            def widget_json(self, widget_id: str):
                for cdata in self._widgets.values():
                    if cdata['id'] == widget_id:
                        return cdata
                return None

    With the ACS helper class:

    .. code-block: python

        class MyService:
            def __init__(self, conn):
                self._conn = conn
                self._widgets = ACS.empty()

            async def run(self):
                async with self._conn.stream("WidgetMod:Widget") as stream:
                    self._widgets = ACS.from_stream(stream, "WidgetMod:Widget")
                    await stream.run()

            def widget_json(self, widget_id: str):
                return self._widgets.first_payload({"id": widget_id})

    """

    @classmethod
    def empty(cls) -> ACS:
        return ACS()

    @classmethod
    def from_stream(cls, stream: QueryStream, template_id: Union[str, TypeConName]):
        acs = ACS()
        stream.on_create(template_id, lambda e: setitem(acs._contracts, e.contract_id, e.payload))
        stream.on_archive(template_id, lambda e: delitem(acs._contracts, e.contract_id))
        return acs

    def __init__(self):
        self._contracts = {}  # type: Dict[ContractId, ContractData]

    def __contains__(self, key: ContractId) -> bool:
        return key in self._contracts

    def __getitem__(self, key: ContractId) -> ContractData:
        return self._contracts[key]

    def __setitem__(self, key: ContractId, payload: ContractData) -> None:
        self._contracts[key] = payload

    def __delitem__(self, key: ContractId) -> None:
        del self._contracts[key]

    def __iter__(self) -> Iterator[ContractId]:
        return iter(self._contracts)

    def __len__(self) -> int:
        return len(self._contracts)

    def clear(self) -> None:
        self._contracts.clear()

    def first_payload(self, predicate: ContractMatch) -> Optional[ContractData]:
        for value in self._contracts.values():
            if is_match(predicate, value):
                return value
        return None

    def __repr__(self):
        return f"ACS(len={len(self)})"
