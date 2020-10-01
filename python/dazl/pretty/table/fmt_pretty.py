# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Pretty print format that orders templates by ID, and attempts to render a more compact
representation.
"""

import re

from collections import defaultdict
from typing import Iterable, Mapping, Sequence, AbstractSet, Callable

from .model import Formatter, RowBuilder
from ...damlast.daml_lf_1 import TypeConName
from ...model.core import Party
from ...model.types_store import PackageStore

__all__ = ['PrettyFormatter']

BOX_B3 = '|'
BOX_C4 = '-'
BOX_DA = '+'

# a list of template parameter names that are long and make it tough to understand
# what is going on when written out as a single line
_COMMON_PREFIXES = ['invitedAs']


class PrettyFormatter(Formatter):
    def render(
            self,
            store: 'PackageStore',
            parties: 'AbstractSet[Party]',
            entries: 'Iterable[RowBuilder]'):
        sort = ByPartySort(parties)

        entries_by_template = group_by_name(entries)
        entry_count = sum(len(entries) for entries in entries_by_template.values())

        yield "{} total contracts over {} templates".format(entry_count, len(entries_by_template))
        for line in party_header(parties):
            yield line

        for name, entries in entries_by_template.items():
            # for each column for all entries in the data set, determine the most
            # compact representation here
            yield ''

            renderer = _TemplateEntryRenderer(store, name, parties)
            renderer.measure(entries)

            for line in renderer.render_header():
                yield line

            for line in renderer.render_entries(sorted(entries, key=sort.key)):
                yield line


def party_header(parties):
    parties = tuple(parties)
    party_count = len(parties)

    for index, party in enumerate(parties):
        ascii_art = (BOX_B3 * index) + BOX_DA + (BOX_C4 * (party_count - index - 1))
        yield f"{ascii_art} party '{party}'"
    yield '|' * party_count


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

    def __init__(self, store: 'PackageStore', name: 'TypeConName', parties: 'AbstractSet[Party]'):
        data_types = store.resolve_template_type(name)

        self.max_widths = {}
        if data_types:
            _, data_type = list(data_types.items())[0]
            self.headers = [_Header(name, param, parties)
                            for name, param in data_type.as_args_list()]
        else:
            self.headers = [_Header(".cdata", None, parties)]

        self.template_name = name
        self.headers.insert(0, _Header(".time", None, parties))
        self.headers.insert(0, _Header(".cid", None, parties))
        self.headers.insert(0, _Header(".party", None, parties, colsize=len(parties)))
        self.entry_count = 0

    def measure(self, entries):
        for entry in entries:
            self.entry_count += 1
            for header in self.headers:
                header.measure_cell(entry)

    def render_header(self):
        """
        Return an iterable over header rows.
        """
        if self.entry_count == 1:
            template_header_row = f'{self.template_name} (1 contract)'
        else:
            template_header_row = f'{self.template_name} ({self.entry_count} contracts)'

        # if columns is not None and len(template_header_row) < (columns - 1):
        #     yield template_header_row + ' ' + ''.rjust(columns - len(template_header_row) - 1, '-')
        # else:
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

    _value_from_entry: 'Callable[[RowBuilder], str]'

    def __init__(self, name, param, parties, colsize=None):
        self.name = name

        if name == '.cid':
            self.header_lines = ['#cid']
            self._value_from_entry = lambda entry: entry.cid
        elif name == '.time':
            self.header_lines = ['#time']
            self._value_from_entry = lambda entry: entry.time
        elif name == '.party':
            self.header_lines = ['']
            self._value_from_entry = lambda entry: render_parties(parties, entry)
        elif name == '.cdata':
            self.header_lines = ['#cdata (metadata missing)']
            self._value_from_entry = lambda entry: entry.cdata
        else:
            self.header_lines = split_header_name(name, 8 if hasattr(param, 'name') and param.name == 'Bool' else None)
            self._value_from_entry = lambda entry: entry.cdata[
                name] if entry.cdata is not None else None

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


def group_by_name(entries: 'Iterable[RowBuilder]') -> 'Mapping[TypeConName, Sequence[RowBuilder]]':
    """
    Organize the entries by their template name. The returned mapping where the keys are in sorted
    order.
    """
    entries_by_template = defaultdict(list)
    for entry in entries:
        entries_by_template[entry.cid.value_type].append(entry)

    return {name: entries_by_template[name] for name in sorted(entries_by_template)}
