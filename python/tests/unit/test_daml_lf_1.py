from dazl.damlast.daml_lf_1 import TypeConName, ModuleRef, PackageRef, DottedName


def test_type_con_name():
    a = PackageRef("deadbeef00000000000000000000000000000000000000000000000000000000")
    con1 = TypeConName(module=ModuleRef(a, DottedName(["Some", "Module"])), name=["Iou"])
    con2 = TypeConName(module=ModuleRef(a, DottedName(["Some", "Module"])), name=["Iou"])
    assert con1 == con2
    assert hash(con1) == hash(con2)
