# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dazl.damlast.daml_lf_1 import DottedName, ModuleRef, PackageRef, TypeConName


def test_type_con_name():
    a = PackageRef("deadbeef00000000000000000000000000000000000000000000000000000000")
    con1 = TypeConName(module=ModuleRef(a, DottedName(["Some", "Module"])), name=["Iou"])
    con2 = TypeConName(module=ModuleRef(a, DottedName(["Some", "Module"])), name=["Iou"])
    assert con1 == con2
    assert hash(con1) == hash(con2)
