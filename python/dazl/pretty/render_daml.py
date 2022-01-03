# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# type: ignore

from io import StringIO
from typing import Optional, Sequence, Union

from ..damlast.daml_lf_1 import (
    Block,
    DefDataType,
    DefTemplate,
    Expr,
    ModuleRef,
    PrimType,
    Pure,
    Scenario,
    Type as NewType,
    TypeConName,
    Update,
)
from ..damlast.util import module_name, package_local_name
from ..model.types import (
    SCALAR_TYPE_BOOL,
    SCALAR_TYPE_CHAR,
    SCALAR_TYPE_DATE,
    SCALAR_TYPE_DECIMAL,
    SCALAR_TYPE_INTEGER,
    SCALAR_TYPE_PARTY,
    SCALAR_TYPE_RELTIME,
    SCALAR_TYPE_TEXT,
    SCALAR_TYPE_TIME,
    SCALAR_TYPE_UNIT,
    ContractIdType,
    EnumType,
    ForAllType,
    ListType,
    OptionalType,
    RecordType,
    ScalarType,
    TextMapType,
    Type as OldType,
    TypeApp,
    TypeReference,
    TypeVariable,
    UpdateType,
    VariantType,
    type_dispatch_table,
)
from ._render_base import PrettyPrintBase
from .util import maybe_parentheses

_OldTypePrim = Union[
    ScalarType, ContractIdType, ListType, OptionalType, TextMapType, UpdateType, NewType.Prim
]


