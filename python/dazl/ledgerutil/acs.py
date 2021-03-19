# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from collections.abc import Mapping
from operator import delitem, setitem
import types
from typing import Dict, Iterator, Optional, TypeVar, Union

from ..damlast.daml_lf_1 import TypeConName
from ..ledger.grpc.conn_aio import QueryStream
from ..prim import ContractData, ContractId

__all__ = ["ACS"]

from ..query import ContractMatch, is_match

T = TypeVar("T")


class ACS:
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
                self._widgets = ACS.empty("WidgetMod:Widget")

            async def run(self):
                async with self._conn.stream("WidgetMod:Widget") as stream:
                    self._widgets = ACS.from_stream(stream, "WidgetMod:Widget")
                    await stream.run()

            def widget_json(self, widget_id: str):
                return self._widgets.snapshot().first_payload({"id": widget_id})

    """

    @classmethod
    def empty(cls, template_id: Union[str, TypeConName]) -> ACS:
        return ACS(None, template_id)

    @classmethod
    def from_stream(cls, stream: QueryStream, template_id: Union[str, TypeConName]):
        acs = ACS(0, template_id)
        stream.on_create(template_id, lambda e: acs._set_item(e.contract_id, e.payload))
        stream.on_archive(template_id, lambda e: acs._del_item(e.contract_id))
        return acs

    def __init__(self, serial_number: Optional[int], template_id: Union[str, TypeConName]):
        self._contracts = {}  # type: Dict[ContractId, ContractData]
        self._serial_number = serial_number
        self._template_id = template_id

    def _notice_change(self):
        if self._serial_number is not None:
            self._serial_number = self._serial_number + 1

    def _set_item(self, key: ContractId, payload: ContractData) -> None:
        self._notice_change()
        setitem(self._contracts, key, payload)

    def _del_item(self, key: ContractId) -> None:
        self._notice_change()
        delitem(self._contracts, key)

    def snapshot(self) -> Mapping[ContractId, ContractData]:
        """
        Create a snapshot of the _current_ state of the ACS. Useful if you need a consistent view
        of the ACS at a point in time.
        """
        return types.MappingProxyType(dict(self._contracts))

    def first_payload(self, predicate: ContractMatch) -> Optional[ContractData]:
        for value in self._contracts.values():
            if is_match(predicate, value):
                return value
        return None

    def __repr__(self):
        serno = self._serial_number or "EMPTY-NOT-CONNECTED"
        return f"ACS(len={len(self)}, serial={serno}, tid={self._template_id})"
