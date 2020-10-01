# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Formatting module for outputting captures.
"""

from typing import Iterable, AbstractSet

from .model import Formatter, TableBuilder
from ...model.core import Party
from ...model.types_store import PackageStore
from ...protocols.v0.json_ser_command import LedgerJSONEncoder
from ...util.tools import boundary_iter


class JsonFormatter(Formatter):

    def render(
            self,
            store: 'PackageStore',
            parties: 'AbstractSet[Party]',
            entries: 'Iterable[TableBuilder]'):
        """
        Return a list of strings that, when taken together, constitute a JSON document that lists
        all of the entries of the ledger.

        :param store:
            The contents to render.
        :param parties:
            The list of of parties.
        :param entries:
            The entries to render.
        """
        encode = LedgerJSONEncoder().encode

        party_list = sorted(parties)

        yield "{{ \"parties\": {},".format(encode(party_list))
        yield "  \"contracts\": ["

        for is_last, entry in boundary_iter(party_list):
            yield '  {{ "contract_id": "{}",'.format(entry.contract_id)
            yield '    "template": {},'.format(encode(entry.contract_id.template_id))
            yield '    "parties": {},'.format(encode(party_list))
            yield '    "arguments": {} }}{}'.format(encode(entry.contract_args), '' if is_last else ',')

        yield "  ] }"
