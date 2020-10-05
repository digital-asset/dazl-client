# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from datetime import datetime
from typing import AbstractSet, Dict, Iterable, Iterator, Optional

__all__ = ['Formatter', 'RowBuilder', 'TableBuilder']

from ...model.core import ContractId, ContractData, Party
from ...model.types_store import PackageStore


class Formatter:
    """
    A formatter is a particular way of representing a list of rows that represent contracts visible
    by a set of parties.
    """

    def render(
            self,
            store: 'PackageStore',
            parties: 'AbstractSet[Party]',
            entries: 'Iterable[RowBuilder]') -> 'Iterator[str]':
        """
        Render the set of entries.

        :param store: The store that contains type information.
        :param parties: Set of parties to render.
        :param entries: A list of entries to render.
        :return: An asynchronous generator over string lines that make up the rendering.
        """
        raise NotImplementedError('render needs an implementation')


class TableBuilder:
    """
    State built up during a ledger run.
    """
    def __init__(self):
        self.entries = dict()  # type: Dict[ContractId, RowBuilder]

    def add(
            self,
            party: 'Party',
            cid: 'ContractId',
            cdata: 'Optional[ContractData]',
            time: 'Optional[datetime]' = None) -> None:
        entry = self.entries.get(cid)
        if entry is not None:
            entry.extend(party, cdata)
        else:
            self.entries[cid] = RowBuilder(party, cid, cdata, time)

    def excluding_inactive(self) -> 'Iterator[RowBuilder]':
        return filter(lambda e: not e.is_archived(), self)

    def filtered_by(self, predicate) -> 'Iterator[RowBuilder]':
        return filter(predicate, self)

    def __iter__(self) -> 'Iterator[RowBuilder]':
        return iter(self.entries.values())

    def __repr__(self) -> str:
        return '<LedgerCapture(entry_count={!r})>'.format(len(self.entries))


class RowBuilder:
    """
    Represents a single "row" in the final output. This is a consolidation over the view that
    various parties see for a particular :class:`ContractId`.
    """
    def __init__(
            self,
            party: 'Party',
            cid: 'ContractId',
            cdata: 'ContractData',
            time: 'Optional[datetime]'):
        self.parties = {party: True}  # type: Dict[Party, bool]
        self.cid = cid
        self.cdata = cdata
        self.time = time
        self.errors = []

    def extend(self, party: 'Party', cdata: 'ContractData') -> None:
        self.parties[party] = cdata is not None

    def is_archived(self) -> bool:
        return all(not active for active in self.parties.values())

    def contract_state(self, party: 'Party') -> 'Optional[str]':
        p = self.parties.get(party)
        if p is not None:
            return "CREATED" if p else "ARCHIVED"
        else:
            return None

    def __repr__(self) -> str:
        return f'LedgerEntry(parties={self.parties}, cid={self.cid}, cdata={self.cdata})'