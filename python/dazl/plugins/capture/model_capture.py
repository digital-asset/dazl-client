# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Object model for data capture.
"""

from typing import Dict, Iterator, Optional

from ...model.core import ContractId, ContractData
from ...model.types_store import PackageStore


class LedgerCapture:
    """
    State built up during a ledger run.
    """
    def __init__(self):
        self.entries = dict()  # type: Dict[ContractId, LedgerCaptureEntry]
        self.store: Optional[PackageStore] = None

    def capture(self, party: str, contract_id: ContractId, contract_data: Optional[ContractData], time):
        entry = self.entries.get(contract_id)
        if entry is not None:
            entry.extend(party, contract_id, contract_data)
        else:
            self.entries[contract_id] = LedgerCaptureEntry(party, contract_id, contract_data, time)

    def capture_archive(self, party: str, contract_id: ContractId):
        return self.capture(party, contract_id, None)

    def excluding_inactive(self):
        return filter(lambda e: not e.is_archived(), self)

    def filtered_by(self, predicate):
        return filter(predicate, self)

    def __iter__(self) -> 'Iterator[LedgerCaptureEntry]':
        return iter(self.entries.values())

    def __repr__(self):
        return '<LedgerCapture(entry_count={!r})>'.format(len(self.entries))


class LedgerCaptureEntry:
    def __init__(self, party, contract_id, contract_data, time):
        self.parties = {party: True}
        self.contract_id = contract_id
        self.template_id = contract_id.template_id
        self.contract_args = contract_data
        self.time = time
        self.errors = []

    def extend(self, party, _, contract_data):
        active = contract_data is not None
        self.parties[party] = active

        if active:
            # make sure this party is seeing a consistent view of the same contract
            pass

    def is_archived(self):
        return all(not active for active in self.parties.values())

    def contract_state(self, party):
        p = self.parties.get(party)
        if p is not None:
            return "CREATED" if p else "ARCHIVED"
        else:
            return None

    def __repr__(self):
        return '<LedgerEntry(parties={}, contract_id={}, template_id={}, contract_args={})>'.format(
            self.parties, self.contract_id, self.template_id, self.contract_args)