class DamlPrettyPrinter(PrettyPrintBase):

    syntax = "daml"

    def lexer(self):
        try:
            from .pygments_daml_lexer import DAMLLexer
        except ImportError:
            return None

        return DAMLLexer()

    def module_indent(self):
        return ""

    def visit_module_ref_start(self, module_ref: "ModuleRef"):
        return f"module {module_name(module_ref)} where\n"

    def visit_def_data_type(self, def_data_type: "DefDataType") -> str:
        return self.visit_def_template(None, def_data_type)

    def visit_def_template(
        self, template: "Optional[DefTemplate]", def_data_type: "DefDataType"
    ) -> str:
        """
        Render a template (or a simple data type).

        :param template:
            The :class:`DefTemplate` to render. If not supplied, only the :class:`DefDataType` is
            rendered.
        :param def_data_type:
            The :class:`DefDataType` to render.
        :return:
            String rendering of the template and/or data type.
        """
        local_name = ".".join(def_data_type.name.segments)

        from ..damlast.expand import ExpandVisitor, SimplifyVisitor

        ex = ExpandVisitor(self.lookup)
        sp = SimplifyVisitor(self.lookup)

        def render(expr: Expr) -> str:
            # return self.visit_expr(expr)
            try:
                e1 = ex.visit_expr(expr)
                e2 = sp.visit_expr(e1)
                return self.visit_expr(e2)
            except:
                return "???"

        with StringIO() as buf:
            if def_data_type.record is not None:
                type_args = "".join(f" {p.var}" for p in def_data_type.params)
                if template is not None:
                    buf.write("template " + local_name)
                else:
                    buf.write(f"data {local_name}{type_args} = {local_name}")
                buf.write("\n  with\n")
                for field in def_data_type.record.fields:
                    buf.write(f"    {field.field}: {self.visit_type(field.type)}\n")
                if template is not None:
                    buf.write("  where\n")
                    buf.write(f"    signatory {render(template.signatories)}\n")
                    buf.write(f"    observer {render(template.observers)}\n")
                    buf.write(f"    ensure {render(template.precond)}\n")
                    buf.write(f"    agreement {render(template.agreement)}\n")
                    # buf.write('    controller')
            elif def_data_type.variant is not None:
                buf.write("data " + local_name + " = ")

            if template is None:
                if def_data_type.serializable:
                    buf.write("\n  deriving (Eq, Show)")

            return buf.getvalue()

    # region visit_expr_* methods

    def visit_expr_prim_con_inline_unit(self):
        return "()"

    def visit_expr_rec_con_decl(self, rec_con: "Expr.RecCon", context: "CodeContext"):
        return self._visit_expr_decl(
            context, self.visit_expr_rec_con_inline(rec_con, line_endings=True)
        )

    def visit_expr_rec_con_inline(self, rec_con: "Expr.RecCon", line_endings: bool = False):
        ctor_expr = f"{self.visit_type_con(rec_con.tycon)} with"
        field_exprs = [f"{fwt.field}={self.visit_expr(fwt.expr)}" for fwt in rec_con.fields]
        if line_endings:
            return ctor_expr + "".join("\n  " + expr for expr in field_exprs)
        else:
            return f'{ctor_expr} {"; ".join(field_exprs)}'

    def visit_expr_rec_proj(self, rec_proj: "Expr.RecProj"):
        rec_text = maybe_parentheses(self.visit_expr(rec_proj.record))
        return f"{rec_text}.{rec_proj.field}"

    def visit_expr_variant_con(self, variant_con: "Expr.VariantCon") -> str:
        arg_text = self.visit_expr(variant_con.variant_arg)
        return f"{variant_con.variant_con} {maybe_parentheses(arg_text)}"

    def visit_expr_struct_proj(self, struct_proj: "Expr.StructProj") -> str:
        tuple_text = maybe_parentheses(self.visit_expr(struct_proj.struct))
        return f"{tuple_text}.{struct_proj.field}"

    def visit_expr_app_inline(self, app: "Expr.App") -> str:
        components = [app.fun, *app.args]
        return " ".join(maybe_parentheses(self.visit_expr(e)) for e in components)

    def visit_expr_abs_decl(self, abs_: "Expr.Abs", context: "CodeContext"):
        local_name = ".".join(context.decl_name)
        field_def = f"{local_name} :: {self.visit_type(context.decl_type)}"
        all_params = [t.var for t in context.type_abs] if context.type_abs is not None else []
        all_params.extend(p.var for p in abs_.param)

        param_text = "".join(" " + p for p in all_params)
        body_text = self.visit_expr(abs_.body)
        field_decl = f"{local_name}{param_text} = {body_text}"
        return f"{field_def}\n{field_decl}"

    def visit_expr_abs_inline(self, abs_: "Expr.Abs"):
        param_text = " ".join(p.var for p in abs_.param)
        body_expr = self.visit_expr(abs_.body)
        return f"(\\{param_text} -> {body_expr})"

    def visit_expr_case(self, case: "Case"):
        scrut_text = maybe_parentheses(self.visit_expr(case.scrut))
        patterns = ["  " + self.visit_expr_casealt(alt) for alt in case.alts]
        lines = [f"case {scrut_text} of"]
        lines.extend(patterns)
        return "\n".join(lines)

    def visit_expr_let(self, let: "Block") -> str:
        binding_lines = [
            f"{binding.binder.var} = {self.visit_expr(binding.bound)}" for binding in let.bindings
        ]
        with StringIO() as buf:
            buf.write("let ")
            delim = ""
            for line in binding_lines:
                buf.write(delim)
                buf.write(line)
                buf.write("\n")
                delim = "    "
            buf.write("in ")
            expr_text = self.visit_expr(let.body)
            buf.write(expr_text)
            return buf.getvalue()

    def visit_expr_nil_inline(self, nil: "Expr.Nil") -> str:
        return "nil"

    def visit_expr_cons(self, cons: "Expr.Cons") -> str:
        front_texts = [self.visit_expr(front) for front in cons.front]
        if cons.tail.nil:
            return "[" + ", ".join(maybe_parentheses(t, ",") for t in front_texts) + "]"

        tail_text = self.visit_expr(cons.tail)
        if len(front_texts) > 1:
            return (
                "["
                + ", ".join(maybe_parentheses(t, ",") for t in front_texts)
                + "] ++ "
                + maybe_parentheses(tail_text)
            )
        else:
            return f"{front_texts[0]} `Cons` {tail_text}"

    def visit_expr_update(self, update: "Update"):
        return update.Sum_match(
            self.visit_expr_update_pure,
            self.visit_expr_update_block,
            self.visit_expr_update_create,
            self.visit_expr_update_exercise,
            self.visit_expr_update_fetch,
            self.visit_expr_update_get_time,
            self.visit_expr_update_lookup_by_key,
            self.visit_expr_update_fetch_by_key,
            self.visit_expr_update_embed_expr,
        )

    def visit_expr_update_pure(self, pure: "Pure") -> str:
        return self._visit_pure(pure)

    def visit_expr_update_block(self, block: "Block") -> str:
        return self._visit_block(block)

    def visit_expr_update_create(self, create: "Update.Create") -> str:
        return f"create " + self.visit_expr(create.expr)

    def visit_expr_update_exercise(self, exercise: "Update.Exercise") -> str:
        return f"exercise " + self.visit_expr(exercise.cid) + self.visit_expr(exercise.arg)

    def visit_expr_update_fetch(self, fetch: "Update.Fetch") -> str:
        return f"fetch " + self.visit_expr(fetch.cid)

    def visit_expr_update_get_time(self, get_time: "Unit") -> str:
        return "getTime"

    def visit_expr_update_lookup_by_key(self, lookup_by_key: "Update.RetrieveByKey") -> str:
        return (
            "lookupByKey @"
            + self.visit_type(lookup_by_key.template)
            + " "
            + self.visit_expr(lookup_by_key.key)
        )

    def visit_expr_update_fetch_by_key(self, fetch_by_key: "Update.RetrieveByKey") -> str:
        return (
            "fetchByKey @"
            + self.visit_type(fetch_by_key.template)
            + " "
            + self.visit_expr(fetch_by_key.key)
        )

    def visit_expr_update_embed_expr(self, embed_expr: "Update.EmbedExpr") -> str:
        return self.visit_expr(embed_expr.body)

    def _visit_pure(self, pure: "Pure") -> str:
        text = self.visit_expr(pure.expr)
        return f"return $ {text}" if " " in text else f"return {text}"

    def _visit_block(self, block: "Block") -> str:
        from .util import indent

        with StringIO() as buf:
            buf.write("do\n")
            for binding in block.bindings:
                buf.write(
                    f"  {binding.binder.var} <- {indent(self.visit_expr(binding.bound), 2).lstrip()}\n"
                )
            for line in self.visit_expr(block.body).splitlines():
                buf.write(f"  {line}\n")
            return buf.getvalue()

    def visit_expr_scenario(self, scenario: "Scenario") -> str:
        return scenario.Sum_match(
            self.visit_expr_scenario_pure,
            self.visit_expr_scenario_block,
            self.visit_expr_scenario_commit,
            self.visit_expr_scenario_must_fail_at,
            self.visit_expr_scenario_pass,
            self.visit_expr_scenario_get_time,
            self.visit_expr_scenario_get_party,
            self.visit_expr_scenario_embed_expr,
        )

    def visit_expr_scenario_pure(self, pure: "Pure") -> str:
        return self._visit_pure(pure)

    def visit_expr_scenario_block(self, block: "Block") -> str:
        return self._visit_block(block)

    def visit_expr_scenario_commit(self, commit: "Scenario.Commit") -> str:
        text = self.visit_expr(commit.expr)
        return f"commit $ {text}" if " " in text else f"commit {text}"

    def visit_expr_scenario_must_fail_at(self, must_fail_at: "Scenario.Commit") -> str:
        text = self.visit_expr(must_fail_at.expr)
        return f"mustFailAt $ {text}" if " " in text else f"mustFailAt {text}"

    def visit_expr_scenario_pass(self, pass_: "Expr") -> str:
        text = self.visit_expr(pass_)
        return f"pass $ {text}" if " " in text else f"pass {text}"

    def visit_expr_scenario_get_time(self, get_time: "Unit") -> str:
        return "getTime"

    def visit_expr_scenario_get_party(self, get_party: "Expr") -> str:
        text = self.visit_expr(get_party)
        return f"getParty $ {text}" if " " in text else f"getParty {text}"

    def visit_expr_scenario_embed_expr(self, embed_expr: "Scenario.EmbedExpr") -> str:
        return self.visit_expr(embed_expr.body)

    def visit_expr_optional_none(self, optional_none: "Expr.OptionalNone") -> str:
        return f"None"

    def visit_expr_optional_some(self, optional_some: "Expr.OptionalSome") -> str:
        expr_text = self.visit_expr(optional_some.body)
        return f"Some {maybe_parentheses(expr_text)}"

    # endregion

    # region visit_type_* methods

    def visit_type(
        self, type: "Union[str, NewType, OldType, TypeConName]", parenthesize: bool = False
    ) -> str:
        from ..damlast.daml_lf_1 import TypeConName
        from ..model.types import TypeReference

        if isinstance(type, str):
            type_str = type
        elif isinstance(type, NewType):
            type_str = type.Sum_match(
                var=self.visit_type_var,
                con=self.visit_type_con,
                prim=self.visit_type_prim,
                forall=self.visit_type_forall,
                struct=self.visit_type_struct,
                nat=self.visit_type_nat,
                syn=self.visit_type_syn,
            )
        elif isinstance(type, UpdateType):
            type_str = self.visit_type_prim(type)
        elif isinstance(type, ForAllType):
            type_str = self.visit_type_forall(type)
        elif isinstance(type, OldType):
            type_str = type_dispatch_table(
                on_type_var=self.visit_type_var,
                on_type_ref=self.visit_type_con,
                on_scalar=self.visit_type_prim,
                on_contract_id=self.visit_type_prim,
                on_list=self.visit_type_prim,
                on_optional=self.visit_type_prim,
                on_text_map=self.visit_type_prim,
                on_record=self.visit_type_con,
                on_variant=self.visit_type_con,
                on_enum=self.visit_type_con,
                on_type_app=self._visit_type_app,
                on_unsupported=repr,
            )(type)
        elif isinstance(type, TypeConName):
            type_str = self.visit_type_con(TypeReference(type))
        else:
            raise TypeError(f"A DAML Type is required here (got {type!r} instead")

        return maybe_parentheses(type_str) if parenthesize else type_str

    def visit_type_var(self, var: "Union[str, TypeVariable, NewType.Var]"):
        if isinstance(var, NewType.Var):
            return self._visit_type_app((var.var, *var.args))
        elif isinstance(var, TypeVariable):
            return var.name
        elif isinstance(var, str):
            return var
        else:
            raise TypeError(f"A DAML Type variable is required here (got {var!r} instead")

    def visit_type_con(
        self, con: "Union[TypeReference, RecordType, VariantType, EnumType, NewType.Con]"
    ) -> str:
        if isinstance(con, TypeReference):
            return package_local_name(con.con)
        elif isinstance(con, (RecordType, VariantType, EnumType)):
            if con.name is None:
                raise ValueError("A named Record, Variant, or Enum type is required here")
            return package_local_name(con.name.con)
        elif isinstance(con, NewType.Con):
            return self._visit_type_app((package_local_name(con.tycon), *con.args))
        else:
            raise TypeError(f"A DAML Type constructor is required here (got {con!r} instead")

    def visit_type_prim(self, prim: "_OldTypePrim") -> str:
        prim_type = prim.prim if isinstance(prim, NewType.Prim) else None

        if PrimType.UNIT == prim_type or SCALAR_TYPE_UNIT == prim:
            return "Unit"
        elif PrimType.BOOL == prim_type or SCALAR_TYPE_BOOL == prim:
            return "Bool"
        elif PrimType.INT64 == prim_type or SCALAR_TYPE_INTEGER == prim:
            return "Int"
        elif PrimType.DECIMAL == prim_type or SCALAR_TYPE_DECIMAL == prim:
            return "Decimal"
        elif PrimType.CHAR == prim_type or SCALAR_TYPE_CHAR == prim:
            return "Char"
        elif PrimType.TEXT == prim_type or SCALAR_TYPE_TEXT == prim:
            return "Text"
        elif PrimType.TIMESTAMP == prim_type or SCALAR_TYPE_TIME == prim:
            return "Time"
        elif PrimType.RELTIME == prim_type or SCALAR_TYPE_RELTIME == prim:
            return "RelTime"
        elif PrimType.PARTY == prim_type or SCALAR_TYPE_PARTY == prim:
            return "Party"

        elif PrimType.LIST == prim_type:
            if len(prim.args) == 0:
                return "List"
            else:
                return f"[{self.visit_type(prim.args[0])}]"
        elif isinstance(prim, ListType):
            return f"[{self.visit_type(prim.type_parameter)}]"

        elif PrimType.UPDATE == prim_type:
            return self._visit_type_app(("Update", *prim.args))
        elif isinstance(prim, UpdateType):
            return self._visit_type_app(("Update", prim.type_parameter))

        elif PrimType.SCENARIO == prim_type:
            return self._visit_type_app(("Scenario", *prim.args))

        elif PrimType.DATE == prim_type or SCALAR_TYPE_DATE == prim:
            return "Date"

        elif PrimType.CONTRACT_ID == prim_type:
            return self._visit_type_app(("ContractId", *prim.args))
        elif isinstance(prim, ContractIdType):
            return self._visit_type_app(("ContractId", prim.type_parameter))

        elif PrimType.OPTIONAL == prim_type:
            return self._visit_type_app(("Optional", *prim.args))
        elif isinstance(prim, OptionalType):
            return self._visit_type_app(("Optional", prim.type_parameter))

        elif PrimType.ARROW == prim_type:
            arrow_operator = " -> "
            return arrow_operator.join(
                maybe_parentheses(self.visit_type(a), arrow_operator) for a in prim.args
            )

        elif PrimType.NUMERIC == prim_type:
            return self._visit_type_app(("Numeric", *prim.args))

        elif PrimType.TEXTMAP == prim_type:
            return self._visit_type_app(("TextMap", *prim.args))

        elif PrimType.GENMAP == prim_type:
            return self._visit_type_app(("Map", *prim.args))

        elif PrimType.TYPE_REP == prim.prim:
            return "???"

        elif PrimType.ANY == prim_type:
            return "Any"

        elif PrimType.ANY_EXCEPTION == prim_type:
            return "AnyException"

        else:
            raise TypeError(f"A DAML Type primitive is required here (got {prim!r} instead")

    def visit_type_forall(self, forall: "Union[ForAllType, NewType.Forall]") -> str:
        if isinstance(forall, NewType.Forall):
            return f'forall {" ".join(self.visit_type_var(v.var) for v in forall.vars)}. {self.visit_type(forall.body)}'
        elif isinstance(forall, ForAllType):
            return (
                f'forall {" ".join(self.visit_type_var(v.var) for v in forall.type_vars)}. '
                f"{self.visit_type(forall.body_type)}"
            )
        else:
            raise TypeError(f"A DAML forall Type is required here (got {forall!r} instead")

    # noinspection PyShadowingBuiltins
    def visit_type_tuple(self, struct: "NewType.Struct") -> str:
        return "(" + ",".join(self.visit_type(t.type) for t in struct.fields) + ")"

    def _visit_type_app(self, types: "Union[TypeApp, Sequence[Union[str, NewType, OldType]]]"):
        if isinstance(types, TypeApp):
            types = (types.body, *types.arguments)

        return " ".join(self.visit_type(c, True) for c in types)

    # endregion


DEFAULT_PRINTER = DamlPrettyPrinter()
