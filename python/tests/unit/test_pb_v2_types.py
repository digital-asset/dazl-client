# Copyright (c) 2017-2026 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Checks that the Daml-LF 2 parser reads types correctly, not just that it reads something.

Builtin types are checked against the LF 2.1 fixture `3.3.0/all-kinds-of-1.0.0_lf.dar`. The
encodings added in LF 2.2 (type application, interned kinds and expressions, package import
tables) are checked against small packages built here with the LF 2 protobuf classes.
"""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from dazl._gen.com.digitalasset.daml.lf.archive import daml_lf2_pb2 as pblf
from dazl.damlast import DarFile, daml_lf_1 as lf
from dazl.damlast.parse_factory.pb_v2 import ProtobufParser21
from dazl.damlast.util import package_ref
import pytest

ARCHIVES = Path(__file__).absolute().parent.parent.parent.parent / "_fixtures" / "archives"
ALL_KINDS_OF_LF21 = ARCHIVES / "3.3.0/all-kinds-of-1.0.0_lf.dar"
OTHER_PACKAGE = "ab" * 32


def type_name(t: lf.Type) -> object:
    """A type as plain tuples, e.g. `Optional Int` -> ("OPTIONAL", ("INT64",)),
    `Numeric 10` -> ("NUMERIC", 10), `MyPair Int` -> ("AllKindsOf:MyPair", ("INT64",))."""
    if t.prim is not None:
        return (t.prim.prim.name, *map(type_name, t.prim.args))
    if t.con is not None:
        module_and_name = str(t.con.tycon).split(":", 1)[1]  # drop the package ID
        return (module_and_name, *map(type_name, t.con.args))
    if t.var is not None:
        return (t.var.var, *map(type_name, t.var.args))
    if t.nat is not None:
        return t.nat
    raise AssertionError(f"unexpected type: {t._Sum_name}")


def record_fields(modules: Iterable[lf.Module], module: str, name: str) -> dict[str, object]:
    """The field types of a record, by field name."""
    for m in modules:
        for dt in m.data_types:
            if ".".join(m.name.segments) == module and ".".join(dt.name.segments) == name:
                assert dt.record is not None
                return {f.field: type_name(f.type) for f in dt.record.fields}
    raise AssertionError(f"{module}:{name} not found")


class PackageBuilder:
    """Builds a one-module Daml-LF 2 package (module `Mod`) the way LF 2.2+ encodes it: names
    go through the interned string tables and other packages through the import table."""

    def __init__(self) -> None:
        self.pb = pblf.Package()
        self.pb.package_imports.imported_packages.append(OTHER_PACKAGE)
        self.module = self.pb.modules.add(name_interned_dname=self.name("Mod"))

    def string(self, s: str) -> int:
        self.pb.interned_strings.append(s)
        return len(self.pb.interned_strings) - 1

    def name(self, dotted: str) -> int:
        segments = [self.string(s) for s in dotted.split(".")]
        self.pb.interned_dotted_names.add(segments_interned_str=segments)
        return len(self.pb.interned_dotted_names) - 1

    def tycon(self, module: str, name: str, imported: bool = False) -> pblf.TypeConId:
        tycon = pblf.TypeConId(name_interned_dname=self.name(name))
        tycon.module.module_name_interned_dname = self.name(module)
        if imported:
            tycon.module.package_id.package_import_id = 0  # OTHER_PACKAGE
        else:
            tycon.module.package_id.self_package_id.SetInParent()
        return tycon

    def con(self, module: str, name: str, imported: bool = False) -> pblf.Type:
        return pblf.Type(con=pblf.Type.Con(tycon=self.tycon(module, name, imported)))

    def builtin(self, name: str) -> pblf.Type:
        return pblf.Type(builtin=pblf.Type.Builtin(builtin=name))

    def var(self, name: str) -> pblf.Type:
        return pblf.Type(var=pblf.Type.Var(var_interned_str=self.string(name)))

    def apply(self, head: pblf.Type, *args: pblf.Type) -> pblf.Type:
        """`head arg1 arg2 ...` as nested binary applications: ((head arg1) arg2) ..."""
        for arg in args:
            head = pblf.Type(tapp=pblf.Type.TApp(lhs=head, rhs=arg))
        return head

    def record(self, name: str, **fields: pblf.Type) -> pblf.DefDataType:
        data_type = self.module.data_types.add(name_interned_dname=self.name(name))
        for field, type_ in fields.items():
            data_type.record.fields.add(field_interned_str=self.string(field), type=type_)
        return data_type

    def parse(self) -> list[lf.Module]:
        return list(ProtobufParser21(lf.PackageRef("00" * 32)).parse_Package(self.pb).modules)


@pytest.mark.parametrize("builtin", list(pblf.BuiltinType.DESCRIPTOR.values), ids=lambda v: v.name)
def test_builtin_type_maps_to_the_prim_type_of_the_same_name(builtin) -> None:
    parser = ProtobufParser21(lf.PackageRef("00" * 32))
    assert parser.parse_BuiltinType(builtin.number).name == builtin.name


def test_all_kinds_of_field_types() -> None:
    modules = [m for a in DarFile(ALL_KINDS_OF_LF21).archives() for m in a.package.modules]
    pair = "AllKindsOf:MyPair"
    assert record_fields(modules, "AllKindsOf", "OneOfEverything") == {
        "operator": ("PARTY",),
        "someBoolean": ("BOOL",),
        "someInteger": ("INT64",),
        "someDecimal": ("NUMERIC", 10),
        "someMaybe": ("OPTIONAL", ("INT64",)),
        "someMaybeNot": ("OPTIONAL", ("INT64",)),
        "someText": ("TEXT",),
        "someDate": ("DATE",),
        "someDatetime": ("TIMESTAMP",),
        "someSimpleList": ("LIST", ("INT64",)),
        "someSimplePair": (pair, ("INT64",)),
        "someNestedPair": (pair, (pair, ("INT64",))),
        "someUglyNesting": ("AllKindsOf:VPair", (pair, (pair, ("INT64",)))),
        "someMeasurement": ("NUMERIC", 10),
        "someEnum": ("AllKindsOf:Color",),
        "theUnit": ("UNIT",),
    }
    assert record_fields(modules, "AllKindsOf", "MappyContract") == {
        "operator": ("PARTY",),
        "value": ("TEXTMAP", ("TEXT",)),
    }


def test_type_application() -> None:
    pkg = PackageBuilder()
    sku = pkg.con("Mod", "SKU")
    pkg.record(
        "Cart",
        contents=pkg.apply(pkg.builtin("GENMAP"), sku, pkg.builtin("INT64")),
        note=pkg.apply(pkg.builtin("OPTIONAL"), pkg.builtin("TEXT")),
        pair=pkg.apply(pkg.con("Mod", "Pair"), sku, pkg.builtin("PARTY")),
    )

    assert record_fields(pkg.parse(), "Mod", "Cart") == {
        "contents": ("GENMAP", ("Mod:SKU",), ("INT64",)),
        "note": ("OPTIONAL", ("TEXT",)),
        "pair": ("Mod:Pair", ("Mod:SKU",), ("PARTY",)),
    }


def test_interned_kinds_and_type_variable_application() -> None:
    pkg = PackageBuilder()
    pkg.pb.interned_kinds.add().star.SetInParent()  # kind 0: *
    arrow = pkg.pb.interned_kinds.add().arrow  # kind 1: (kind 0) -> (kind 0)
    arrow.params.add(interned_kind=0)
    arrow.result.interned_kind = 0
    box = pkg.record(
        "Box", value=pkg.apply(pkg.var("f"), pkg.builtin("INT64"))
    )  # Box f = Box (f Int)
    box.params.add(var_interned_str=pkg.string("f"), kind=pblf.Kind(interned_kind=1))

    [module] = pkg.parse()
    [param] = module.data_types[0].params
    assert param.kind.arrow is not None  # f : * -> *
    assert [k.star is not None for k in param.kind.arrow.params] == [True]
    assert param.kind.arrow.result.star is not None
    assert record_fields([module], "Mod", "Box") == {"value": ("f", ("INT64",))}


def test_type_from_an_imported_package() -> None:
    pkg = PackageBuilder()
    pkg.record("Wallet", holding=pkg.con("Token", "Holding", imported=True))

    [wallet] = pkg.parse()[0].data_types
    assert wallet.record is not None
    [field] = wallet.record.fields
    assert field.type.con is not None
    assert type_name(field.type) == ("Token:Holding",)
    assert package_ref(field.type.con.tycon) == OTHER_PACKAGE


def test_interface_instance() -> None:
    pkg = PackageBuilder()
    template = pkg.module.templates.add(
        tycon_interned_dname=pkg.name("Asset"), param_interned_str=pkg.string("this")
    )
    instance = template.implements.add(interface=pkg.tycon("Token", "Holding", imported=True))
    instance.body.methods.add(
        method_interned_name=pkg.string("describe"),
        value=pblf.Expr(var_interned_str=pkg.string("this")),
    )
    # the view is an interned expression; its location is on the reference
    pkg.pb.interned_exprs.add(var_interned_str=pkg.string("this"))
    instance.body.view.interned_expr = 0
    instance.body.view.location.range.start_line = 7

    [parsed] = pkg.parse()[0].templates[0].implements
    assert type_name(lf.Type(con=lf.Type.Con(parsed.interface, ()))) == ("Token:Holding",)
    assert package_ref(parsed.interface) == OTHER_PACKAGE
    assert [m.method_name for m in parsed.body.methods] == ["describe"]
    assert parsed.body.view.var == "this"
    assert parsed.body.view.location.range.start_line == 7
