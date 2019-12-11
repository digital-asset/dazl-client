# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from .daml_lf_1 import *
from ..model.types import ModuleRef, TypeReference


# noinspection PyPep8Naming,PyMethodMayBeStatic
class ProtobufParser:
    def __init__(self, current_package: str):
        from typing import List
        self.current_package = current_package
        self.interned_strings = []  # type: List[str]
        self.interned_dotted_names = []  # type: List[List[int]]

    # noinspection PyUnusedLocal
    def parse_Unit(self, pb) -> 'Unit':
        return UNIT

    def parse_ModuleRef(self, pb) -> 'Optional[ModuleRef]':
        sum_name = pb.package_ref.WhichOneof('Sum')
        module_name = self._resolve_dotted_name(pb.module_name_dname, pb.module_name_interned_dname)
        if sum_name is None:
            return None
        elif sum_name == 'self':
            return ModuleRef(self.current_package, module_name.segments)
        elif sum_name == 'package_id_str':
            return ModuleRef(pb.package_ref.package_id_str, module_name.segments)
        elif sum_name == 'package_id_interned_str':
            return ModuleRef(
                self.interned_strings[pb.package_ref.package_id_interned_str], module_name.segments)
        else:
            raise ValueError(f'unknown sum type value: {sum_name!r}')

    def parse_TypeConName(self, pb) -> 'TypeReference':
        return TypeReference(
            self.parse_ModuleRef(pb.module),
            self._resolve_dotted_name(pb.name_dname, pb.name_interned_dname).segments)

    def parse_DottedName(self, pb) -> 'DottedName':
        return DottedName(segments=self._resolve_string_seq(pb.segments, pb.segments_interned_id))

    def parse_ValName(self, pb) -> 'ValName':
        return ValName(
            self.parse_ModuleRef(pb.module),
            self._resolve_string_seq(pb.name_dname, pb.name_interned_dname))

    def parse_FieldWithType(self, pb) -> 'FieldWithType':
        """A field definition in a record or a variant associated with a type."""
        return FieldWithType(
            self._resolve_string(pb.field_str, pb.field_interned_str),
            self.parse_Type(pb.type))

    def parse_VarWithType(self, pb) -> 'VarWithType':
        """Binder associated with a type."""
        return VarWithType(
            self._resolve_string(pb.var_str, pb.var_interned_str),
            self.parse_Type(pb.type))

    def parse_TypeVarWithKind(self, pb) -> 'TypeVarWithKind':
        return TypeVarWithKind(
            self._resolve_string(pb.var_str, pb.var_interned_str),
            self.parse_Kind(pb.kind))

    def parse_FieldWithExpr(self, pb) -> 'FieldWithExpr':
        return FieldWithExpr(
            self._resolve_string(pb.field_str, pb.field_interned_str),
            self.parse_Expr(pb.expr))

    def parse_Binding(self, pb) -> 'Binding':
        return Binding(
            self.parse_VarWithType(pb.binder),
            self.parse_Expr(pb.bound))

    def parse_Kind(self, pb) -> 'Optional[Kind]':
        sum_name = pb.WhichOneof('Sum')
        if sum_name is None:
            return None
        elif sum_name == 'star':
            return Kind(star=self.parse_Unit(pb.star))
        elif sum_name == 'arrow':
            return Kind(arrow=self.parse_Kind_Arrow(pb.arrow))
        elif sum_name == 'nat':
            return Kind(nat=pb.nat)
        else:
            raise ValueError(f'unknown sum type value: {sum_name!r}')

    def parse_Kind_Arrow(self, pb) -> 'Kind.Arrow':
        return Kind.Arrow(
            tuple(self.parse_Kind(param) for param in pb.params),
            self.parse_Kind(pb.result))

    def parse_PrimType(self, pb) -> 'PrimType':
        return PrimType(pb)

    def parse_Type(self, pb) -> 'Type':
        sum_name = pb.WhichOneof('Sum')
        if sum_name == 'var':
            return self.parse_Type_Var(pb.var)
        elif sum_name == 'con':
            return self.parse_Type_Con(pb.con)
        elif sum_name == 'prim':
            return Type(prim=self.parse_Type_Prim(pb.prim))
        elif sum_name == 'fun':
            return self.parse_Type_Fun(pb.fun)
        elif sum_name == 'forall':
            return Type(forall=self.parse_Type_Forall(pb.forall))
        elif sum_name == 'struct':
            return Type(tuple=self.parse_Type_Tuple(pb.struct))
        elif sum_name == 'nat':
            return Type(nat=pb.nat)
        else:
            raise ValueError(f'unknown sum type value: {sum_name!r}')

    def parse_Type_Var(self, pb) -> 'Type':
        return Type(var=Type.Var(
            self._resolve_string(pb.var_str, pb.var_interned_str),
            tuple(self.parse_Type(arg) for arg in pb.args)))

    def parse_Type_Con(self, pb) -> 'Type':
        """
        Create a :class:`Type` instance (but may produce something slightly different than the AST
        due to ``Map``/``Optional`` type rewriting).
        """
        tycon = self.parse_TypeConName(pb.tycon)
        args = tuple(self.parse_Type(arg) for arg in pb.args)
        core_type = Type(con=Type.Con(tycon, args))
        return core_type

    def parse_Type_Prim(self, pb) -> 'Type.Prim':
        return Type.Prim(
            self.parse_PrimType(pb.prim),
            tuple(self.parse_Type(arg) for arg in pb.args))

    def parse_Type_Fun(self, pb) -> 'Type':
        """``fun`` has been deprecated and this code path is now replaced with PrimType.ARROW"""
        last_type = self.parse_Type(pb.result)
        for param in reversed(pb.params):
            last_type = Type(prim=Type.Prim(PrimType.ARROW, (self.parse_Type(param), last_type)))
        return last_type

    def parse_Type_Forall(self, pb) -> 'Type.Forall':
        return Type.Forall(
            tuple(self.parse_TypeVarWithKind(var) for var in pb.vars),
            self.parse_Type(pb.body))

    def parse_Type_Tuple(self, pb) -> 'Type.Tuple':
        return Type.Tuple(tuple(self.parse_FieldWithType(field) for field in pb.fields))

    def parse_PrimCon(self, pb) -> 'Optional[PrimCon]':
        if pb is None:
            return None
        elif pb == 0:
            return PrimCon.CON_UNIT
        elif pb == 1:
            return PrimCon.CON_FALSE
        elif pb == 2:
            return PrimCon.CON_TRUE
        else:
            raise ValueError(f'unknown enum value: {pb!r}')

    def parse_BuiltinFunction(self, pb) -> 'Optional[BuiltinFunction]':
        if pb is None:
            return None
        return BuiltinFunction(pb)

    def parse_PrimLit(self, pb) -> 'PrimLit':
        sum_name = pb.WhichOneof('Sum')
        if sum_name == 'int64':
            return PrimLit(int64=pb.int64)
        elif sum_name == 'decimal_str':
            return PrimLit(decimal=pb.decimal_str)
        elif sum_name == 'numeric_interned_str':
            return PrimLit(numeric=self.interned_strings[pb.numeric_interned_str])
        elif sum_name == 'text_str':
            return PrimLit(text=pb.text_str)
        elif sum_name == 'text_interned_str':
            return PrimLit(text=self.interned_strings[pb.text_interned_str])
        elif sum_name == 'timestamp':
            return PrimLit(timestamp=pb.timestamp)
        elif sum_name == 'party_str':
            return PrimLit(party=pb.party_str)
        elif sum_name == 'party_interned_str':
            return PrimLit(party=pb.party_interned_str)
        elif sum_name == 'date':
            return PrimLit(date=pb.date)
        else:
            raise ValueError(f'unknown Sum value: {pb!r}')

    def parse_Expr(self, pb, optional: bool = False) -> 'Expr':
        location = self.parse_Location(pb.location) if pb.HasField('location') else None
        if location is not None:
            args = {'location': location}
        else:
            args = {}

        sum_name = pb.WhichOneof('Sum')
        if optional and sum_name is None:
            return None
        if sum_name == 'var_str':
            args['var'] = pb.var_str
        elif sum_name == 'var_interned_str':
            args['var'] = self.interned_strings[pb.var_interned_str]
        elif sum_name == 'val':
            args['val'] = self.parse_ValName(pb.val)
        elif sum_name == 'builtin':
            args['builtin'] = self.parse_BuiltinFunction(pb.builtin)
        elif sum_name == 'prim_con':
            args['prim_con'] = self.parse_PrimCon(pb.prim_con)
        elif sum_name == 'prim_lit':
            args['prim_lit'] = self.parse_PrimLit(pb.prim_lit)
        elif sum_name == 'rec_con':
            args['rec_con'] = self.parse_Expr_RecCon(pb.rec_con)
        elif sum_name == 'rec_proj':
            args['rec_proj'] = self.parse_Expr_RecProj(pb.rec_proj)
        elif sum_name == 'variant_con':
            args['variant_con'] = self.parse_Expr_VariantCon(pb.variant_con)
        elif sum_name == 'struct_con':
            args['struct_con'] = self.parse_Expr_TupleCon(pb.struct_con)
        elif sum_name == 'enum_con':
            args['enum_con'] = self.parse_Expr_EnumCon(pb.enum_con)
        elif sum_name == 'struct_proj':
            args['struct_proj'] = self.parse_Expr_TupleProj(pb.struct_proj)
        elif sum_name == 'app':
            args['app'] = self.parse_Expr_App(pb.app)
        elif sum_name == 'ty_app':
            args['ty_app'] = self.parse_Expr_TyApp(pb.ty_app)
        elif sum_name == 'abs':
            args['abs'] = self.parse_Expr_Abs(pb.abs)
        elif sum_name == 'ty_abs':
            args['ty_abs'] = self.parse_Expr_TyAbs(pb.ty_abs)
        elif sum_name == 'case':
            args['case'] = self.parse_Case(pb.case)
        elif sum_name == 'let':
            args['let'] = self.parse_Block(pb.let)
        elif sum_name == 'nil':
            args['nil'] = self.parse_Expr_Nil(pb.nil)
        elif sum_name == 'cons':
            args['cons'] = self.parse_Expr_Cons(pb.cons)
        elif sum_name == 'update':
            args['update'] = self.parse_Update(pb.update)
        elif sum_name == 'scenario':
            args['scenario'] = self.parse_Scenario(pb.scenario)
        elif sum_name == 'rec_upd':
            args['rec_upd'] = self.parse_Expr_RecUpd(pb.rec_upd)
        elif sum_name == 'struct_upd':
            args['struct_upd'] = self.parse_Expr_TupleUpd(pb.struct_upd)
        elif sum_name == 'optional_none':
            args['optional_none'] = self.parse_Expr_OptionalNone(pb.optional_none)
        elif sum_name == 'optional_some':
            args['optional_some'] = self.parse_Expr_OptionalSome(pb.optional_some)
        elif sum_name == 'to_any':
            args['to_any'] = self.parse_Expr_ToAny(pb.to_any)
        elif sum_name == 'from_any':
            args['from_any'] = self.parse_Expr_FromAny(pb.from_any)
        elif sum_name == 'to_text_template_id':
            args['to_text_template_id'] = self.parse_Expr_ToTextTemplateId(pb.to_text_template_id)
        elif sum_name == 'type_rep':
            args['type_rep'] = self.parse_Type(pb.type_rep)
        else:
            raise ValueError(f'Unknown type of Expr: {sum_name!r}')

        return Expr(**args)

    def parse_Expr_RecCon(self, pb) -> 'Expr.RecCon':
        return Expr.RecCon(
            self.parse_Type_Con(pb.tycon).con,
            tuple(self.parse_FieldWithExpr(field) for field in pb.fields))  # length > 0

    def parse_Expr_RecProj(self, pb) -> 'Expr.RecProj':
        return Expr.RecProj(
            self.parse_Type_Con(pb.tycon).con,  # Always fully applied
            self._resolve_string(pb.field_str, pb.field_interned_str),
            self.parse_Expr(pb.record))

    def parse_Expr_RecUpd(self, pb) -> 'Expr.RecUpd':
        """Set ``field`` in ``record`` to ``update``."""
        return Expr.RecUpd(
            self.parse_Type_Con(pb.tycon).con,
            self._resolve_string(pb.field_str, pb.field_interned_str),
            self.parse_Expr(pb.record),
            self.parse_Expr(pb.update))

    def parse_Expr_VariantCon(self, pb) -> 'Expr.VariantCon':
        return Expr.VariantCon(
            self.parse_Type_Con(pb.tycon).con,  # Always fully applied
            self._resolve_string(pb.variant_con_str, pb.variant_con_interned_str),
            self.parse_Expr(pb.variant_arg))

    def parse_Expr_TupleCon(self, pb) -> 'Expr.StructCon':
        return Expr.StructCon(
            tuple(self.parse_FieldWithExpr(field) for field in pb.fields))  # length > 0

    def parse_Expr_EnumCon(self, pb) -> 'Expr.EnumCon':
        return Expr.EnumCon(
            self.parse_TypeConName(pb.tycon),
            self._resolve_string(pb.enum_con_str, pb.enum_con_interned_str))

    def parse_Expr_TupleProj(self, pb) -> 'Expr.StructProj':
        return Expr.StructProj(
            self._resolve_string(pb.field_str, pb.field_interned_str),
            self.parse_Expr(pb.struct))

    def parse_Expr_TupleUpd(self, pb) -> 'Expr.StructUpd':
        """Set ``field`` in ``tuple`` to ``update``."""
        return Expr.StructUpd(
            self._resolve_string(pb.field_str, pb.field_interned_str),
            self.parse_Expr(pb.struct),
            self.parse_Expr(pb.update))

    def parse_Expr_App(self, pb) -> 'Expr.App':
        return Expr.App(
            self.parse_Expr(pb.fun),
            tuple(self.parse_Expr(arg) for arg in pb.args))  # length > 0

    def parse_Expr_TyApp(self, pb) -> 'Expr.TyApp':
        return Expr.TyApp(
            self.parse_Expr(pb.expr),
            tuple(self.parse_Type(type) for type in pb.types))  # length > 0

    def parse_Expr_Abs(self, pb):
        return Expr.Abs(
            tuple(self.parse_VarWithType(param) for param in pb.param),  # length > 0
            self.parse_Expr(pb.body))

    def parse_Expr_TyAbs(self, pb):
        return Expr.TyAbs(
            tuple(self.parse_TypeVarWithKind(param) for param in pb.param),  # length > 0
            self.parse_Expr(pb.body))

    def parse_Expr_Nil(self, pb):
        return Expr.Nil(
            self.parse_Type(pb.type))

    def parse_Expr_Cons(self, pb):
        return Expr.Cons(
            self.parse_Type(pb.type),
            tuple(self.parse_Expr(front) for front in pb.front),  # length > 0
            self.parse_Expr(pb.tail))

    def parse_Expr_OptionalNone(self, pb):
        return Expr.OptionalNone(
            self.parse_Type(pb.type))

    def parse_Expr_OptionalSome(self, pb):
        return Expr.OptionalSome(
            self.parse_Type(pb.type),
            self.parse_Expr(pb.body))

    def parse_Expr_ToAny(self, pb):
        return Expr.ToAny(
            self.parse_Type(pb.type),
            self.parse_Expr(pb.expr))

    def parse_Expr_FromAny(self, pb):
        return Expr.FromAny(
            self.parse_Type(pb.type),
            self.parse_Expr(pb.expr))

    def parse_Expr_ToTextTemplateId(self, pb):
        return Expr.ToTextTemplateId(self.parse_Type(pb.type))

    def parse_CaseAlt(self, pb) -> 'CaseAlt':
        body = self.parse_Expr(pb.body)
        sum_name = pb.WhichOneof('Sum')
        if sum_name == 'default':
            return CaseAlt(default=self.parse_Unit(pb.default), body=body)
        elif sum_name == 'variant':
            return CaseAlt(variant=self.parse_CaseAlt_Variant(pb.variant), body=body)
        elif sum_name == 'prim_con':
            return CaseAlt(prim_con=self.parse_PrimCon(pb.prim_con), body=body)
        elif sum_name == 'nil':
            return CaseAlt(nil=self.parse_Unit(pb.nil), body=body)
        elif sum_name == 'cons':
            return CaseAlt(cons=self.parse_CaseAlt_Cons(pb.cons), body=body)
        elif sum_name == 'optional_none':
            return CaseAlt(optional_none=self.parse_Unit(pb.optional_none), body=body)
        elif sum_name == 'optional_some':
            return CaseAlt(optional_some=self.parse_CaseAlt_OptionalSome(pb.optional_some), body=body)
        elif sum_name == 'enum':
            return CaseAlt(enum=self.parse_CaseAlt_Enum(pb.enum), body=body)
        else:
            raise ValueError(f'unknown Sum value: {sum_name!r}')

    def parse_CaseAlt_Variant(self, pb) -> 'CaseAlt.Variant':
        return CaseAlt.Variant(
            self.parse_TypeConName(pb.con),
            self._resolve_string(pb.variant_str, pb.variant_interned_str),
            self._resolve_string(pb.binder_str, pb.binder_interned_str))

    def parse_CaseAlt_Enum(self, pb) -> 'CaseAlt.Enum':
        return CaseAlt.Enum(
            self.parse_TypeConName(pb.con),
            self._resolve_string(pb.constructor_str, pb.constructor_interned_str))

    def parse_CaseAlt_Cons(self, pb) -> 'CaseAlt.Cons':
        return CaseAlt.Cons(
            self._resolve_string(pb.var_head_str, pb.var_head_interned_str),
            self._resolve_string(pb.var_tail_str, pb.var_tail_interned_str))

    def parse_CaseAlt_OptionalSome(self, pb) -> 'CaseAlt.OptionalSome':
        return CaseAlt.OptionalSome(
            self._resolve_string(pb.var_body_str, pb.var_body_interned_str))

    def parse_Case(self, pb) -> 'Case':
        return Case(
            self.parse_Expr(pb.scrut),
            tuple(self.parse_CaseAlt(alt) for alt in pb.alts))

    def parse_Block(self, pb) -> 'Block':
        return Block(
            tuple(self.parse_Binding(binding) for binding in pb.bindings),
            self.parse_Expr(pb.body))

    def parse_Pure(self, pb) -> 'Pure':
        return Pure(
            type=self.parse_Type(pb.type),
            expr=self.parse_Expr(pb.expr))

    def parse_Update(self, pb) -> 'Update':
        sum_name = pb.WhichOneof('Sum')
        if sum_name == 'pure':
            return Update(pure=self.parse_Pure(pb.pure))
        elif sum_name == 'block':
            return Update(block=self.parse_Block(pb.block))
        elif sum_name == 'create':
            return Update(create=self.parse_Update_Create(pb.create))
        elif sum_name == 'exercise':
            return Update(exercise=self.parse_Update_Exercise(pb.exercise))
        elif sum_name == 'fetch':
            return Update(fetch=self.parse_Update_Fetch(pb.fetch))
        elif sum_name == 'get_time':
            return Update(get_time=self.parse_Unit(pb.get_time))
        elif sum_name == 'embed_expr':
            return Update(embed_expr=self.parse_Update_EmbedExpr(pb.embed_expr))
        elif sum_name == 'lookup_by_key':
            return Update(lookup_by_key=self.parse_Update_RetrieveByKey(pb.lookup_by_key))
        elif sum_name == 'fetch_by_key':
            return Update(fetch_by_key=self.parse_Update_RetrieveByKey(pb.fetch_by_key))
        else:
            raise ValueError(f'unknown Sum value: {sum_name!r}')

    def parse_Update_Create(self, pb) -> 'Update.Create':
        return Update.Create(
            template=self.parse_TypeConName(pb.template),
            expr=self.parse_Expr(pb.expr))

    def parse_Update_Exercise(self, pb) -> 'Update.Exercise':
        return Update.Exercise(
            template=self.parse_TypeConName(pb.template),
            choice=self._resolve_string(pb.choice_str, pb.choice_interned_str),
            cid=self.parse_Expr(pb.cid),
            actor=self.parse_Expr(pb.actor, optional=True),
            arg=self.parse_Expr(pb.arg))

    def parse_Update_Fetch(self, pb) -> 'Update.Fetch':
        return Update.Fetch(
            template=self.parse_TypeConName(pb.template),
            cid=self.parse_Expr(pb.cid))

    def parse_Update_EmbedExpr(self, pb) -> 'Update.EmbedExpr':
        return Update.EmbedExpr(
            type=self.parse_Type(pb.type),
            body=self.parse_Expr(pb.body))

    def parse_Update_RetrieveByKey(self, pb) -> 'Update.RetrieveByKey':
        return Update.RetrieveByKey(
            template=self.parse_TypeConName(pb.template),
            key=self.parse_Expr(pb.key))

    def parse_Scenario(self, pb) -> 'Scenario':
        sum_name = pb.WhichOneof('Sum')
        if sum_name == 'pure':
            return Scenario(pure=self.parse_Pure(pb.pure))
        elif sum_name == 'block':
            return Scenario(block=self.parse_Block(pb.block))
        elif sum_name == 'commit':
            return Scenario(commit=self.parse_Scenario_Commit(pb.commit))
        elif sum_name == 'mustFailAt':
            return Scenario(must_fail_at=self.parse_Scenario_Commit(pb.mustFailAt))
        elif sum_name == 'pass':
            return Scenario(must_fail_at=self.parse_Expr(getattr(pb, 'pass')))
        elif sum_name == 'get_time':
            return Scenario(get_time=self.parse_Unit(pb.get_time))
        elif sum_name == 'get_party':
            return Scenario(get_party=self.parse_Expr(pb.get_party))
        elif sum_name == 'embed_expr':
            return Scenario(embed_expr=self.parse_Scenario_EmbedExpr(pb.embed_expr))
        else:
            raise ValueError('unknown Sum value')

    def parse_Scenario_Commit(self, pb) -> 'Scenario.Commit':
        return Scenario.Commit(
            party=self.parse_Expr(pb.party),
            expr=self.parse_Expr(pb.expr),
            ret_type=self.parse_Type(pb.ret_type))

    def parse_Scenario_EmbedExpr(self, pb) -> 'Scenario.EmbedExpr':
        return Scenario.EmbedExpr(
            type=self.parse_Type(pb.type),
            body=self.parse_Expr(pb.body))

    def parse_Location(self, pb) -> 'Location':
        return Location(
            self.parse_ModuleRef(pb.module),
            self.parse_Location_Range(pb.range))

    def parse_Location_Range(self, pb) -> 'Location.Range':
        return Location.Range(
            pb.start_line,
            pb.start_col,
            pb.end_line,
            pb.end_col)

    def parse_TemplateChoice(self, pb) -> 'TemplateChoice':
        return TemplateChoice(
            name=self._resolve_string(pb.name_str, pb.name_interned_str),
            consuming=pb.consuming,
            controllers=self.parse_Expr(pb.controllers),
            arg_binder=self.parse_VarWithType(pb.arg_binder),
            ret_type=self.parse_Type(pb.ret_type),
            update=self.parse_Expr(pb.update),
            self_binder=self._resolve_string(pb.self_binder_str, pb.self_binder_interned_str),
            location=self.parse_Location(pb.location))

    def parse_KeyExpr(self, pb) -> 'KeyExpr':
        if pb.HasField('projections'):
            return KeyExpr(projections=self.parse_KeyExpr_Projections(pb.projections))
        elif pb.HasField('record'):
            return KeyExpr(record=self.parse_KeyExpr_Record(pb.record))
        else:
            raise ValueError(f'unknown KeyExpr {pb}')

    def parse_KeyExpr_Projection(self, pb) -> 'KeyExpr.Projection':
        return KeyExpr.Projection(
            tycon=self.parse_Type_Con(pb.tycon).con,
            field=self._resolve_string(pb.name, pb.interned_id))

    def parse_KeyExpr_Projections(self, pb) -> 'KeyExpr.Projections':
        return KeyExpr.Projections(
            projections=[self.parse_KeyExpr_Projection(p) for p in pb.projections])

    def parse_KeyExpr_RecordField(self, pb) -> 'KeyExpr.RecordField':
        return KeyExpr.RecordField(
            field=self._resolve_string(pb.name, pb.interned_id), expr=pb.expr)

    def parse_KeyExpr_Record(self, pb) -> 'KeyExpr.Record':
        return KeyExpr.Record(
            tycon=self.parse_Type_Con(pb.tycon).con,
            fields=[self.parse_KeyExpr_RecordField(p) for p in pb.fields])

    def parse_DefTemplate(self, pb) -> 'DefTemplate':
        return DefTemplate(
            tycon=self._resolve_dotted_name(pb.tycon_dname, pb.tycon_interned_dname),
            param=self._resolve_string(pb.param_str, pb.param_interned_str),
            precond=self.parse_Expr(pb.precond),
            signatories=self.parse_Expr(pb.signatories),
            agreement=self.parse_Expr(pb.agreement),
            choices=tuple(self.parse_TemplateChoice(choice) for choice in pb.choices),
            observers=self.parse_Expr(pb.observers),
            location=self.parse_Location(pb.location),
            key=self.parse_DefTemplate_DefKey(pb.key) if pb.HasField('key') else None)

    def parse_DefTemplate_DefKey(self, pb) -> 'DefTemplate.DefKey':
        kwargs = dict(
            type=self.parse_Type(pb.type),
            maintainers=self.parse_Expr(pb.maintainers))
        key_expr_name = pb.WhichOneof('key_expr')
        if key_expr_name == 'key':
            kwargs['key'] = self.parse_KeyExpr(pb.key)
        elif key_expr_name == 'complex_key':
            kwargs['complex_key'] = self.parse_Expr(pb.complex_key)
        return DefTemplate.DefKey(**kwargs)

    def parse_DefDataType(self, pb) -> 'DefDataType':
        kwargs = dict(
            name=self._resolve_dotted_name(pb.name_dname, pb.name_interned_dname),
            params=tuple(self.parse_TypeVarWithKind(param) for param in pb.params),
            serializable=pb.serializable,
            location=self.parse_Location(pb.location))
        DataCons_name = pb.WhichOneof('DataCons')
        if DataCons_name == 'record':
            kwargs['record'] = self.parse_DefDataType_Fields(pb.record)
        elif DataCons_name == 'variant':
            kwargs['variant'] = self.parse_DefDataType_Fields(pb.variant)
        elif DataCons_name == 'enum':
            kwargs['enum'] = self.parse_DefDataType_EnumConstructors(pb.enum)
        elif DataCons_name == 'synonym':
            kwargs['synonym'] = self.parse_Type(pb.synonym)
        else:
            raise ValueError(f'unknown DataCons value: {DataCons_name!r}')
        return DefDataType(**kwargs)

    def parse_DefDataType_Fields(self, pb) -> 'DefDataType.Fields':
        return DefDataType.Fields(
            fields=tuple(self.parse_FieldWithType(field) for field in pb.fields))

    def parse_DefDataType_EnumConstructors(self, pb) -> 'DefDataType.EnumConstructors':
        ctors_1 = tuple(pb.constructors_str)
        ctors_2 = tuple(self.interned_strings[idx] for idx in pb.constructors_interned_str)
        return DefDataType.EnumConstructors(constructors=ctors_1 + ctors_2)

    def parse_DefValue(self, pb) -> 'DefValue':
        return DefValue(
            name_with_type=self.parse_DefValue_NameWithType(pb.name_with_type),
            expr=self.parse_Expr(pb.expr),
            no_party_literals=pb.no_party_literals,
            is_test=pb.is_test,
            location=self.parse_Location(pb.location))

    def parse_DefValue_NameWithType(self, pb) -> 'DefValue.NameWithType':
        return DefValue.NameWithType(
            name=self._resolve_string_seq(pb.name_dname, pb.name_interned_dname),
            type=self.parse_Type(pb.type))

    def parse_FeatureFlags(self, pb) -> 'FeatureFlags':
        return FeatureFlags(
          forbidPartyLiterals=pb.forbidPartyLiterals,
          dontDivulgeContractIdsInCreateArguments=pb.dontDivulgeContractIdsInCreateArguments,
          dontDiscloseNonConsumingChoicesToObservers=pb.dontDiscloseNonConsumingChoicesToObservers)

    def parse_Module(self, pb) -> 'Module':
        return Module(
            name=self._resolve_dotted_name(pb.name_dname, pb.name_interned_dname),
            flags=self.parse_FeatureFlags(pb.flags),
            data_types=tuple(self.parse_DefDataType(data_type) for data_type in pb.data_types),
            values=tuple(self.parse_DefValue(value) for value in pb.values),
            templates=tuple(self.parse_DefTemplate(template) for template in pb.templates))

    def parse_Package(self, pb) -> 'Package':
        # TODO: this modifies state in a parser which is less than ideal; a better pattern would be
        #  to create a sub-parser with the contextual state required to understand interned package
        #  IDs
        self.interned_strings.extend(pb.interned_strings)

        indices = [tuple(self.interned_strings[idx] for idx in idn.segments_interned_str)
                   for idn in pb.interned_dotted_names]

        self.interned_dotted_names.extend(indices)

        return Package(modules=tuple(self.parse_Module(module) for module in pb.modules))

    def _resolve_string(self, name: 'Optional[str]', interned_id: 'Optional[int]') -> str:
        return name if name else self.interned_strings[interned_id]

    def _resolve_string_seq(
            self, name: 'Optional[Sequence[str]]', name_interned_id: 'Optional[int]') \
            -> 'Sequence[str]':
        if self.interned_dotted_names:
            return tuple(name) if name else self.interned_dotted_names[name_interned_id]
        else:
            return tuple(name) if name else tuple()

    def _resolve_dotted_name(self, pb_dotted_name, interned_id: 'Optional[int]') -> 'DottedName':
        return DottedName(self._resolve_string_seq(pb_dotted_name.segments, interned_id))
