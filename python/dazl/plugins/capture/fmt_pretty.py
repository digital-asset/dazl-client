# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Pretty print format that orders templates by ID, and attempts to render a more compact
representation.
"""

import re

from collections import defaultdict
from typing import Iterable, Optional

from .model_capture import LedgerCapture, LedgerCaptureEntry
from dazl.util.termcap import termsize
from ...model.types import Type, RecordType

BOX_B3 = '|'
BOX_C4 = '-'
BOX_DA = '+'


# a list of template parameter names that are long and make it tough to understand
# what is going on when written out as a single line
_COMMON_PREFIXES = ['invitedAs']


class _TemplateKey:
    """
    Type that identifies templates for display purposes.
    """
    @staticmethod
    def unknown(identifier: str) -> '_TemplateKey':
        return _TemplateKey(identifier, None)

    @staticmethod
    def for_record_type(record_type: RecordType) -> '_TemplateKey':
        return _TemplateKey(
            '.'.join(record_type.name.module.module_name + record_type.name.name),
            record_type)

    def __init__(self, template_name: str, data_type: Optional[Type]):
        self.template_name = template_name
        self.data_type = data_type


def format_error(error: str) -> Iterable[str]:
    return [error]


def format_entries(capture: LedgerCapture,
                   parties: Iterable[str],
                   entries: Optional[Iterable[LedgerCaptureEntry]]=None,
                   color: bool=True,
                   columns: Optional[int]=None) -> Iterable[str]:
    if columns is None:
        _, columns = termsize()
        if columns is None:
            columns = 120

    sort = ByPartySort(parties)

    entries_by_template = defaultdict(list)
    if entries is None:
        entries = capture

    for entry in entries:
        entries_by_template[entry.template_id].append(entry)

    grouped_entries = []
    for template_id, entries in entries_by_template.items():
        # try to resolve a template for the template ID
        template_type = None
        if capture.store is not None:
            candidates = capture.store.resolve_template_type(template_id)
            if len(candidates) == 1:
                template_type = next(iter(candidates.values()))

        # if we can successfully resolve metadata and render instances of this template nicely,
        # then use that rendering; otherwise resort to a rougher display
        key = _TemplateKey.for_record_type(template_type) if template_type is not None \
            else _TemplateKey.unknown(template_id)
        grouped_entries.append((key, entries))

    grouped_entries.sort(key=lambda t: t[0].template_name)

    entry_count = sum(len(entries) for entries in entries_by_template.values())

    yield "{} total contracts over {} templates".format(entry_count, len(entries_by_template))
    yield from party_header(parties)
    for template, entries in grouped_entries:
        # for each column for all entries in the data set, determine the most
        # compact representation here
        yield ''

        renderer = _TemplateEntryRenderer(template, parties)
        renderer.measure(entries)

        yield from renderer.render_header(color=color, columns=columns)
        yield from renderer.render_entries(sorted(entries, key=sort.key))


def party_header(parties):
    parties = tuple(parties)
    party_count = len(parties)

    for index, party in enumerate(parties):
        ascii_art = (BOX_B3 * index) + BOX_DA + (BOX_C4 * (party_count - index - 1))
        yield f"{ascii_art} party '{party}'"
    yield (('|' * party_count))


class ByPartySort:
    def __init__(self, parties):
        self.parties = parties

    def key(self, entry):
        party_vis = [1 if entry.parties.get(party) is not None else 0 for party in self.parties]
        return sum(party_vis), ''.join(map(str, reversed(party_vis)))


def split_header_name(name, max_length=None):
    """
    Splits a name in a header so that it is as short as possible while still being readable.
    """
    candidate = [name]
    for prefix in _COMMON_PREFIXES:
        if name.startswith(prefix):
            candidate = [prefix, name[len(prefix):]]
            break

    if max_length is not None and any(len(line) > max_length for line in candidate):
        # this is still a little long; try slicing on all uppercase letters
        split_half_index = 1 if len(candidate) >= 1 else 0

        substitution = candidate[0:split_half_index]
        if split_half_index < len(candidate):
            next_upper = re.match('[A-Z]', candidate[split_half_index])
            if next_upper is not None:
                idx = next_upper.start(0)
                if idx > 0:
                    substitution.append(candidate[split_half_index][0:idx])
                for line in candidate[split_half_index:]:
                    substitution.extend(re.findall('[A-Z][^A-Z]*', line))
        return substitution

    return candidate


class _TemplateEntryRenderer:
    """
    A template-specific renderer.
    """

    def __init__(self, template: _TemplateKey, parties):
        self.max_widths = {}
        if template.data_type is not None:
            self.headers = [_Header(name, param, parties)
                            for name, param in template.data_type.as_args_list()]
            self.template_name = template.template_name
        else:
            self.headers = [_Header(".cdata", None, parties)]
            self.template_name = template.template_name

        self.headers.insert(0, _Header(".time", None, parties))
        self.headers.insert(0, _Header(".cid", None, parties))
        self.headers.insert(0, _Header(".party", None, parties, colsize=len(parties)))
        self.entry_count = 0

    def measure(self, entries):
        for entry in entries:
            self.entry_count += 1
            for header in self.headers:
                header.measure_cell(entry)

    def render_header(self, color, columns=None):
        """
        Return an iterable over header rows.
        """
        if self.entry_count == 1:
            template_header_row = '{!s} (1 contract)'.format(self.template_name)
        else:
            template_header_row = '{!s} ({!s} contracts)'.format(self.template_name, self.entry_count)

        if columns is not None and len(template_header_row) < (columns - 1):
            yield template_header_row + ' ' + ''.rjust(columns - len(template_header_row) - 1, '-')
        else:
            yield template_header_row

        header_row_height = max(len(header.header_lines) for header in self.headers)
        for i in range(header_row_height):
            yield ' '.join(header.header_cell(i, header_row_height) for header in self.headers)

    def render_entries(self, entries):
        """
        Return an iterable that renders entries in order of their visibility to parties.
        """
        for entry in entries:
            yield ' '.join(header.render_cell(entry) for header in self.headers)


class _Header:
    def __init__(self, name, param, parties, colsize=None):
        self.name = name

        if name == '.cid':
            self.header_lines = ['#cid']
            self._value_from_entry = lambda entry: entry.contract_id
        elif name == '.time':
            self.header_lines = ['#time']
            self._value_from_entry = lambda entry: entry.time
        elif name == '.party':
            self.header_lines = ['']
            self._value_from_entry = lambda entry: render_parties(parties, entry)
        elif name == '.cdata':
            self.header_lines = ['#cdata (metadata missing)']
            self._value_from_entry = lambda entry: entry.contract_args
        else:
            self.header_lines = split_header_name(name, 8 if hasattr(param, 'name') and param.name == 'Bool' else None)
            self._value_from_entry = lambda entry: entry.contract_args[name] if entry.contract_args is not None else None

        self.colsize = colsize if colsize is not None else max(len(header) for header in self.header_lines)

    def header_cell(self, index, count):
        offset = count - len(self.header_lines)
        actual_index = index - offset
        return (self.header_lines[actual_index] if actual_index >= 0 else '').ljust(self.colsize, ' ')

    def measure_cell(self, data):
        data_size = len(str(self._value_from_entry(data)))
        self.colsize = max(self.colsize, data_size)

    def render_cell(self, entry):
        return str(self._value_from_entry(entry)).ljust(self.colsize, ' ')

    def __repr__(self):
        return '<_Header(name={!r}, colsize={!r})>'.format(self.name, self.colsize)


def render_parties(all_parties, entry):
    return ''.join(_render_party_bool(entry.parties.get(party)) for party in all_parties)


def _render_party_bool(value):
    if value is not None:
        return 'C' if value else 'A'
    return ' '
