# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl import Command, ContractId, CreateCommand
from dazl.damlast.lookup import parse_type_con_name

template_id_str = "deadbeef:DeadBeef:DeadBeef"
template_id = parse_type_con_name(template_id_str)
cid = ContractId(template_id, "#0:0")
choice = "Cook"
payload = {"operator": "beef", "weight": "10kg"}
key = {"operator": "beef"}


def test_isinstance() -> None:
    cmd = CreateCommand(template_id, payload)

    # we expect isinstance to succeed at runtime, even though mypy fails to
    # typecheck it
    assert isinstance(cmd, Command)  # type: ignore
