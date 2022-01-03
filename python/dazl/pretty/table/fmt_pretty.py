# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Pretty print format that orders templates by ID, and attempts to render a more compact
representation.
"""

from collections import defaultdict
from typing import AbstractSet, Generator, Iterable, Mapping, Sequence

from ... import LOG
from ...damlast.daml_lf_1 import Type, TypeConName
from ...damlast.daml_types import con
from ...damlast.protocols import SymbolLookup
from ...prim import Party
from ...values import ArrayStringMapper, Context
from .model import Formatter, RowBuilder

__all__ = ["PrettyFormatter"]

BOX_B3 = "|"
BOX_C4 = "-"
BOX_DA = "+"


class PrettyFormatter(Formatter):
    def render(
        self, lookup: "SymbolLookup", parties: "AbstractSet[Party]", entries: "Iterable[RowBuilder]"
    ):
        sort = ByPartySort(parties)

        col_spacer = "  "

        entries_by_template = group_by_name(entries)
        entry_count = sum(len(entries) for entries in entries_by_template.values())

        yield "{} total contracts over {} templates".format(entry_count, len(entries_by_template))
        for line in party_header(parties):
            yield line

        for name, entries in entries_by_template.items():
            # for each column for all entries in the data set, determine the most
            # compact representation here
            yield ""

            tt = con(name)
            context = Context(ArrayStringMapper(), lookup)
            header_row = ["", "#cid", *(expand_record_field_names(context, Type.Con(name, ())))]

            with LOG.debug_timed("Render entries as strings"):
                orig_rows = [
                    (
                        sort.key(entry),
                        [
                            render_parties(parties, entry),
                            str(entry.cid),
                            *context.convert(tt, entry.cdata),
                        ],
                    )
                    for entry in entries
                ]

            with LOG.debug_timed("Sort rows"):
                orig_rows.sort(key=lambda val: val[0])
                rows = [row for _, row in orig_rows]
                rows.insert(0, header_row)

            with LOG.debug_timed("Measure entry sizes"):
                cell_sizes = [0] * len(rows[0])
                for row in rows:
                    for i, cell in enumerate(row):
                        cell_size = len(cell)
                        if cell_sizes[i] < cell_size:
                            cell_sizes[i] = cell_size

            with LOG.debug_timed("Render rows"):
                header_len = sum(cell_sizes) + (len(cell_sizes) - 1) * len(col_spacer)
                header = f"{name} ({contract_count(len(entries))}) "

                yield header + "-" * max(3, header_len - len(header))
                for row in rows:
                    yield col_spacer.join(
                        cell.ljust(cell_size) for cell_size, cell in zip(cell_sizes, row)
                    )


def contract_count(c: int) -> str:
    if c == 1:
        return "1 contract"
    else:
        return f"{c} contracts"


def expand_record_field_names(
    context: "Context", con: "Type.Con", path: "Sequence[str]" = ()
) -> "Generator[str, None, None]":
    """
    From a starting :class:`Type.Con`, return a string list of field names, additionally expanding
    sub-record fields.

    :param context:
        A context to use to perform type evaluation.
    :param con:
    :param path:
    :return:
    """
    dt = context.resolve_data_type(con)
    if dt.record is not None:
        for field in dt.record.fields:
            subpath = (*path, field.field)
            if field.type.con is not None:
                child_fields = list(expand_record_field_names(context, field.type.con, subpath))
                if child_fields:
                    yield from child_fields
                else:
                    yield ".".join(subpath)
            else:
                yield ".".join(subpath)


def party_header(parties):
    parties = tuple(parties)
    party_count = len(parties)

    for index, party in enumerate(parties):
        ascii_art = (BOX_B3 * index) + BOX_DA + (BOX_C4 * (party_count - index - 1))
        yield f"{ascii_art} party '{party}'"
    yield "|" * party_count


class ByPartySort:
    def __init__(self, parties):
        self.parties = parties

    def key(self, entry):
        party_vis = [1 if entry.parties.get(party) is not None else 0 for party in self.parties]
        return sum(party_vis), "".join(map(str, reversed(party_vis)))


def render_parties(all_parties, entry):
    return "".join(_render_party_bool(entry.parties.get(party)) for party in all_parties)


def _render_party_bool(value):
    if value is not None:
        return "C" if value else "A"
    return " "


def group_by_name(entries: "Iterable[RowBuilder]") -> "Mapping[TypeConName, Sequence[RowBuilder]]":
    """
    Organize the entries by their template name. The returned mapping where the keys are in sorted
    order.
    """
    entries_by_template = defaultdict(list)
    for entry in entries:
        entries_by_template[entry.cid.value_type].append(entry)

    return {name: entries_by_template[name] for name in sorted(entries_by_template)}
