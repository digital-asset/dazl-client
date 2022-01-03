# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json

from dazl.damlast.lookup import parse_type_con_name
from dazl.prim import ContractId, JSONEncoder


def test_contract_id():
    name = parse_type_con_name("0000deadbeef0000:MyMod:MyName")
    cid = ContractId(name, "#4:8")

    expected = '{"cid": "#4:8"}'
    actual = json.dumps({"cid": cid}, cls=JSONEncoder)
    assert expected == actual
