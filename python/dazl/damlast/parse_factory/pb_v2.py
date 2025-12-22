# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Optional, Sequence

from .. import daml_lf_1 as lf
from ..._gen.com.daml.daml_lf_2_1 import daml_lf2_pb2 as pblf
from .pb_parse_base import ProtobufParserBase

__all__ = ["ProtobufParser21"]


# noinspection PyPep8Naming,PyMethodMayBeStatic
class ProtobufParser21(ProtobufParserBase):
    def __init__(self, current_package: lf.PackageRef) -> None:
        self.current_package = current_package
        self.current_module = None  # type: Optional[lf.ModuleRef]
        self.interned_strings = list[str]()
        self.interned_dotted_names = list[Sequence[str]]()
        self.interned_types = list[lf.Type]()

    # noinspection PyUnusedLocal
    def parse_Unit(self, pb: pblf.Unit) -> lf.Unit:
        return lf.UNIT

    def parse_ModuleId(self, pb: pblf.ModuleId) -> Optional[lf.ModuleRef]:
        sum_name = pb.package_id.WhichOneof("Sum")
        if sum_name is None:
            return None

        module_name = lf.DottedName(self.interned_dotted_names[pb.module_name_interned_dname])
        match sum_name:
            case "self_package_id":
                return lf.ModuleRef(self.current_package, module_name)
            case "imported_package_id_interned_str":
                return lf.ModuleRef(
                    lf.PackageRef(
                        self.interned_strings[pb.package_id.imported_package_id_interned_str]
                    ),
                    module_name,
                )
            case "package_import_id":
                # Handle package_import_id case - use interned string lookup
                return lf.ModuleRef(
                    lf.PackageRef(self.interned_strings[pb.package_id.package_import_id]),
                    module_name,
                )
            case _:
                raise ValueError(f"unknown sum type value: {sum_name!r}")

    def parse_TypeConId(self, pb: pblf.TypeConId) -> lf.TypeConName:
        module_ref = self.parse_ModuleId(pb.module)
        if module_ref is None:
            raise ValueError("missing a valid ModuleId in a TypeConId definition")
        return lf.TypeConName(
            module_ref,
            self.interned_dotted_names[pb.name_interned_dname],
        )

    def parse_TypeSynId(self, pb: pblf.TypeSynId) -> lf.TypeSynName:
        module_ref = self.parse_ModuleId(pb.module)
        if module_ref is None:
            raise ValueError("missing a valid ModuleId in a TypeSynId definition")
        return lf.TypeSynName(
            module_ref,
            self.interned_dotted_names[pb.name_interned_dname],
        )

    def parse_ValueId(self, pb: pblf.ValueId) -> lf.ValName:
        module_ref = self.parse_ModuleId(pb.module)
        if module_ref is None:
            raise ValueError("missing a valid ModuleId in a ValueId definition")
        return lf.ValName(
            module_ref,
            self.interned_dotted_names[pb.name_interned_dname],
        )

    def parse_FieldWithType(self, pb: pblf.FieldWithType) -> lf.FieldWithType:
        """A field definition in a record or a variant associated with a type."""
        return lf.FieldWithType(
            self.interned_strings[pb.field_interned_str], self.parse_Type(pb.type)
        )

    def parse_VarWithType(self, pb: pblf.VarWithType) -> lf.VarWithType:
        """Binder associated with a type."""
        return lf.VarWithType(self.interned_strings[pb.var_interned_str], self.parse_Type(pb.type))

    def parse_TypeVarWithKind(self, pb: pblf.TypeVarWithKind) -> lf.TypeVarWithKind:
        return lf.TypeVarWithKind(
            self.interned_strings[pb.var_interned_str], self.parse_Kind(pb.kind)
        )

    def parse_FieldWithExpr(self, pb: pblf.FieldWithExpr) -> lf.FieldWithExpr:
        return lf.FieldWithExpr(
            self.interned_strings[pb.field_interned_str], self.parse_Expr(pb.expr)
        )

    def parse_Binding(self, pb: pblf.Binding) -> lf.Binding:
        return lf.Binding(self.parse_VarWithType(pb.binder), self.parse_Expr(pb.bound))

    def parse_Kind(self, pb: pblf.Kind) -> lf.Kind:
        sum_name = pb.WhichOneof("Sum")
        match sum_name:
            case "star":
                return lf.Kind(star=self.parse_Unit(pb.star))
            case "arrow":
                return lf.Kind(arrow=self.parse_Kind_Arrow(pb.arrow))
            case "nat":
                return lf.Kind(nat=self.parse_Unit(pb.nat))
            case _:
                raise ValueError(f"unknown sum type value: {sum_name!r}")

    def parse_Kind_Arrow(self, pb: pblf.Kind.Arrow) -> lf.Kind.Arrow:
        return lf.Kind.Arrow(
            tuple(self.parse_Kind(param) for param in pb.params), self.parse_Kind(pb.result)
        )

    def parse_BuiltinType(self, pb: pblf.BuiltinType) -> lf.PrimType:
        return lf.PrimType(pb)

    def parse_Type(self, pb: pblf.Type) -> lf.Type:
        sum_name = pb.WhichOneof("Sum")
        match sum_name:
            case "var":
                return self.parse_Type_Var(pb.var)
            case "con":
                return self.parse_Type_Con(pb.con)
            case "builtin":
                return lf.Type(prim=self.parse_Type_Builtin(pb.builtin))
            case "forall":
                return lf.Type(forall=self.parse_Type_Forall(pb.forall))
            case "struct":
                return lf.Type(struct=self.parse_Type_Struct(pb.struct))
            case "nat":
                return lf.Type(nat=pb.nat)
            case "syn":
                return lf.Type(syn=self.parse_Type_Syn(pb.syn))
            case "interned_type":
                return self.interned_types[pb.interned_type]
            case _:
                raise ValueError(f"unknown sum type value: {sum_name!r}")

    def parse_Type_Var(self, pb: pblf.Type.Var) -> lf.Type:
        return lf.Type(
            var=lf.Type.Var(
                self.interned_strings[pb.var_interned_str],
                tuple(self.parse_Type(arg) for arg in pb.args),
            )
        )

    def parse_Type_Con(self, pb: pblf.Type.Con) -> lf.Type:
        """
        Create a :class:`Type` instance (but may produce something slightly different than the AST
        due to ``Map``/``Optional`` type rewriting).
        """
        tycon = self.parse_TypeConId(pb.tycon)
        args = tuple(self.parse_Type(arg) for arg in pb.args)
        return lf.Type(con=lf.Type.Con(tycon, args))

    def parse_Type_Builtin(self, pb: pblf.Type.Builtin) -> lf.Type.Prim:
        return lf.Type.Prim(
            self.parse_BuiltinType(pb.builtin), tuple(self.parse_Type(arg) for arg in pb.args)
        )

    def parse_Type_Forall(self, pb: pblf.Type.Forall) -> lf.Type.Forall:
        return lf.Type.Forall(
            tuple(self.parse_TypeVarWithKind(var) for var in pb.vars), self.parse_Type(pb.body)
        )

    def parse_Type_Struct(self, pb: pblf.Type.Struct) -> lf.Type.Struct:
        return lf.Type.Struct(tuple(self.parse_FieldWithType(field) for field in pb.fields))

    def parse_Type_Syn(self, pb: pblf.Type.Syn) -> lf.Type.Syn:
        return lf.Type.Syn(
            tysyn=self.parse_TypeSynId(pb.tysyn),
            args=tuple(self.parse_Type(arg) for arg in pb.args),
        )

    def parse_BuiltinCon(self, pb: pblf.BuiltinCon) -> lf.PrimCon:
        match pb:
            case pblf.BuiltinCon.CON_UNIT:
                return lf.PrimCon.CON_UNIT
            case pblf.BuiltinCon.CON_FALSE:
                return lf.PrimCon.CON_FALSE
            case pblf.BuiltinCon.CON_TRUE:
                return lf.PrimCon.CON_TRUE
            case _:
                raise ValueError(f"unknown enum value: {pb!r}")

    def parse_BuiltinFunction(self, pb: pblf.BuiltinFunction) -> lf.BuiltinFunction:
        return lf.BuiltinFunction(pb)

    def parse_BuiltinLit(self, pb: pblf.BuiltinLit) -> lf.PrimLit:
        sum_name = pb.WhichOneof("Sum")
        match sum_name:
            case "int64":
                return lf.PrimLit(int64=pb.int64)
            case "numeric_interned_str":
                return lf.PrimLit(numeric=self.interned_strings[pb.numeric_interned_str])
            case "text_interned_str":
                return lf.PrimLit(text=self.interned_strings[pb.text_interned_str])
            case "timestamp":
                return lf.PrimLit(timestamp=pb.timestamp)
            case "date":
                return lf.PrimLit(date=pb.date)
            case "rounding_mode":
                return lf.PrimLit(
                    rounding_mode=self.parse_BuiltinLit_RoundingMode(pb.rounding_mode)
                )
            case _:
                raise ValueError(f"unknown Sum value: {pb!r}")

    def parse_BuiltinLit_RoundingMode(
        self, pb: pblf.BuiltinLit.RoundingMode
    ) -> lf.PrimLit.RoundingMode:
        return lf.PrimLit.RoundingMode(pb)

    def parse_Expr(self, pb: pblf.Expr) -> lf.Expr:
        location = self.parse_Location(pb.location) if pb.HasField("location") else None

        sum_name = pb.WhichOneof("Sum")
        match sum_name:
            case "var_interned_str":
                return lf.Expr(var=self.interned_strings[pb.var_interned_str], location=location)
            case "val":
                return lf.Expr(val=self.parse_ValueId(pb.val), location=location)
            case "builtin":
                return lf.Expr(builtin=self.parse_BuiltinFunction(pb.builtin), location=location)
            case "builtin_con":
                return lf.Expr(prim_con=self.parse_BuiltinCon(pb.builtin_con), location=location)
            case "builtin_lit":
                return lf.Expr(prim_lit=self.parse_BuiltinLit(pb.builtin_lit), location=location)
            case "rec_con":
                return lf.Expr(rec_con=self.parse_Expr_RecCon(pb.rec_con), location=location)
            case "rec_proj":
                return lf.Expr(rec_proj=self.parse_Expr_RecProj(pb.rec_proj), location=location)
            case "rec_upd":
                return lf.Expr(rec_upd=self.parse_Expr_RecUpd(pb.rec_upd), location=location)
            case "variant_con":
                return lf.Expr(
                    variant_con=self.parse_Expr_VariantCon(pb.variant_con), location=location
                )
            case "enum_con":
                return lf.Expr(enum_con=self.parse_Expr_EnumCon(pb.enum_con), location=location)
            case "struct_con":
                return lf.Expr(
                    struct_con=self.parse_Expr_StructCon(pb.struct_con), location=location
                )
            case "struct_proj":
                return lf.Expr(
                    struct_proj=self.parse_Expr_StructProj(pb.struct_proj), location=location
                )
            case "struct_upd":
                return lf.Expr(
                    struct_upd=self.parse_Expr_StructUpd(pb.struct_upd), location=location
                )
            case "app":
                return lf.Expr(app=self.parse_Expr_App(pb.app), location=location)
            case "ty_app":
                return lf.Expr(ty_app=self.parse_Expr_TyApp(pb.ty_app), location=location)
            case "abs":
                return lf.Expr(abs=self.parse_Expr_Abs(pb.abs), location=location)
            case "ty_abs":
                return lf.Expr(ty_abs=self.parse_Expr_TyAbs(pb.ty_abs), location=location)
            case "case":
                return lf.Expr(case=self.parse_Case(pb.case), location=location)
            case "let":
                return lf.Expr(let=self.parse_Block(pb.let), location=location)
            case "nil":
                return lf.Expr(nil=self.parse_Expr_Nil(pb.nil), location=location)
            case "cons":
                return lf.Expr(cons=self.parse_Expr_Cons(pb.cons), location=location)
            case "update":
                return lf.Expr(update=self.parse_Update(pb.update), location=location)
            case "optional_none":
                return lf.Expr(
                    optional_none=self.parse_Expr_OptionalNone(pb.optional_none), location=location
                )
            case "optional_some":
                return lf.Expr(
                    optional_some=self.parse_Expr_OptionalSome(pb.optional_some), location=location
                )
            case "to_any":
                return lf.Expr(to_any=self.parse_Expr_ToAny(pb.to_any), location=location)
            case "from_any":
                return lf.Expr(from_any=self.parse_Expr_FromAny(pb.from_any), location=location)
            case "type_rep":
                return lf.Expr(type_rep=self.parse_Type(pb.type_rep), location=location)
            case "to_any_exception":
                return lf.Expr(
                    to_any_exception=self.parse_Expr_ToAnyException(pb.to_any_exception),
                    location=location,
                )
            case "from_any_exception":
                return lf.Expr(
                    from_any_exception=self.parse_Expr_FromAnyException(pb.from_any_exception),
                    location=location,
                )
            case "throw":
                return lf.Expr(throw=self.parse_Expr_Throw(pb.throw), location=location)
            case "to_interface":
                return lf.Expr(
                    to_interface=self.parse_Expr_ToInterface(pb.to_interface), location=location
                )
            case "from_interface":
                return lf.Expr(
                    from_interface=self.parse_Expr_FromInterface(pb.from_interface),
                    location=location,
                )
            case "call_interface":
                return lf.Expr(
                    call_interface=self.parse_Expr_CallInterface(pb.call_interface),
                    location=location,
                )
            case "signatory_interface":
                return lf.Expr(
                    signatory_interface=self.parse_Expr_SignatoryInterface(pb.signatory_interface),
                    location=location,
                )
            case "observer_interface":
                return lf.Expr(
                    observer_interface=self.parse_Expr_ObserverInterface(pb.observer_interface),
                    location=location,
                )
            case "view_interface":
                return lf.Expr(
                    view_interface=self.parse_Expr_ViewInterface(pb.view_interface),
                    location=location,
                )
            case "unsafe_from_interface":
                return lf.Expr(
                    unsafe_from_interface=self.parse_Expr_UnsafeFromInterface(
                        pb.unsafe_from_interface
                    ),
                    location=location,
                )
            case "interface_template_type_rep":
                return lf.Expr(
                    interface_template_type_rep=self.parse_Expr_InterfaceTemplateTypeRep(
                        pb.interface_template_type_rep
                    ),
                    location=location,
                )
            case "to_required_interface":
                return lf.Expr(
                    to_required_interface=self.parse_Expr_ToRequiredInterface(
                        pb.to_required_interface
                    ),
                    location=location,
                )
            case "from_required_interface":
                return lf.Expr(
                    from_required_interface=self.parse_Expr_FromRequiredInterface(
                        pb.from_required_interface
                    ),
                    location=location,
                )
            case "unsafe_from_required_interface":
                return lf.Expr(
                    unsafe_from_required_interface=self.parse_Expr_UnsafeFromRequiredInterface(
                        pb.unsafe_from_required_interface
                    ),
                    location=location,
                )
            case "experimental":
                return lf.Expr(
                    experimental=self.parse_Expr_Experimental(pb.experimental), location=location
                )
            case "choice_controller":
                return lf.Expr(
                    choice_controller=self.parse_Expr_ChoiceController(pb.choice_controller),
                    location=location,
                )
            case "choice_observer":
                return lf.Expr(
                    choice_observer=self.parse_Expr_ChoiceObserver(pb.choice_observer),
                    location=location,
                )
            case _:
                raise ValueError(f"Unknown type of Expr: {sum_name!r}")

    def parse_Expr_RecCon(self, pb: pblf.Expr.RecCon) -> lf.Expr.RecCon:
        return lf.Expr.RecCon(
            self.parse_Type_Con(pb.tycon).con,
            tuple(self.parse_FieldWithExpr(field) for field in pb.fields),
        )  # length > 0

    def parse_Expr_RecProj(self, pb: pblf.Expr.RecProj) -> lf.Expr.RecProj:
        return lf.Expr.RecProj(
            self.parse_Type_Con(pb.tycon).con,  # Always fully applied
            self.interned_strings[pb.field_interned_str],
            self.parse_Expr(pb.record),
        )

    def parse_Expr_RecUpd(self, pb: pblf.Expr.RecUpd) -> lf.Expr.RecUpd:
        """Set ``field`` in ``record`` to ``update``."""
        return lf.Expr.RecUpd(
            self.parse_Type_Con(pb.tycon).con,
            self.interned_strings[pb.field_interned_str],
            self.parse_Expr(pb.record),
            self.parse_Expr(pb.update),
        )

    def parse_Expr_VariantCon(self, pb: pblf.Expr.VariantCon) -> lf.Expr.VariantCon:
        return lf.Expr.VariantCon(
            self.parse_Type_Con(pb.tycon).con,  # Always fully applied
            self.interned_strings[pb.variant_con_interned_str],
            self.parse_Expr(pb.variant_arg),
        )

    def parse_Expr_StructCon(self, pb: pblf.Expr.StructCon) -> lf.Expr.StructCon:
        return lf.Expr.StructCon(
            tuple(self.parse_FieldWithExpr(field) for field in pb.fields)
        )  # length > 0

    def parse_Expr_EnumCon(self, pb: pblf.Expr.EnumCon) -> lf.Expr.EnumCon:
        return lf.Expr.EnumCon(
            self.parse_TypeConId(pb.tycon),
            self.interned_strings[pb.enum_con_interned_str],
        )

    def parse_Expr_StructProj(self, pb: pblf.Expr.StructProj) -> lf.Expr.StructProj:
        return lf.Expr.StructProj(
            self.interned_strings[pb.field_interned_str], self.parse_Expr(pb.struct)
        )

    def parse_Expr_StructUpd(self, pb: pblf.Expr.StructUpd) -> lf.Expr.StructUpd:
        """Set ``field`` in ``tuple`` to ``update``."""
        return lf.Expr.StructUpd(
            self.interned_strings[pb.field_interned_str],
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
        return lf.Expr.OptionalSome(self.parse_Type(pb.type), self.parse_Expr(pb.value))

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
            interface_type=self.parse_TypeConId(pb.interface_type),
            template_type=self.parse_TypeConId(pb.template_type),
            template_expr=self.parse_Expr(pb.template_expr),
        )

    def parse_Expr_FromInterface(self, pb: pblf.Expr.FromInterface) -> lf.Expr.FromInterface:
        return lf.Expr.FromInterface(
            interface_type=self.parse_TypeConId(pb.interface_type),
            template_type=self.parse_TypeConId(pb.template_type),
            interface_expr=self.parse_Expr(pb.interface_expr),
        )

    def parse_Expr_CallInterface(self, pb: pblf.Expr.CallInterface) -> lf.Expr.CallInterface:
        return lf.Expr.CallInterface(
            interface_type=self.parse_TypeConId(pb.interface_type),
            method_name=self.interned_strings[pb.method_interned_name],
            interface_expr=self.parse_Expr(pb.interface_expr),
        )

    def parse_Expr_SignatoryInterface(
        self, pb: pblf.Expr.SignatoryInterface
    ) -> lf.Expr.SignatoryInterface:
        return lf.Expr.SignatoryInterface(
            interface=self.parse_TypeConId(pb.interface),
            expr=self.parse_Expr(pb.expr),
        )

    def parse_Expr_ObserverInterface(
        self, pb: pblf.Expr.ObserverInterface
    ) -> lf.Expr.ObserverInterface:
        return lf.Expr.ObserverInterface(
            interface=self.parse_TypeConId(pb.interface),
            expr=self.parse_Expr(pb.expr),
        )

    def parse_Expr_ViewInterface(self, pb: pblf.Expr.ViewInterface) -> lf.Expr.ViewInterface:
        return lf.Expr.ViewInterface(
            interface=self.parse_TypeConId(pb.interface),
            expr=self.parse_Expr(pb.expr),
        )

    def parse_Expr_UnsafeFromInterface(
        self, pb: pblf.Expr.UnsafeFromInterface
    ) -> lf.Expr.UnsafeFromInterface:
        return lf.Expr.UnsafeFromInterface(
            interface_type=self.parse_TypeConId(pb.interface_type),
            template_type=self.parse_TypeConId(pb.template_type),
            contract_id_expr=self.parse_Expr(pb.contract_id_expr),
            interface_expr=self.parse_Expr(pb.interface_expr),
        )

    def parse_Expr_InterfaceTemplateTypeRep(
        self, pb: pblf.Expr.InterfaceTemplateTypeRep
    ) -> lf.Expr.InterfaceTemplateTypeRep:
        return lf.Expr.InterfaceTemplateTypeRep(
            interface=self.parse_TypeConId(pb.interface),
            expr=self.parse_Expr(pb.expr),
        )

    def parse_Expr_ToRequiredInterface(
        self, pb: pblf.Expr.ToRequiredInterface
    ) -> lf.Expr.ToRequiredInterface:
        return lf.Expr.ToRequiredInterface(
            required_interface=self.parse_TypeConId(pb.required_interface),
            requiring_interface=self.parse_TypeConId(pb.requiring_interface),
            expr=self.parse_Expr(pb.expr),
        )

    def parse_Expr_FromRequiredInterface(
        self, pb: pblf.Expr.FromRequiredInterface
    ) -> lf.Expr.FromRequiredInterface:
        return lf.Expr.FromRequiredInterface(
            required_interface=self.parse_TypeConId(pb.required_interface),
            requiring_interface=self.parse_TypeConId(pb.requiring_interface),
            expr=self.parse_Expr(pb.expr),
        )

    def parse_Expr_UnsafeFromRequiredInterface(
        self, pb: pblf.Expr.UnsafeFromRequiredInterface
    ) -> lf.Expr.UnsafeFromRequiredInterface:
        return lf.Expr.UnsafeFromRequiredInterface(
            required_interface=self.parse_TypeConId(pb.required_interface),
            requiring_interface=self.parse_TypeConId(pb.requiring_interface),
            contract_id_expr=self.parse_Expr(pb.contract_id_expr),
            interface_expr=self.parse_Expr(pb.interface_expr),
        )

    def parse_Expr_Experimental(self, pb: pblf.Expr.Experimental) -> lf.Expr.Experimental:
        return lf.Expr.Experimental(name=pb.name, type=self.parse_Type(pb.type))

    def parse_Expr_ChoiceController(
        self, pb: pblf.Expr.ChoiceController
    ) -> lf.Expr.ChoiceController:
        return lf.Expr.ChoiceController(
            template=self.parse_TypeConId(pb.template),
            choice=self.interned_strings[pb.choice_interned_str],
            contract_expr=self.parse_Expr(pb.contract_expr),
            choice_arg_expr=self.parse_Expr(pb.choice_arg_expr),
        )

    def parse_Expr_ChoiceObserver(self, pb: pblf.Expr.ChoiceObserver) -> lf.Expr.ChoiceObserver:
        return lf.Expr.ChoiceObserver(
            template=self.parse_TypeConId(pb.template),
            choice=self.interned_strings[pb.choice_interned_str],
            contract_expr=self.parse_Expr(pb.contract_expr),
            choice_arg_expr=self.parse_Expr(pb.choice_arg_expr),
        )

    def parse_CaseAlt(self, pb: pblf.CaseAlt) -> lf.CaseAlt:
        body = self.parse_Expr(pb.body)
        sum_name = pb.WhichOneof("Sum")
        match sum_name:
            case "default":
                return lf.CaseAlt(default=self.parse_Unit(pb.default), body=body)
            case "variant":
                return lf.CaseAlt(variant=self.parse_CaseAlt_Variant(pb.variant), body=body)
            case "builtin_con":
                return lf.CaseAlt(prim_con=self.parse_BuiltinCon(pb.builtin_con), body=body)
            case "nil":
                return lf.CaseAlt(nil=self.parse_Unit(pb.nil), body=body)
            case "cons":
                return lf.CaseAlt(cons=self.parse_CaseAlt_Cons(pb.cons), body=body)
            case "optional_none":
                return lf.CaseAlt(optional_none=self.parse_Unit(pb.optional_none), body=body)
            case "optional_some":
                return lf.CaseAlt(
                    optional_some=self.parse_CaseAlt_OptionalSome(pb.optional_some), body=body
                )
            case "enum":
                return lf.CaseAlt(enum=self.parse_CaseAlt_Enum(pb.enum), body=body)
            case _:
                raise ValueError(f"unknown Sum value: {sum_name!r}")

    def parse_CaseAlt_Variant(self, pb: pblf.CaseAlt.Variant) -> lf.CaseAlt.Variant:
        return lf.CaseAlt.Variant(
            self.parse_TypeConId(pb.con),
            self.interned_strings[pb.variant_interned_str],
            self.interned_strings[pb.binder_interned_str],
        )

    def parse_CaseAlt_Enum(self, pb: pblf.CaseAlt.Enum) -> lf.CaseAlt.Enum:
        return lf.CaseAlt.Enum(
            self.parse_TypeConId(pb.con),
            self.interned_strings[pb.constructor_interned_str],
        )

    def parse_CaseAlt_Cons(self, pb: pblf.CaseAlt.Cons) -> lf.CaseAlt.Cons:
        return lf.CaseAlt.Cons(
            self.interned_strings[pb.var_head_interned_str],
            self.interned_strings[pb.var_tail_interned_str],
        )

    def parse_CaseAlt_OptionalSome(self, pb: pblf.CaseAlt.OptionalSome) -> lf.CaseAlt.OptionalSome:
        return lf.CaseAlt.OptionalSome(self.interned_strings[pb.var_body_interned_str])

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
        match sum_name:
            case "pure":
                return lf.Update(pure=self.parse_Pure(pb.pure))
            case "block":
                return lf.Update(block=self.parse_Block(pb.block))
            case "create":
                return lf.Update(create=self.parse_Update_Create(pb.create))
            case "exercise":
                return lf.Update(exercise=self.parse_Update_Exercise(pb.exercise))
            case "exercise_by_key":
                return lf.Update(
                    exercise_by_key=self.parse_Update_ExerciseByKey(pb.exercise_by_key)
                )
            case "fetch":
                return lf.Update(fetch=self.parse_Update_Fetch(pb.fetch))
            case "get_time":
                return lf.Update(get_time=self.parse_Unit(pb.get_time))
            case "lookup_by_key":
                return lf.Update(lookup_by_key=self.parse_Update_RetrieveByKey(pb.lookup_by_key))
            case "fetch_by_key":
                return lf.Update(fetch_by_key=self.parse_Update_RetrieveByKey(pb.fetch_by_key))
            case "embed_expr":
                return lf.Update(embed_expr=self.parse_Update_EmbedExpr(pb.embed_expr))
            case "try_catch":
                return lf.Update(try_catch=self.parse_Update_TryCatch(pb.try_catch))
            case "create_interface":
                return lf.Update(
                    create_interface=self.parse_Update_CreateInterface(pb.create_interface)
                )
            case "exercise_interface":
                return lf.Update(
                    exercise_interface=self.parse_Update_ExerciseInterface(pb.exercise_interface)
                )
            case "fetch_interface":
                return lf.Update(
                    fetch_interface=self.parse_Update_FetchInterface(pb.fetch_interface)
                )
            case _:
                raise ValueError(f"unknown Sum value: {sum_name!r}")

    def parse_Update_Create(self, pb: pblf.Update.Create) -> lf.Update.Create:
        return lf.Update.Create(
            template=self.parse_TypeConId(pb.template), expr=self.parse_Expr(pb.expr)
        )

    def parse_Update_Exercise(self, pb: pblf.Update.Exercise) -> lf.Update.Exercise:
        return lf.Update.Exercise(
            template=self.parse_TypeConId(pb.template),
            choice=self.interned_strings[pb.choice_interned_str],
            cid=self.parse_Expr(pb.cid),
            arg=self.parse_Expr(pb.arg),
        )

    def parse_Update_ExerciseByKey(self, pb: pblf.Update.ExerciseByKey) -> lf.Update.ExerciseByKey:
        return lf.Update.ExerciseByKey(
            template=self.parse_TypeConId(pb.template),
            choice=self.interned_strings[pb.choice_interned_str],
            key=self.parse_Expr(pb.key),
            arg=self.parse_Expr(pb.arg),
        )

    def parse_Update_Fetch(self, pb: pblf.Update.Fetch) -> lf.Update.Fetch:
        return lf.Update.Fetch(
            template=self.parse_TypeConId(pb.template), cid=self.parse_Expr(pb.cid)
        )

    def parse_Update_EmbedExpr(self, pb: pblf.Update.EmbedExpr) -> lf.Update.EmbedExpr:
        return lf.Update.EmbedExpr(type=self.parse_Type(pb.type), body=self.parse_Expr(pb.body))

    def parse_Update_RetrieveByKey(self, pb: pblf.Update.RetrieveByKey) -> lf.Update.RetrieveByKey:
        # Note: key field was removed in Daml-LF 2.x (3.4.9+)
        # Create a placeholder expression for compatibility
        return lf.Update.RetrieveByKey(
            template=self.parse_TypeConId(pb.template),
            key=lf.Expr(prim_con=lf.PrimCon.CON_UNIT),  # Placeholder - key is no longer in proto
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
            interface=self.parse_TypeConId(pb.interface),
            expr=self.parse_Expr(pb.expr),
        )

    def parse_Update_ExerciseInterface(
        self, pb: pblf.Update.ExerciseInterface
    ) -> lf.Update.ExerciseInterface:
        return lf.Update.ExerciseInterface(
            interface=self.parse_TypeConId(pb.interface),
            cid=self.parse_Expr(pb.cid),
            arg=self.parse_Expr(pb.arg),
            guard=self.parse_Expr(pb.guard) if pb.HasField("guard") else None,
        )

    def parse_Update_FetchInterface(
        self, pb: pblf.Update.FetchInterface
    ) -> lf.Update.FetchInterface:
        return lf.Update.FetchInterface(
            interface=self.parse_TypeConId(pb.interface),
            cid=self.parse_Expr(pb.cid),
        )

    def parse_Scenario(self, pb: object) -> lf.Scenario:
        # Scenarios are not supported in Daml-LF 2.x (3.4.9+)
        raise NotImplementedError("Scenarios are not supported in Daml-LF 2.x")

    def parse_Location(self, pb: pblf.Location) -> lf.Location:
        module_ref = self.parse_ModuleId(pb.module)
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
            name=self.interned_strings[pb.name_interned_str],
            consuming=pb.consuming,
            controllers=self.parse_Expr(pb.controllers),
            observers=self.parse_Expr(pb.observers) if pb.HasField("observers") else None,
            authorizers=self.parse_Expr(pb.authorizers) if pb.HasField("authorizers") else None,
            arg_binder=self.parse_VarWithType(pb.arg_binder),
            ret_type=self.parse_Type(pb.ret_type),
            update=self.parse_Expr(pb.update),
            self_binder=self.interned_strings[pb.self_binder_interned_str],
            location=self.parse_Location(pb.location),
        )

    def parse_DefTemplate(self, pb: pblf.DefTemplate) -> lf.DefTemplate:
        return lf.DefTemplate(
            tycon=lf.DottedName(self.interned_dotted_names[pb.tycon_interned_dname]),
            param=self.interned_strings[pb.param_interned_str],
            precond=self.parse_Expr(pb.precond) if pb.HasField("precond") else None,
            signatories=self.parse_Expr(pb.signatories) if pb.HasField("signatories") else None,
            agreement=None,  # agreement field removed in Daml-LF 2.x (3.4.9+)
            choices=tuple(self.parse_TemplateChoice(choice) for choice in pb.choices),
            observers=self.parse_Expr(pb.observers) if pb.HasField("observers") else None,
            location=self.parse_Location(pb.location),
            key=self.parse_DefTemplate_DefKey(pb.key) if pb.HasField("key") else None,
        )

    def parse_DefTemplate_DefKey(self, pb: pblf.DefTemplate.DefKey) -> lf.DefTemplate.DefKey:
        return lf.DefTemplate.DefKey(
            type=self.parse_Type(pb.type),
            complex_key=self.parse_Expr(pb.key_expr),
            maintainers=self.parse_Expr(pb.maintainers),
        )

    def parse_DefDataType(self, pb: pblf.DefDataType) -> lf.DefDataType:
        name = lf.DottedName(self.interned_dotted_names[pb.name_interned_dname])
        params = tuple(self.parse_TypeVarWithKind(param) for param in pb.params)
        serializable = pb.serializable
        location = self.parse_Location(pb.location)

        DataCons_name = pb.WhichOneof("DataCons")
        match DataCons_name:
            case "record":
                return lf.DefDataType(
                    name=name,
                    params=params,
                    serializable=serializable,
                    location=location,
                    record=self.parse_DefDataType_Fields(pb.record),
                )
            case "variant":
                return lf.DefDataType(
                    name=name,
                    params=params,
                    serializable=serializable,
                    location=location,
                    variant=self.parse_DefDataType_Fields(pb.variant),
                )
            case "enum":
                return lf.DefDataType(
                    name=name,
                    params=params,
                    serializable=serializable,
                    location=location,
                    enum=self.parse_DefDataType_EnumConstructors(pb.enum),
                )
            case "interface":
                return lf.DefDataType(
                    name=name,
                    params=params,
                    serializable=serializable,
                    location=location,
                    interface=lf.UNIT,
                )
            case _:
                raise ValueError(f"unknown DataCons value: {DataCons_name!r}")

    def parse_DefDataType_Fields(self, pb: pblf.DefDataType.Fields) -> lf.DefDataType.Fields:
        return lf.DefDataType.Fields(
            fields=tuple(self.parse_FieldWithType(field) for field in pb.fields)
        )

    def parse_DefDataType_EnumConstructors(
        self, pb: pblf.DefDataType.EnumConstructors
    ) -> lf.DefDataType.EnumConstructors:
        ctors = tuple(self.interned_strings[idx] for idx in pb.constructors_interned_str)
        return lf.DefDataType.EnumConstructors(constructors=ctors)

    def parse_DefTypeSyn(self, pb: pblf.DefTypeSyn) -> lf.DefTypeSyn:
        return lf.DefTypeSyn(
            name=lf.DottedName(self.interned_dotted_names[pb.name_interned_dname]),
            params=tuple(self.parse_TypeVarWithKind(param) for param in pb.params),
            type=self.parse_Type(pb.type),
            location=self.parse_Location(pb.location),
        )

    def parse_DefValue(self, pb: pblf.DefValue) -> lf.DefValue:
        return lf.DefValue(
            name_with_type=self.parse_DefValue_NameWithType(pb.name_with_type),
            expr=lambda: self.parse_Expr(pb.expr),
            no_party_literals=False,
            is_test=False,  # is_test field removed in Daml-LF 2.x (3.4.9+)
            location=self.parse_Location(pb.location),
        )

    def parse_DefValue_NameWithType(
        self, pb: pblf.DefValue.NameWithType
    ) -> lf.DefValue.NameWithType:
        return lf.DefValue.NameWithType(
            name=self.interned_dotted_names[pb.name_interned_dname],
            type=self.parse_Type(pb.type),
        )

    def parse_FeatureFlags(self, pb: pblf.FeatureFlags) -> lf.FeatureFlags:
        return lf.FeatureFlags(
            forbid_party_literals=pb.forbidPartyLiterals,
            dont_divulge_contract_ids_in_create_arguments=pb.dontDivulgeContractIdsInCreateArguments,
            dont_disclose_nonconsuming_choices_to_observers=pb.dontDiscloseNonConsumingChoicesToObservers,
        )

    def parse_Module(self, pb: pblf.Module) -> lf.Module:
        name = lf.DottedName(self.interned_dotted_names[pb.name_interned_dname])
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
                interfaces=tuple(
                    child_parser.parse_DefInterface(interface) for interface in pb.interfaces
                ),
            )
        finally:
            self.current_module = None

        return module

    def parse_InterfaceMethod(self, pb: pblf.InterfaceMethod) -> lf.InterfaceMethod:
        return lf.InterfaceMethod(
            method_name=self.interned_strings[pb.method_interned_name],
            type=self.parse_Type(pb.type),
        )

    def parse_DefInterface(self, pb: pblf.DefInterface) -> lf.DefInterface:
        return lf.DefInterface(
            name=lf.DottedName(self.interned_dotted_names[pb.tycon_interned_dname]),
            methods=tuple(self.parse_InterfaceMethod(method) for method in pb.methods),
            param=self.interned_strings[pb.param_interned_str],
            choices=tuple(self.parse_TemplateChoice(choice) for choice in pb.choices),
            view=self.parse_Type(pb.view),
            requires=tuple(self.parse_TypeConId(require) for require in pb.requires),
        )

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
            upgraded_package_id=(
                self.parse_UpgradedPackageId(pb.upgraded_package_id)
                if pb.HasField("upgraded_package_id")
                else None
            ),
        )

    def parse_UpgradedPackageId(self, pb: pblf.UpgradedPackageId) -> lf.UpgradedPackageId:
        return lf.UpgradedPackageId(
            upgraded_package_id=lf.PackageRef(
                self.interned_strings[pb.upgraded_package_id_interned_str]
            )
        )

    def _copy(self) -> "ProtobufParser21":
        p = ProtobufParser21(self.current_package)
        p.current_module = self.current_module
        p.interned_strings = self.interned_strings
        p.interned_dotted_names = self.interned_dotted_names
        p.interned_types = self.interned_types
        return p
