# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Formatting module for outputting captures.
"""

from typing import Iterable

from ...protocols.v0.json_ser_command import LedgerJSONEncoder
from ...util.tools import boundary_iter
from .model_capture import LedgerCapture


def format_error(error: str) -> Iterable[str]:
    encode = LedgerJSONEncoder().encode
    return encode(dict(errors=[error]))


def format_entries(capture: LedgerCapture, parties=None, entries=None, **kwargs) -> Iterable[str]:
    """
    Return a list of strings that, when taken together, constitute a JSON document that lists
    all of the entries of the ledger.

    :param capture:
        The contents to render.
    :param parties:
        The list of of parties.
    :param entries:
        The entries to render.
    :param kwargs:
        Additional parameters. Because all formatters have different arguments, these extra
        unknown parameters are ignored.
    """
    encode = LedgerJSONEncoder().encode

    yield "{{ \"parties\": {},".format(encode(parties))
    yield "  \"contracts\": ["

    for is_last, entry in boundary_iter(entries):
        party_list = sorted(entry.parties.keys())

        yield '  {{ "contract_id": "{}",'.format(entry.contract_id)
        yield '    "template": {},'.format(encode(entry.template_id.full_name))
        yield '    "parties": {},'.format(encode(party_list))
        yield '    "arguments": {} }}{}'.format(encode(entry.contract_args), '' if is_last else ',')

    yield "  ] }"
