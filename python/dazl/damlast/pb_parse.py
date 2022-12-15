# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import sys
from typing import List, Optional, Sequence

from . import daml_lf_1 as lf
from .._gen.com.daml.daml_lf_1_15 import daml_lf_1_pb2 as pblf

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ["ProtobufParser"]

# TODO: Figure out a way to define these literals in daml_lf_1_pb2.pyi where they belong
# fmt: off
PrimCon = Literal[0, 1, 2]
PrimType = Literal[0, 1, 2, 3, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
PrimLit_RoundingMode = Literal[0, 1, 2, 3, 4, 5, 6, 7]
BuiltinFunction = Literal[0, 1, 2, 3, 6, 107, 108, 109, 110, 111, 121, 122, 7, 8, 9, 10, 11, 12, 20, 21, 96, 97, 98, 99, 100, 101, 124, 125, 126, 127, 128, 129, 130, 23, 24, 25, 147, 33, 34, 112, 36, 37, 67, 89, 39, 40, 113, 42, 43, 68, 90, 45, 46, 114, 48, 49, 69, 91, 51, 52, 115, 54, 55, 70, 92, 57, 58, 116, 60, 61, 71, 63, 94, 95, 103, 104, 117, 136, 93, 72, 73, 74, 75, 76, 77, 118, 119, 78, 79, 80, 120, 81, 82, 83, 84, 85, 86, 87, 123, 131, 132, 133, 134, 135, 88, 102, 105, 106, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146]

# fmt: on


# noinspection PyPep8Naming,PyMethodMayBeStatic
class ProtobufParser:
    def __init__(self, current_package: lf.PackageRef) -> None:
        self.current_package = current_package
        self.current_module = None  # type: Optional[lf.ModuleRef]
        self.interned_strings = []  # type: List[str]
        self.interned_dotted_names = []  # type: List[Sequence[str]]
        self.interned_types = []  # type: List[lf.Type]

    # noinspection PyUnusedLocal
    def parse_Unit(self, pb: pblf.Unit) -> lf.Unit:
        return lf.UNIT

    def parse_ModuleRef(self, pb: pblf.ModuleRef) -> Optional[lf.ModuleRef]:
        sum_name = pb.package_ref.WhichOneof("Sum")
        if sum_name is None:
            return None

        module_name = self._resolve_dotted_name(pb.module_name_dname, pb.module_name_interned_dname)
        if sum_name == "self":
            return lf.ModuleRef(self.current_package, module_name)
        elif sum_name == "package_id_str":
            return lf.ModuleRef(lf.PackageRef(pb.package_ref.package_id_str), module_name)
        elif sum_name == "package_id_interned_str":
            return lf.ModuleRef(
                lf.PackageRef(self.interned_strings[pb.package_ref.package_id_interned_str]),
                module_name,
            )
        else:
            raise ValueError(f"unknown sum type value: {sum_name!r}")

    def parse_TypeConName(self, pb: pblf.TypeConName) -> lf.TypeConName:
        module_ref = self.parse_ModuleRef(pb.module)
        if module_ref is None:
            raise ValueError("missing a valid ModuleRef in a TypeConName definition")
        return lf.TypeConName(
            module_ref,
            self._resolve_dotted_name(pb.name_dname, pb.name_interned_dname).segments,
        )

    def parse_TypeSynName(self, pb: pblf.TypeSynName) -> lf.TypeSynName:
        module_ref = self.parse_ModuleRef(pb.module)
        if module_ref is None:
            raise ValueError("missing a valid ModuleRef in a TypeSynName definition")
        return lf.TypeSynName(
            module_ref,
            self._resolve_dotted_name(pb.name_dname, pb.name_interned_dname).segments,
        )

    def parse_DottedName(self, pb: pblf.DottedName) -> lf.DottedName:
        return lf.DottedName(segments=self._resolve_string_seq(pb.segments, None))

    def parse_ValName(self, pb: pblf.ValName) -> lf.ValName:
        module_ref = self.parse_ModuleRef(pb.module)
        if module_ref is None:
            raise ValueError("missing a valid ModuleRef in a ValName definition")
        return lf.ValName(
            module_ref,
            self._resolve_string_seq(pb.name_dname, pb.name_interned_dname),
        )

    def parse_FieldWithType(self, pb: pblf.FieldWithType) -> lf.FieldWithType:
        """A field definition in a record or a variant associated with a type."""
        return lf.FieldWithType(
            self._resolve_string(pb.field_str, pb.field_interned_str), self.parse_Type(pb.type)
        )

    def parse_VarWithType(self, pb: pblf.VarWithType) -> lf.VarWithType:
        """Binder associated with a type."""
        return lf.VarWithType(
            self._resolve_string(pb.var_str, pb.var_interned_str), self.parse_Type(pb.type)
        )

    def parse_TypeVarWithKind(self, pb: pblf.TypeVarWithKind) -> lf.TypeVarWithKind:
        return lf.TypeVarWithKind(
            self._resolve_string(pb.var_str, pb.var_interned_str), self.parse_Kind(pb.kind)
        )

    def parse_FieldWithExpr(self, pb: pblf.FieldWithExpr) -> lf.FieldWithExpr:
        return lf.FieldWithExpr(
            self._resolve_string(pb.field_str, pb.field_interned_str), self.parse_Expr(pb.expr)
        )

    def parse_Binding(self, pb: pblf.Binding) -> lf.Binding:
        return lf.Binding(self.parse_VarWithType(pb.binder), self.parse_Expr(pb.bound))

    def parse_Kind(self, pb: pblf.Kind) -> lf.Kind:
        sum_name = pb.WhichOneof("Sum")
        if sum_name == "star":
            return lf.Kind(star=self.parse_Unit(pb.star))
        elif sum_name == "arrow":
            return lf.Kind(arrow=self.parse_Kind_Arrow(pb.arrow))
        elif sum_name == "nat":
            return lf.Kind(nat=self.parse_Unit(pb.nat))
        else:
            raise ValueError(f"unknown sum type value: {sum_name!r}")

    def parse_Kind_Arrow(self, pb: pblf.Kind.Arrow) -> lf.Kind.Arrow:
        return lf.Kind.Arrow(
            tuple(self.parse_Kind(param) for param in pb.params), self.parse_Kind(pb.result)
        )

    def parse_PrimType(self, pb: PrimType) -> lf.PrimType:
        return lf.PrimType(pb)

    def parse_Type(self, pb: pblf.Type) -> lf.Type:
        sum_name = pb.WhichOneof("Sum")
        if sum_name == "var":
            return self.parse_Type_Var(pb.var)
        elif sum_name == "con":
            return self.parse_Type_Con(pb.con)
        elif sum_name == "prim":
            return lf.Type(prim=self.parse_Type_Prim(pb.prim))
        elif sum_name == "forall":
            return lf.Type(forall=self.parse_Type_Forall(pb.forall))
        elif sum_name == "struct":
            return lf.Type(struct=self.parse_Type_Struct(pb.struct))
        elif sum_name == "nat":
            return lf.Type(nat=pb.nat)
        elif sum_name == "syn":
            return lf.Type(syn=self.parse_Type_Syn(pb.syn))
        elif sum_name == "interned":
            return self.interned_types[pb.interned]
        else:
            raise ValueError(f"unknown sum type value: {sum_name!r}")

    def parse_Type_Var(self, pb: pblf.Type.Var) -> lf.Type:
        return lf.Type(
            var=lf.Type.Var(
                self._resolve_string(pb.var_str, pb.var_interned_str),
                tuple(self.parse_Type(arg) for arg in pb.args),
            )
        )

    def parse_Type_Con(self, pb: pblf.Type.Con) -> lf.Type:
        """
        Create a :class:`Type` instance (but may produce something slightly different than the AST
        due to ``Map``/``Optional`` type rewriting).
        """
        tycon = self.parse_TypeConName(pb.tycon)
        args = tuple(self.parse_Type(arg) for arg in pb.args)
        return lf.Type(con=lf.Type.Con(tycon, args))

    def parse_Type_Prim(self, pb: pblf.Type.Prim) -> lf.Type.Prim:
        return lf.Type.Prim(
            self.parse_PrimType(pb.prim), tuple(self.parse_Type(arg) for arg in pb.args)
        )

    def parse_Type_Forall(self, pb: pblf.Type.Forall) -> lf.Type.Forall:
        return lf.Type.Forall(
            tuple(self.parse_TypeVarWithKind(var) for var in pb.vars), self.parse_Type(pb.body)
        )

    def parse_Type_Struct(self, pb: pblf.Type.Struct) -> lf.Type.Struct:
        return lf.Type.Struct(tuple(self.parse_FieldWithType(field) for field in pb.fields))

    def parse_Type_Syn(self, pb: pblf.Type.Syn) -> lf.Type.Syn:
        return lf.Type.Syn(
            tysyn=self.parse_TypeSynName(pb.tysyn),
            args=tuple(self.parse_Type(arg) for arg in pb.args),
        )

    def parse_PrimCon(self, pb: PrimCon) -> lf.PrimCon:
        if pb == 0:
            return lf.PrimCon.CON_UNIT
        elif pb == 1:
            return lf.PrimCon.CON_FALSE
        elif pb == 2:
            return lf.PrimCon.CON_TRUE
        else:
            raise ValueError(f"unknown enum value: {pb!r}")

    def parse_BuiltinFunction(self, pb: BuiltinFunction) -> lf.BuiltinFunction:
        return lf.BuiltinFunction(pb)

    def parse_PrimLit(self, pb: pblf.PrimLit) -> lf.PrimLit:
        sum_name = pb.WhichOneof("Sum")
        if sum_name == "int64":
            return lf.PrimLit(int64=pb.int64)
        elif sum_name == "decimal_str":
            return lf.PrimLit(decimal=pb.decimal_str)
        elif sum_name == "numeric_interned_str":
            return lf.PrimLit(numeric=self.interned_strings[pb.numeric_interned_str])
        elif sum_name == "text_str":
            return lf.PrimLit(text=pb.text_str)
        elif sum_name == "text_interned_str":
            return lf.PrimLit(text=self.interned_strings[pb.text_interned_str])
        elif sum_name == "timestamp":
            return lf.PrimLit(timestamp=pb.timestamp)
        elif sum_name == "party_str":
            return lf.PrimLit(party=pb.party_str)
        elif sum_name == "party_interned_str":
            return lf.PrimLit(party=self.interned_strings[pb.party_interned_str])
        elif sum_name == "date":
            return lf.PrimLit(date=pb.date)
        elif sum_name == "rounding_mode":
            return lf.PrimLit(rounding_mode=self.parse_PrimLit_RoundingMode(pb.rounding_mode))
        else:
            raise ValueError(f"unknown Sum value: {pb!r}")

    def parse_PrimLit_RoundingMode(self, pb: PrimLit_RoundingMode) -> lf.PrimLit.RoundingMode:
        return lf.PrimLit.RoundingMode(pb)

    def parse_Expr(self, pb: pblf.Expr) -> lf.Expr:
        location = self.parse_Location(pb.location) if pb.HasField("location") else None

        sum_name = pb.WhichOneof("Sum")
        if sum_name == "var_str":
            return lf.Expr(var=pb.var_str, location=location)
        elif sum_name == "var_interned_str":
            return lf.Expr(var=self.interned_strings[pb.var_interned_str], location=location)
        elif sum_name == "val":
            return lf.Expr(val=self.parse_ValName(pb.val), location=location)
        elif sum_name == "builtin":
            return lf.Expr(builtin=self.parse_BuiltinFunction(pb.builtin), location=location)
        elif sum_name == "prim_con":
            return lf.Expr(prim_con=self.parse_PrimCon(pb.prim_con), location=location)
        elif sum_name == "prim_lit":
            return lf.Expr(prim_lit=self.parse_PrimLit(pb.prim_lit), location=location)
        elif sum_name == "rec_con":
            return lf.Expr(rec_con=self.parse_Expr_RecCon(pb.rec_con), location=location)
        elif sum_name == "rec_proj":
            return lf.Expr(rec_proj=self.parse_Expr_RecProj(pb.rec_proj), location=location)
        elif sum_name == "rec_upd":
            return lf.Expr(rec_upd=self.parse_Expr_RecUpd(pb.rec_upd), location=location)
        elif sum_name == "variant_con":
            return lf.Expr(
                variant_con=self.parse_Expr_VariantCon(pb.variant_con), location=location
            )
        elif sum_name == "enum_con":
            return lf.Expr(enum_con=self.parse_Expr_EnumCon(pb.enum_con), location=location)
        elif sum_name == "struct_con":
            return lf.Expr(struct_con=self.parse_Expr_StructCon(pb.struct_con), location=location)
        elif sum_name == "struct_proj":
            return lf.Expr(
                struct_proj=self.parse_Expr_StructProj(pb.struct_proj), location=location
            )
        elif sum_name == "struct_upd":
            return lf.Expr(struct_upd=self.parse_Expr_StructUpd(pb.struct_upd), location=location)
        elif sum_name == "app":
            return lf.Expr(app=self.parse_Expr_App(pb.app), location=location)
        elif sum_name == "ty_app":
            return lf.Expr(ty_app=self.parse_Expr_TyApp(pb.ty_app), location=location)
        elif sum_name == "abs":
            return lf.Expr(abs=self.parse_Expr_Abs(pb.abs), location=location)
        elif sum_name == "ty_abs":
            return lf.Expr(ty_abs=self.parse_Expr_TyAbs(pb.ty_abs), location=location)
        elif sum_name == "case":
            return lf.Expr(case=self.parse_Case(pb.case), location=location)
        elif sum_name == "let":
            return lf.Expr(let=self.parse_Block(pb.let), location=location)
        elif sum_name == "nil":
            return lf.Expr(nil=self.parse_Expr_Nil(pb.nil), location=location)
        elif sum_name == "cons":
            return lf.Expr(cons=self.parse_Expr_Cons(pb.cons), location=location)
        elif sum_name == "update":
            return lf.Expr(update=self.parse_Update(pb.update), location=location)
        elif sum_name == "scenario":
            return lf.Expr(scenario=self.parse_Scenario(pb.scenario), location=location)
        elif sum_name == "optional_none":
            return lf.Expr(
                optional_none=self.parse_Expr_OptionalNone(pb.optional_none), location=location
            )
        elif sum_name == "optional_some":
            return lf.Expr(
                optional_some=self.parse_Expr_OptionalSome(pb.optional_some), location=location
            )
        elif sum_name == "to_any":
            return lf.Expr(to_any=self.parse_Expr_ToAny(pb.to_any), location=location)
        elif sum_name == "from_any":
            return lf.Expr(from_any=self.parse_Expr_FromAny(pb.from_any), location=location)
        elif sum_name == "type_rep":
            return lf.Expr(type_rep=self.parse_Type(pb.type_rep), location=location)
        elif sum_name == "to_any_exception":
            return lf.Expr(
                to_any_exception=self.parse_Expr_ToAnyException(pb.to_any_exception),
                location=location,
            )
        elif sum_name == "from_any_exception":
            return lf.Expr(
                from_any_exception=self.parse_Expr_FromAnyException(pb.from_any_exception),
                location=location,
            )
        elif sum_name == "throw":
            return lf.Expr(throw=self.parse_Expr_Throw(pb.throw), location=location)
        elif sum_name == "to_interface":
            return lf.Expr(
                to_interface=self.parse_Expr_ToInterface(pb.to_interface), location=location
            )
        elif sum_name == "from_interface":
            return lf.Expr(
                from_interface=self.parse_Expr_FromInterface(pb.from_interface), location=location
            )
        elif sum_name == "call_interface":
            return lf.Expr(
                call_interface=self.parse_Expr_CallInterface(pb.call_interface), location=location
            )
        elif sum_name == "signatory_interface":
            return lf.Expr(
                signatory_interface=self.parse_Expr_SignatoryInterface(pb.signatory_interface),
                location=location,
            )
        elif sum_name == "observer_interface":
            return lf.Expr(
                observer_interface=self.parse_Expr_ObserverInterface(pb.observer_interface),
                location=location,
            )
        elif sum_name == "view_interface":
            return lf.Expr(
                view_interface=self.parse_Expr_ViewInterface(pb.view_interface), location=location
            )
        elif sum_name == "unsafe_from_interface":
            return lf.Expr(
                unsafe_from_interface=self.parse_Expr_UnsafeFromInterface(pb.unsafe_from_interface),
                location=location,
            )
        elif sum_name == "interface_template_type_rep":
            return lf.Expr(
                interface_template_type_rep=self.parse_Expr_InterfaceTemplateTypeRep(
                    pb.interface_template_type_rep
                ),
                location=location,
            )
        elif sum_name == "to_required_interface":
            return lf.Expr(
                to_required_interface=self.parse_Expr_ToRequiredInterface(pb.to_required_interface),
                location=location,
            )
        elif sum_name == "from_required_interface":
            return lf.Expr(
                from_required_interface=self.parse_Expr_FromRequiredInterface(
                    pb.from_required_interface
                ),
                location=location,
            )
        elif sum_name == "unsafe_from_required_interface":
            return lf.Expr(
                unsafe_from_required_interface=self.parse_Expr_UnsafeFromRequiredInterface(
                    pb.unsafe_from_required_interface
                ),
                location=location,
            )
        elif sum_name == "experimental":
            return lf.Expr(
                experimental=self.parse_Expr_Experimental(pb.experimental), location=location
            )
        else:
            raise ValueError(f"Unknown type of Expr: {sum_name!r}")

    def parse_Expr_RecCon(self, pb: pblf.Expr.RecCon) -> lf.Expr.RecCon:
        return lf.Expr.RecCon(
            self.parse_Type_Con(pb.tycon).con,
            tuple(self.parse_FieldWithExpr(field) for field in pb.fields),
        )  # length > 0

    def parse_Expr_RecProj(self, pb: pblf.Expr.RecProj) -> lf.Expr.RecProj:
        return lf.Expr.RecProj(
            self.parse_Type_Con(pb.tycon).con,  # Always fully applied
            self._resolve_string(pb.field_str, pb.field_interned_str),
            self.parse_Expr(pb.record),
        )

    def parse_Expr_RecUpd(self, pb: pblf.Expr.RecUpd) -> lf.Expr.RecUpd:
        """Set ``field`` in ``record`` to ``update``."""
        return lf.Expr.RecUpd(
            self.parse_Type_Con(pb.tycon).con,
            self._resolve_string(pb.field_str, pb.field_interned_str),
            self.parse_Expr(pb.record),
            self.parse_Expr(pb.update),
        )

    def parse_Expr_VariantCon(self, pb: pblf.Expr.VariantCon) -> lf.Expr.VariantCon:
        return lf.Expr.VariantCon(
            self.parse_Type_Con(pb.tycon).con,  # Always fully applied
            self._resolve_string(pb.variant_con_str, pb.variant_con_interned_str),
            self.parse_Expr(pb.variant_arg),
        )

    def parse_Expr_StructCon(self, pb: pblf.Expr.StructCon) -> lf.Expr.StructCon:
        return lf.Expr.StructCon(
            tuple(self.parse_FieldWithExpr(field) for field in pb.fields)
        )  # length > 0

    def parse_Expr_EnumCon(self, pb: pblf.Expr.EnumCon) -> lf.Expr.EnumCon:
        return lf.Expr.EnumCon(
            self.parse_TypeConName(pb.tycon),
            self._resolve_string(pb.enum_con_str, pb.enum_con_interned_str),
        )

    def parse_Expr_StructProj(self, pb: pblf.Expr.StructProj) -> lf.Expr.StructProj:
        return lf.Expr.StructProj(
            self._resolve_string(pb.field_str, pb.field_interned_str), self.parse_Expr(pb.struct)
        )

    def parse_Expr_StructUpd(self, pb: pblf.Expr.StructUpd) -> lf.Expr.StructUpd:
        """Set ``field`` in ``tuple`` to ``update``."""
        return lf.Expr.StructUpd(
            self._resolve_string(pb.field_str, pb.field_interned_str),
            self.parse_Expr(pb.struct),
            self.parse_Expr(pb.update),
        )

    def parse_Expr_App(self, pb: pblf.Expr.App) -> lf.Expr.App:
        return lf.Expr.App(
            self.parse_Expr(pb.fun), tuple(self.parse_Expr(arg) for arg in pb.args)
        )  # length > 0

    def parse_Expr_TyApp(self, pb: pblf.Expr.TyApp) -> lf.Expr.TyApp:
        return lf.Expr.TyApp(
            self.parse_Expr(pb.expr), tuple(self.parse_Type(type) for type in pb.types)
        )  # length > 0

    def parse_Expr_Abs(self, pb: pblf.Expr.Abs) -> lf.Expr.Abs:
        return lf.Expr.Abs(
            tuple(self.parse_VarWithType(param) for param in pb.param),  # length > 0
            self.parse_Expr(pb.body),
        )

    def parse_Expr_TyAbs(self, pb: pblf.Expr.TyAbs) -> lf.Expr.TyAbs:
        return lf.Expr.TyAbs(
            tuple(self.parse_TypeVarWithKind(param) for param in pb.param),  # length > 0
            self.parse_Expr(pb.body),
        )

    def parse_Expr_Nil(self, pb: pblf.Expr.Nil) -> lf.Expr.Nil:
        return lf.Expr.Nil(self.parse_Type(pb.type))

    def parse_Expr_Cons(self, pb: pblf.Expr.Cons) -> lf.Expr.Cons:
        return lf.Expr.Cons(
            self.parse_Type(pb.type),
            tuple(self.parse_Expr(front) for front in pb.front),  # length > 0
            self.parse_Expr(pb.tail),
        )

    def parse_Expr_OptionalNone(self, pb: pblf.Expr.OptionalNone) -> lf.Expr.OptionalNone:
        return lf.Expr.OptionalNone(self.parse_Type(pb.type))

    def parse_Expr_OptionalSome(self, pb: pblf.Expr.OptionalSome) -> lf.Expr.OptionalSome:
        return lf.Expr.OptionalSome(self.parse_Type(pb.type), self.parse_Expr(pb.body))

    def parse_Expr_ToAny(self, pb: pblf.Expr.ToAny) -> lf.Expr.ToAny:
        return lf.Expr.ToAny(self.parse_Type(pb.type), self.parse_Expr(pb.expr))

    def parse_Expr_FromAny(self, pb: pblf.Expr.FromAny) -> lf.Expr.FromAny:
        return lf.Expr.FromAny(self.parse_Type(pb.type), self.parse_Expr(pb.expr))

    def parse_Expr_ToAnyException(self, pb: pblf.Expr.ToAnyException) -> lf.Expr.ToAnyException:
        return lf.Expr.ToAnyException(self.parse_Type(pb.type), self.parse_Expr(pb.expr))

    def parse_Expr_FromAnyException(
        self, pb: pblf.Expr.FromAnyException
    ) -> lf.Expr.FromAnyException:
        return lf.Expr.FromAnyException(self.parse_Type(pb.type), self.parse_Expr(pb.expr))

    def parse_Expr_Throw(self, pb: pblf.Expr.Throw) -> lf.Expr.Throw:
        return lf.Expr.Throw(
            return_type=self.parse_Type(pb.return_type),
            exception_type=self.parse_Type(pb.exception_type),
            exception_expr=self.parse_Expr(pb.exception_expr),
        )

    def parse_Expr_ToInterface(self, pb: pblf.Expr.ToInterface) -> lf.Expr.ToInterface:
        return lf.Expr.ToInterface(
            interface_type=self.parse_TypeConName(pb.interface_type),
            template_type=self.parse_TypeConName(pb.template_type),
            template_expr=self.parse_Expr(pb.template_expr),
        )

    def parse_Expr_FromInterface(self, pb: pblf.Expr.FromInterface) -> lf.Expr.FromInterface:
        return lf.Expr.FromInterface(
            interface_type=self.parse_TypeConName(pb.interface_type),
            template_type=self.parse_TypeConName(pb.template_type),
            interface_expr=self.parse_Expr(pb.interface_expr),
        )

    def parse_Expr_CallInterface(self, pb: pblf.Expr.CallInterface) -> lf.Expr.CallInterface:
        return lf.Expr.CallInterface(
            interface_type=self.parse_TypeConName(pb.interface_type),
            method_name=self.interned_strings[pb.method_interned_name],
            interface_expr=self.parse_Expr(pb.interface_expr),
        )

    def parse_Expr_SignatoryInterface(
        self, pb: pblf.Expr.SignatoryInterface
    ) -> lf.Expr.SignatoryInterface:
        return lf.Expr.SignatoryInterface(
            interface=self.parse_TypeConName(pb.interface),
            expr=self.parse_Expr(pb.expr),
        )

    def parse_Expr_ObserverInterface(
        self, pb: pblf.Expr.ObserverInterface
    ) -> lf.Expr.ObserverInterface:
        return lf.Expr.ObserverInterface(
            interface=self.parse_TypeConName(pb.interface),
            expr=self.parse_Expr(pb.expr),
        )

    def parse_Expr_ViewInterface(self, pb: pblf.Expr.ViewInterface) -> lf.Expr.ViewInterface:
        return lf.Expr.ViewInterface(
            interface=self.parse_TypeConName(pb.interface),
            expr=self.parse_Expr(pb.expr),
        )

    def parse_Expr_UnsafeFromInterface(
        self, pb: pblf.Expr.UnsafeFromInterface
    ) -> lf.Expr.UnsafeFromInterface:
        return lf.Expr.UnsafeFromInterface(
            interface_type=self.parse_TypeConName(pb.interface_type),
            template_type=self.parse_TypeConName(pb.template_type),
            contract_id_expr=self.parse_Expr(pb.contract_id_expr),
            interface_expr=self.parse_Expr(pb.interface_expr),
        )

    def parse_Expr_InterfaceTemplateTypeRep(
        self, pb: pblf.Expr.InterfaceTemplateTypeRep
    ) -> lf.Expr.InterfaceTemplateTypeRep:
        return lf.Expr.InterfaceTemplateTypeRep(
            interface=self.parse_TypeConName(pb.interface),
            expr=self.parse_Expr(pb.expr),
        )

    def parse_Expr_ToRequiredInterface(
        self, pb: pblf.Expr.ToRequiredInterface
    ) -> lf.Expr.ToRequiredInterface:
        return lf.Expr.ToRequiredInterface(
            required_interface=self.parse_TypeConName(pb.required_interface),
            requiring_interface=self.parse_TypeConName(pb.requiring_interface),
            expr=self.parse_Expr(pb.expr),
        )

    def parse_Expr_FromRequiredInterface(
        self, pb: pblf.Expr.FromRequiredInterface
    ) -> lf.Expr.FromRequiredInterface:
        return lf.Expr.FromRequiredInterface(
            required_interface=self.parse_TypeConName(pb.required_interface),
            requiring_interface=self.parse_TypeConName(pb.requiring_interface),
            expr=self.parse_Expr(pb.expr),
        )

    def parse_Expr_UnsafeFromRequiredInterface(
        self, pb: pblf.Expr.UnsafeFromRequiredInterface
    ) -> lf.Expr.UnsafeFromRequiredInterface:
        return lf.Expr.UnsafeFromRequiredInterface(
            required_interface=self.parse_TypeConName(pb.required_interface),
            requiring_interface=self.parse_TypeConName(pb.requiring_interface),
            contract_id_expr=self.parse_Expr(pb.contract_id_expr),
            interface_expr=self.parse_Expr(pb.interface_expr),
        )

    def parse_Expr_Experimental(self, pb: pblf.Expr.Experimental) -> lf.Expr.Experimental:
        return lf.Expr.Experimental(name=pb.name, type=self.parse_Type(pb.type))

    def parse_CaseAlt(self, pb: pblf.CaseAlt) -> lf.CaseAlt:
        body = self.parse_Expr(pb.body)
        sum_name = pb.WhichOneof("Sum")
        if sum_name == "default":
            return lf.CaseAlt(default=self.parse_Unit(pb.default), body=body)
        elif sum_name == "variant":
            return lf.CaseAlt(variant=self.parse_CaseAlt_Variant(pb.variant), body=body)
        elif sum_name == "prim_con":
            return lf.CaseAlt(prim_con=self.parse_PrimCon(pb.prim_con), body=body)
        elif sum_name == "nil":
            return lf.CaseAlt(nil=self.parse_Unit(pb.nil), body=body)
        elif sum_name == "cons":
            return lf.CaseAlt(cons=self.parse_CaseAlt_Cons(pb.cons), body=body)
        elif sum_name == "optional_none":
            return lf.CaseAlt(optional_none=self.parse_Unit(pb.optional_none), body=body)
        elif sum_name == "optional_some":
            return lf.CaseAlt(
                optional_some=self.parse_CaseAlt_OptionalSome(pb.optional_some), body=body
            )
        elif sum_name == "enum":
            return lf.CaseAlt(enum=self.parse_CaseAlt_Enum(pb.enum), body=body)
        else:
            raise ValueError(f"unknown Sum value: {sum_name!r}")

    def parse_CaseAlt_Variant(self, pb: pblf.CaseAlt.Variant) -> lf.CaseAlt.Variant:
        return lf.CaseAlt.Variant(
            self.parse_TypeConName(pb.con),
            self._resolve_string(pb.variant_str, pb.variant_interned_str),
            self._resolve_string(pb.binder_str, pb.binder_interned_str),
        )

    def parse_CaseAlt_Enum(self, pb: pblf.CaseAlt.Enum) -> lf.CaseAlt.Enum:
        return lf.CaseAlt.Enum(
            self.parse_TypeConName(pb.con),
            self._resolve_string(pb.constructor_str, pb.constructor_interned_str),
        )

    def parse_CaseAlt_Cons(self, pb: pblf.CaseAlt.Cons) -> lf.CaseAlt.Cons:
        return lf.CaseAlt.Cons(
            self._resolve_string(pb.var_head_str, pb.var_head_interned_str),
            self._resolve_string(pb.var_tail_str, pb.var_tail_interned_str),
        )

    def parse_CaseAlt_OptionalSome(self, pb: pblf.CaseAlt.OptionalSome) -> lf.CaseAlt.OptionalSome:
        return lf.CaseAlt.OptionalSome(
            self._resolve_string(pb.var_body_str, pb.var_body_interned_str)
        )

    def parse_Case(self, pb: pblf.Case) -> lf.Case:
        return lf.Case(self.parse_Expr(pb.scrut), tuple(self.parse_CaseAlt(alt) for alt in pb.alts))

    def parse_Block(self, pb: pblf.Block) -> lf.Block:
        return lf.Block(
            tuple(self.parse_Binding(binding) for binding in pb.bindings), self.parse_Expr(pb.body)
        )

    def parse_Pure(self, pb: pblf.Pure) -> lf.Pure:
        return lf.Pure(type=self.parse_Type(pb.type), expr=self.parse_Expr(pb.expr))

    def parse_Update(self, pb: pblf.Update) -> lf.Update:
        sum_name = pb.WhichOneof("Sum")
        if sum_name == "pure":
            return lf.Update(pure=self.parse_Pure(pb.pure))
        elif sum_name == "block":
            return lf.Update(block=self.parse_Block(pb.block))
        elif sum_name == "create":
            return lf.Update(create=self.parse_Update_Create(pb.create))
        elif sum_name == "exercise":
            return lf.Update(exercise=self.parse_Update_Exercise(pb.exercise))
        elif sum_name == "exercise_by_key":
            return lf.Update(exercise_by_key=self.parse_Update_ExerciseByKey(pb.exercise_by_key))
        elif sum_name == "fetch":
            return lf.Update(fetch=self.parse_Update_Fetch(pb.fetch))
        elif sum_name == "get_time":
            return lf.Update(get_time=self.parse_Unit(pb.get_time))
        elif sum_name == "lookup_by_key":
            return lf.Update(lookup_by_key=self.parse_Update_RetrieveByKey(pb.lookup_by_key))
        elif sum_name == "fetch_by_key":
            return lf.Update(fetch_by_key=self.parse_Update_RetrieveByKey(pb.fetch_by_key))
        elif sum_name == "embed_expr":
            return lf.Update(embed_expr=self.parse_Update_EmbedExpr(pb.embed_expr))
        elif sum_name == "try_catch":
            return lf.Update(try_catch=self.parse_Update_TryCatch(pb.try_catch))
        elif sum_name == "create_interface":
            return lf.Update(
                create_interface=self.parse_Update_CreateInterface(pb.create_interface)
            )
        elif sum_name == "exercise_interface":
            return lf.Update(
                exercise_interface=self.parse_Update_ExerciseInterface(pb.exercise_interface)
            )
        elif sum_name == "fetch_interface":
            return lf.Update(fetch_interface=self.parse_Update_FetchInterface(pb.fetch_interface))
        else:
            raise ValueError(f"unknown Sum value: {sum_name!r}")

    def parse_Update_Create(self, pb: pblf.Update.Create) -> lf.Update.Create:
        return lf.Update.Create(
            template=self.parse_TypeConName(pb.template), expr=self.parse_Expr(pb.expr)
        )

    def parse_Update_Exercise(self, pb: pblf.Update.Exercise) -> lf.Update.Exercise:
        return lf.Update.Exercise(
            template=self.parse_TypeConName(pb.template),
            choice=self._resolve_string(pb.choice_str, pb.choice_interned_str),
            cid=self.parse_Expr(pb.cid),
            arg=self.parse_Expr(pb.arg),
        )

    def parse_Update_ExerciseByKey(self, pb: pblf.Update.ExerciseByKey) -> lf.Update.ExerciseByKey:
        return lf.Update.ExerciseByKey(
            template=self.parse_TypeConName(pb.template),
            choice=self.interned_strings[pb.choice_interned_str],
            key=self.parse_Expr(pb.key),
            arg=self.parse_Expr(pb.arg),
        )

    def parse_Update_Fetch(self, pb: pblf.Update.Fetch) -> lf.Update.Fetch:
        return lf.Update.Fetch(
            template=self.parse_TypeConName(pb.template), cid=self.parse_Expr(pb.cid)
        )

    def parse_Update_EmbedExpr(self, pb: pblf.Update.EmbedExpr) -> lf.Update.EmbedExpr:
        return lf.Update.EmbedExpr(type=self.parse_Type(pb.type), body=self.parse_Expr(pb.body))

    def parse_Update_RetrieveByKey(self, pb: pblf.Update.RetrieveByKey) -> lf.Update.RetrieveByKey:
        return lf.Update.RetrieveByKey(
            template=self.parse_TypeConName(pb.template), key=self.parse_Expr(pb.key)
        )

    def parse_Update_TryCatch(self, pb: pblf.Update.TryCatch) -> lf.Update.TryCatch:
        return lf.Update.TryCatch(
            return_type=self.parse_Type(pb.return_type),
            try_expr=self.parse_Expr(pb.try_expr),
            var=self.interned_strings[pb.var_interned_str],
            catch_expr=self.parse_Expr(pb.catch_expr),
        )

    def parse_Update_CreateInterface(
        self, pb: pblf.Update.CreateInterface
    ) -> lf.Update.CreateInterface:
        return lf.Update.CreateInterface(
            interface=self.parse_TypeConName(pb.interface),
            expr=self.parse_Expr(pb.expr),
        )

    def parse_Update_ExerciseInterface(
        self, pb: pblf.Update.ExerciseInterface
    ) -> lf.Update.ExerciseInterface:
        return lf.Update.ExerciseInterface(
            interface=self.parse_TypeConName(pb.interface),
            cid=self.parse_Expr(pb.cid),
            arg=self.parse_Expr(pb.arg),
            guard=self.parse_Expr(pb.guard),
        )

    def parse_Update_FetchInterface(
        self, pb: pblf.Update.FetchInterface
    ) -> lf.Update.FetchInterface:
        return lf.Update.FetchInterface(
            interface=self.parse_TypeConName(pb.interface),
            cid=self.parse_Expr(pb.cid),
        )

    def parse_Scenario(self, pb: pblf.Scenario) -> lf.Scenario:
        sum_name = pb.WhichOneof("Sum")
        if sum_name == "pure":
            return lf.Scenario(pure=self.parse_Pure(pb.pure))
        elif sum_name == "block":
            return lf.Scenario(block=self.parse_Block(pb.block))
        elif sum_name == "commit":
            return lf.Scenario(commit=self.parse_Scenario_Commit(pb.commit))
        elif sum_name == "mustFailAt":
            return lf.Scenario(must_fail_at=self.parse_Scenario_Commit(pb.mustFailAt))
        elif sum_name == "pass":
            return lf.Scenario(pass_=self.parse_Expr(getattr(pb, "pass")))
        elif sum_name == "get_time":
            return lf.Scenario(get_time=self.parse_Unit(pb.get_time))
        elif sum_name == "get_party":
            return lf.Scenario(get_party=self.parse_Expr(pb.get_party))
        elif sum_name == "embed_expr":
            return lf.Scenario(embed_expr=self.parse_Scenario_EmbedExpr(pb.embed_expr))
        else:
            raise ValueError("unknown Sum value")

    def parse_Scenario_Commit(self, pb: pblf.Scenario.Commit) -> lf.Scenario.Commit:
        return lf.Scenario.Commit(
            party=self.parse_Expr(pb.party),
            expr=self.parse_Expr(pb.expr),
            ret_type=self.parse_Type(pb.ret_type),
        )

    def parse_Scenario_EmbedExpr(self, pb: pblf.Scenario.EmbedExpr) -> lf.Scenario.EmbedExpr:
        return lf.Scenario.EmbedExpr(type=self.parse_Type(pb.type), body=self.parse_Expr(pb.body))

    def parse_Location(self, pb: pblf.Location) -> lf.Location:
        module_ref = self.parse_ModuleRef(pb.module)
        if module_ref is None:
            module_ref = self.current_module
        if module_ref is None:
            # This is probably a programming mistake, since nowhere in the Daml-LF protobuf does
            # a Location occur outside of a Module
            raise ValueError(
                "cannot parse a Location object without a ModuleRef outside of a Module"
            )

        return lf.Location(module_ref, self.parse_Location_Range(pb.range))

    def parse_Location_Range(self, pb: pblf.Location.Range) -> lf.Location.Range:
        return lf.Location.Range(pb.start_line, pb.start_col, pb.end_line, pb.end_col)

    def parse_TemplateChoice(self, pb: pblf.TemplateChoice) -> lf.TemplateChoice:
        return lf.TemplateChoice(
            name=self._resolve_string(pb.name_str, pb.name_interned_str),
            consuming=pb.consuming,
            controllers=self.parse_Expr(pb.controllers),
            observers=self.parse_Expr(pb.observers) if pb.HasField("observers") else None,
            arg_binder=self.parse_VarWithType(pb.arg_binder),
            ret_type=self.parse_Type(pb.ret_type),
            update=self.parse_Expr(pb.update),
            self_binder=self._resolve_string(pb.self_binder_str, pb.self_binder_interned_str),
            location=self.parse_Location(pb.location),
        )

    def parse_KeyExpr(self, pb: pblf.KeyExpr) -> lf.KeyExpr:
        if pb.HasField("projections"):
            return lf.KeyExpr(projections=self.parse_KeyExpr_Projections(pb.projections))
        elif pb.HasField("record"):
            return lf.KeyExpr(record=self.parse_KeyExpr_Record(pb.record))
        else:
            raise ValueError(f"unknown KeyExpr {pb}")

    def parse_KeyExpr_Projection(self, pb: pblf.KeyExpr.Projection) -> lf.KeyExpr.Projection:
        return lf.KeyExpr.Projection(
            tycon=self.parse_Type_Con(pb.tycon).con,
            field=self._resolve_string(pb.field_str, pb.field_interned_str),
        )

    def parse_KeyExpr_Projections(self, pb: pblf.KeyExpr.Projections) -> lf.KeyExpr.Projections:
        return lf.KeyExpr.Projections(
            projections=[self.parse_KeyExpr_Projection(p) for p in pb.projections]
        )

    def parse_KeyExpr_RecordField(self, pb: pblf.KeyExpr.RecordField) -> lf.KeyExpr.RecordField:
        return lf.KeyExpr.RecordField(
            field=self._resolve_string(pb.field_str, pb.field_interned_str),
            expr=self.parse_KeyExpr(pb.expr),
        )

    def parse_KeyExpr_Record(self, pb: pblf.KeyExpr.Record) -> lf.KeyExpr.Record:
        return lf.KeyExpr.Record(
            tycon=self.parse_Type_Con(pb.tycon).con,
            fields=[self.parse_KeyExpr_RecordField(p) for p in pb.fields],
        )

    def parse_DefTemplate(self, pb: pblf.DefTemplate) -> lf.DefTemplate:
        return lf.DefTemplate(
            tycon=self._resolve_dotted_name(pb.tycon_dname, pb.tycon_interned_dname),
            param=self._resolve_string(pb.param_str, pb.param_interned_str),
            precond=self.parse_Expr(pb.precond),
            signatories=self.parse_Expr(pb.signatories),
            agreement=self.parse_Expr(pb.agreement),
            choices=tuple(self.parse_TemplateChoice(choice) for choice in pb.choices),
            observers=self.parse_Expr(pb.observers),
            location=self.parse_Location(pb.location),
            key=self.parse_DefTemplate_DefKey(pb.key) if pb.HasField("key") else None,
        )

    def parse_DefTemplate_DefKey(self, pb: pblf.DefTemplate.DefKey) -> lf.DefTemplate.DefKey:
        kwargs = dict(type=self.parse_Type(pb.type), maintainers=self.parse_Expr(pb.maintainers))
        key_expr_name = pb.WhichOneof("key_expr")
        if key_expr_name == "key":
            kwargs["key"] = self.parse_KeyExpr(pb.key)
        elif key_expr_name == "complex_key":
            kwargs["complex_key"] = self.parse_Expr(pb.complex_key)
        return lf.DefTemplate.DefKey(**kwargs)

    def parse_DefDataType(self, pb: pblf.DefDataType) -> lf.DefDataType:
        name = self._resolve_dotted_name(pb.name_dname, pb.name_interned_dname)
        params = tuple(self.parse_TypeVarWithKind(param) for param in pb.params)
        serializable = pb.serializable
        location = self.parse_Location(pb.location)

        DataCons_name = pb.WhichOneof("DataCons")
        if DataCons_name == "record":
            return lf.DefDataType(
                name=name,
                params=params,
                serializable=serializable,
                location=location,
                record=self.parse_DefDataType_Fields(pb.record),
            )
        elif DataCons_name == "variant":
            return lf.DefDataType(
                name=name,
                params=params,
                serializable=serializable,
                location=location,
                variant=self.parse_DefDataType_Fields(pb.variant),
            )
        elif DataCons_name == "enum":
            return lf.DefDataType(
                name=name,
                params=params,
                serializable=serializable,
                location=location,
                enum=self.parse_DefDataType_EnumConstructors(pb.enum),
            )
        elif DataCons_name == "interface":
            return lf.DefDataType(
                name=name,
                params=params,
                serializable=serializable,
                location=location,
                interface=lf.UNIT,
            )
        else:
            raise ValueError(f"unknown DataCons value: {DataCons_name!r}")

    def parse_DefDataType_Fields(self, pb: pblf.DefDataType.Fields) -> lf.DefDataType.Fields:
        return lf.DefDataType.Fields(
            fields=tuple(self.parse_FieldWithType(field) for field in pb.fields)
        )

    def parse_DefDataType_EnumConstructors(
        self, pb: pblf.DefDataType.EnumConstructors
    ) -> lf.DefDataType.EnumConstructors:
        ctors_1 = tuple(pb.constructors_str)
        ctors_2 = tuple(self.interned_strings[idx] for idx in pb.constructors_interned_str)
        return lf.DefDataType.EnumConstructors(constructors=ctors_1 + ctors_2)

    def parse_DefTypeSyn(self, pb: pblf.DefTypeSyn) -> lf.DefTypeSyn:
        return lf.DefTypeSyn(
            name=self._resolve_dotted_name(pb.name_dname, pb.name_interned_dname),
            params=tuple(self.parse_TypeVarWithKind(param) for param in pb.params),
            type=self.parse_Type(pb.type),
            location=self.parse_Location(pb.location),
        )

    def parse_DefValue(self, pb: pblf.DefValue) -> lf.DefValue:
        return lf.DefValue(
            name_with_type=self.parse_DefValue_NameWithType(pb.name_with_type),
            expr=lambda: self.parse_Expr(pb.expr),
            no_party_literals=pb.no_party_literals,
            is_test=pb.is_test,
            location=self.parse_Location(pb.location),
        )

    def parse_DefValue_NameWithType(
        self, pb: pblf.DefValue.NameWithType
    ) -> lf.DefValue.NameWithType:
        return lf.DefValue.NameWithType(
            name=self._resolve_string_seq(pb.name_dname, pb.name_interned_dname),
            type=self.parse_Type(pb.type),
        )

    def parse_FeatureFlags(self, pb: pblf.FeatureFlags) -> lf.FeatureFlags:
        return lf.FeatureFlags(
            forbid_party_literals=pb.forbidPartyLiterals,
            dont_divulge_contract_ids_in_create_arguments=pb.dontDivulgeContractIdsInCreateArguments,
            dont_disclose_nonconsuming_choices_to_observers=pb.dontDiscloseNonConsumingChoicesToObservers,
        )

    def parse_Module(self, pb: pblf.Module) -> lf.Module:
        name = self._resolve_dotted_name(pb.name_dname, pb.name_interned_dname)
        self.current_module = lf.ModuleRef(self.current_package, name)
        child_parser = self._copy()
        try:
            module = lf.Module(
                name=name,
                flags=child_parser.parse_FeatureFlags(pb.flags),
                synonyms=tuple(child_parser.parse_DefTypeSyn(value) for value in pb.synonyms),
                data_types=tuple(
                    child_parser.parse_DefDataType(data_type) for data_type in pb.data_types
                ),
                values=tuple(child_parser.parse_DefValue(value) for value in pb.values),
                templates=tuple(
                    child_parser.parse_DefTemplate(template) for template in pb.templates
                ),
            )
        finally:
            self.current_module = None

        return module

    def parse_Package(self, pb: pblf.Package) -> lf.Package:
        # TODO: this modifies state in a parser which is less than ideal; a better pattern would be
        #  to create a sub-parser with the contextual state required to understand interned package
        #  IDs
        self.interned_strings.extend(pb.interned_strings)

        indices = [
            tuple(self.interned_strings[idx] for idx in idn.segments_interned_str)
            for idn in pb.interned_dotted_names
        ]

        self.interned_dotted_names.extend(indices)

        # types in the type intern table are allowed to refer to previously interned types, so we
        # must parse, then add each type individually
        for type_pb in pb.interned_types:
            self.interned_types.append(self.parse_Type(type_pb))

        return lf.Package(
            modules=tuple(self.parse_Module(module) for module in pb.modules),
            metadata=self.parse_PackageMetadata(pb.metadata) if pb.HasField("metadata") else None,
        )

    def parse_PackageMetadata(self, pb: pblf.PackageMetadata) -> lf.PackageMetadata:
        return lf.PackageMetadata(
            name=self.interned_strings[pb.name_interned_str],
            version=self.interned_strings[pb.version_interned_str],
        )

    def _copy(self) -> "ProtobufParser":
        p = ProtobufParser(self.current_package)
        p.current_module = self.current_module
        p.interned_strings = self.interned_strings
        p.interned_dotted_names = self.interned_dotted_names
        p.interned_types = self.interned_types
        return p

    def _resolve_string(self, name: Optional[str], interned_id: Optional[int]) -> str:
        # note that we intentionally conflate None and empty string, or None and 0 because
        # of Protobuf
        return name if name else self.interned_strings[interned_id or 0]

    def _resolve_string_seq(
        self, name: Optional[Sequence[str]], name_interned_id: Optional[int]
    ) -> Sequence[str]:
        if self.interned_dotted_names:
            return tuple(name) if name else self.interned_dotted_names[name_interned_id or 0]
        else:
            return tuple(name) if name else tuple()

    def _resolve_dotted_name(
        self, pb_dotted_name: pblf.DottedName, interned_id: Optional[int]
    ) -> lf.DottedName:
        return lf.DottedName(self._resolve_string_seq(pb_dotted_name.segments, interned_id))
