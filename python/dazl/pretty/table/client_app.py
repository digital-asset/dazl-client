# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains utilities for deterministically outputting contract information.
"""

import sys
from collections import defaultdict
from typing import Collection, Iterable, TextIO, Optional, Union, TYPE_CHECKING
from typing import Dict, Iterator

from .fmt_base import get_formatter
from ...model.core import ContractId, ContractData, Party
from ...model.types_store import PackageStore

if TYPE_CHECKING:
    from ...client import Network


def collate_entries(metadata, parties, entries):
    """
    Return entries as a dict of :class:`TemplateMetadata` to list of :class:`LedgerCaptureEntry`.
    """
    sort = EntrySorter(parties)

    entries_by_template = defaultdict(list)
    for entry in entries:
        entries_by_template[entry.template_id].append(entry)

    grouped_entries = []
    for template_id, entries in entries_by_template.items():
        template = metadata.templates.find(template_id)
        entries.sort(key=sort.key)
        grouped_entries.append((template, entries))

    grouped_entries.sort(key=lambda t: t[0].template_name)
    return dict(grouped_entries)


class EntrySorter:
    """
    Implementation of a sort key method for :class:`LedgerCaptureEntry`.
    """

    def __init__(self, parties):
        self.parties = parties

    def key(self, entry):
        """
        Return an expression that can be used as an absolute sorting value as a proxy for this
        entry.
        """
        party_vis = [1 if entry.parties.get(party) is not None else 0 for party in self.parties]
        return sum(party_vis), ''.join(map(str, reversed(party_vis)))


class LedgerCapture:
    """
    State built up during a ledger run.
    """

    def __init__(self):
        self.entries = dict()  # type: Dict[ContractId, LedgerCaptureEntry]
        self.store: Optional[PackageStore] = None

    def capture(self, party: str, contract_id: ContractId, contract_data: Optional[ContractData], time = None):
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


class LedgerCaptureApp:
    """
    Plugin that passively listens to the event stream on all parties. Call :meth:`dump_all` to
    render what it sees.
    """

    @classmethod
    def stdout(cls, **kwargs) -> 'LedgerCaptureApp':
        """
        Return a :class:`LedgerCapturePlugin` that writes its output to stdout.
        """
        return cls(sys.stdout, False, **kwargs)

    @classmethod
    def stderr(cls, **kwargs) -> 'LedgerCaptureApp':
        """
        Return a :class:`LedgerCapturePlugin` that writes its output to stderr.
        """
        return cls(sys.stderr, False, **kwargs)

    @classmethod
    def to_file(cls, path, **kwargs) -> 'LedgerCaptureApp':
        """
        Return a :class:`LedgerCapturePlugin` that writes its output to a file.

        :param path: The file to write to.
        """
        return cls(open(path, 'w'), True, **kwargs)

    def __init__(self,
                 buf: TextIO,
                 buf_close: bool,
                 template_filter: 'Optional[Iterable[str]]' = None,
                 include_archived: bool = False):
        """
        Initialize a :class:`LedgerCapturePlugin`.

        :param buf:
            The buffer to write ledger state to.
        :param buf_close:
            ``True`` to close ``buf`` after fully dumping the contents of the ledger;
            ``False`` to keep ``buf`` open.
        :param template_filter:
            A list of ``str`` of template names. The default value is ``None``, which includes all
            templates.
        :param include_archived:
            ``True`` to include archived contracts in the output;
            otherwise, ``False`` (the default).
        """
        self.buf = buf
        self.buf_close = buf_close
        self.template_filter = template_filter
        self.include_archived = include_archived
        self.manager = None
        self.store = None

    def dump_all(self, fmt=None, parties=None, include_archived=None, **kwargs) -> None:
        """
        Write all entries captured by the plugin to the provided buffer.

        :param fmt:
            Format of the output; currently either ``"json"`` or ``"pretty"``.
        :param parties:
            An optional list of parties. If unspecified, the list is taken from the list of parties
            connected to the client.
        :param include_archived:
            ``None`` to use the default value passed in the constructor; ``True`` to include
            archived contracts in the output; otherwise, ``False``.
        :param kwargs:
            Parameters passed directly to the formatter.
        """
        formatter = get_formatter(fmt)

        if self.manager is None:
            lines = formatter.format_error('Plugin not initialized')
        else:
            if parties is None:
                parties = sorted(self.manager.parties())

            include_archived = include_archived if include_archived is not None \
                else self.include_archived

            capture = LedgerCapture()
            capture.store = self.store
            for party in self.manager.parties():
                client = self.manager.client(party)

                if include_archived:
                    for cid, (cdata, state) in client.select('*', include_archived=True).items():
                        if cdata is not None:
                            capture.capture(party, cid, cdata)
                        if not state:
                            capture.capture(party, cid, None)
                else:
                    for cid, cdata in client.select('*').items():
                        capture.capture(party, cid, cdata)

            lines = formatter.format_entries(
                capture=capture,
                parties=parties,
                entries=capture,
                **kwargs)

        for line in lines:
            self.buf.write(line + '\n')


def write_acs(
        buf: 'TextIO',
        network: 'Network',
        fmt: 'Optional[str]' = None,
        parties: 'Collection[Union[str, Party]]' = None,
        include_archived: bool = False,
        **kwargs) \
        -> None:
    """
    Write all entries captured by the plugin to the provided buffer.

    :param buf:
        The buffer to write to.
    :param network:
        The network to write data from.
    :param fmt:
        Format of the output; currently either ``"json"`` or ``"pretty"``.
    :param parties:
        An optional list of parties. If unspecified, the list is taken from the list of parties
        connected to the client.
    :param include_archived:
        ``True`` to include archived contracts in the output; otherwise, ``False``.
    :param kwargs:
        Parameters passed directly to the formatter.
    """
    formatter = get_formatter(fmt)

    if parties is None:
        parties = sorted(network.parties())

    capture = LedgerCapture()
    capture.store = network.simple_global().metadata().store
    for party in parties:
        # TODO: This is a hack because ACS calls on a simple_party instance don't really work once
        #   the loop is closed.
        client = network.aio_party(party)

        for cxdata in client.find_historical('*'):
            if cxdata.active:
                capture.capture(party, cxdata.cid, cxdata.cdata, cxdata.effective_at)
            elif include_archived:
                capture.capture(party, cxdata.cid, None, None)

    lines = formatter.format_entries(
        capture=capture,
        parties=parties,
        entries=capture,
        **kwargs)

    for line in lines:
        buf.write(line + '\n')
