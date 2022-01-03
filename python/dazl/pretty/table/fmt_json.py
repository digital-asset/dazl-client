# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Formatting module for outputting captures.
"""

import json
from typing import AbstractSet, Iterable

from ...damlast.daml_types import con
from ...damlast.protocols import SymbolLookup
from ...prim import Party
from ...util.tools import boundary_iter
from ...values import Context, JsonEncoder
from .model import Formatter, RowBuilder


class JsonFormatter(Formatter):
    def render(
        self, lookup: "SymbolLookup", parties: "AbstractSet[Party]", entries: "Iterable[RowBuilder]"
    ):
        """
        Return a list of strings that, when taken together, constitute a JSON document that lists
        all of the entries of the ledger.

        :param lookup:
            The contents to render.
        :param parties:
            The list of of parties.
        :param entries:
            The entries to render.
        """
        context = Context(JsonEncoder(), lookup)

        party_list = sorted(parties)

        yield '{{ "parties": {},'.format(json.dumps(party_list))
        yield '  "contracts": ['

        for is_last, entry in boundary_iter(entries):
            cid = entry.cid
            yield f'  {{ "contract_id": "{cid.value}",'
            yield f'    "template": {json.dumps(str(cid.value_type))},'
            yield f'    "parties": {json.dumps(party_list)},'
            yield f'    "arguments": {json.dumps(context.convert(con(cid.value_type), entry.cdata))} }}' + (
                "" if is_last else ","
            )

        yield "  ] }"
