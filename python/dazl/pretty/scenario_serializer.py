# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Any

from ..damlast.daml_lf_1 import Expr, Scenario, Update, PrimCon, PrimLit, FieldWithExpr, Type as _Type
from ..model.core import ContractId
from ..model.types import RecordType, TemplateChoice, TypeReference, TypeEvaluationContext, UnsupportedType, \
    EnumType, VariantType, TextMapType, ListType, OptionalType, ContractIdType
from ..model.writing import AbstractSerializer

TypeCon = _Type.Con


class ScenarioSerializer(AbstractSerializer[None, Expr]):
    """
    Converter from ledger commands to Scenario AST objects.
    """

    def get_scenario(self) -> Scenario:
        return None

    def serialize_create_command(self, template_type: RecordType, template_args: Expr) -> Update:
        return Update(create=Update.Create(template_type.name, template_args))

    def serialize_exercise_command(
            self, contract_id: ContractId, choice_info: TemplateChoice, choice_args: Expr) \
            -> Update:
        exercise = Update.Exercise(
            template=contract_id.template_id,
            choice=choice_info.name,
            cid=contract_id,
            actor=None,
            arg=choice_args)

        return Update(exercise=exercise)

    def serialize_exercise_by_key_command(self, template_ref: TypeReference, key_arguments: Any,
                                          choice_info: TemplateChoice, choice_arguments: Any) -> Update:
        pass

    def serialize_create_and_exercise_command(self, template_type: RecordType, create_arguments: Any,
                                              choice_info: TemplateChoice, choice_arguments: Any) -> Update:
        pass

    def serialize_unit(self, context: TypeEvaluationContext, obj: Any) -> Expr:
        return Expr(prim_con=PrimCon.CON_UNIT)

    def serialize_bool(self, context: TypeEvaluationContext, obj: Any) -> Expr:
        value = self.type_context.to_boolean(obj)
        return Expr(prim_con=PrimCon.CON_TRUE) if value else Expr(prim_con=PrimCon.CON_FALSE)

    def serialize_text(self, context: TypeEvaluationContext, obj: Any) -> Expr:
        value = self.type_context.to_str(obj)
        return Expr(prim_lit=PrimLit(text=value))

    def serialize_int(self, context: TypeEvaluationContext, obj: Any) -> Expr:
        pass

    def serialize_decimal(self, context: TypeEvaluationContext, obj: Any) -> Expr:
        value = self.type_context.to_decimal(obj)
        return Expr(prim_lit=PrimLit(decimal=str(value)))

    def serialize_party(self, context: TypeEvaluationContext, obj: Any) -> Expr:
        value = self.type_context.to_str(obj)
        return Expr(prim_lit=PrimLit(party=value))

    def serialize_date(self, context: TypeEvaluationContext, obj: Any) -> Expr:
        pass

    def serialize_datetime(self, context: TypeEvaluationContext, obj: Any) -> Expr:
        pass

    def serialize_timedelta(self, context: TypeEvaluationContext, obj: Any) -> Expr:
        pass

    def serialize_contract_id(self, context: TypeEvaluationContext, tt: ContractIdType, obj: Any) -> Expr:
        pass

    def serialize_optional(self, context: TypeEvaluationContext, tt: OptionalType, obj: Any) -> Expr:
        if obj is None:
            return Expr(optional_none=Expr.OptionalNone(tt.type_parameter))
        else:
            value = self._serialize_dispatch(context, tt.type_parameter, obj)
            return Expr(optional_some=Expr.OptionalSome(type=tt.type_parameter, body=value))

    def serialize_list(self, context: TypeEvaluationContext, tt: ListType, obj: Any) -> Expr:
        front = [self._serialize_dispatch(context, tt.type_parameter, item) for item in obj]
        tail = Expr(nil=Expr.Nil(type=tt.type_parameter))
        return Expr(cons=Expr.Cons(type=tt.type_parameter, front=front, tail=tail))

    def serialize_map(self, context: TypeEvaluationContext, tt: TextMapType, obj: Any) -> Expr:
        pass

    def serialize_record(self, context: TypeEvaluationContext, tt: RecordType, obj: Any) -> Expr:
        value = {arg: self._serialize_dispatch(context, arg_type, obj.get(arg)) for arg, arg_type in tt.named_args}
        return Expr(rec_con=Expr.RecCon(TypeCon(tt.name, []), fields=[FieldWithExpr(field, expr) for field, expr in value.items()]))

    def serialize_variant(self, context: TypeEvaluationContext, tt: VariantType, obj: Any) -> Expr:
        pass

    def serialize_enum(self, context: TypeEvaluationContext, tt: EnumType, obj: Any) -> Expr:
        pass

    def serialize_unsupported(self, context: TypeEvaluationContext, tt: UnsupportedType, obj: Any) -> Expr:
        pass
