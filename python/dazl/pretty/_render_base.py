# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import json
from io import StringIO
from typing import Callable, Dict, Optional, Type as TType, Sequence, Union

from .options import PrettyOptions
from .util import maybe_parentheses, is_hidden_module_name
from .. import LOG
from ..damlast.daml_lf_1 import Block, BuiltinFunction, Case, CaseAlt, DefDataType, DefTemplate, \
    Expr, Module, Package, PrimCon, PrimLit, Scenario, Type, TypeVarWithKind, ValName, \
    Update, DefValue, Unit
from ..damlast.util import unpack_arrow_type
from ..damlast.visitor import PackageVisitor, ModuleVisitor, ExprVisitor, TypeVisitor
from ..model.definition import DamlDataType, DamlTemplate
from ..model.types import ModuleRef
from ..model.types_store import PackageStore
from ..util.prim_types import to_date, to_datetime


# noinspection PyMethodMayBeStatic
class PrettyPrintBase(PackageVisitor[str], ModuleVisitor[str], ExprVisitor[str], TypeVisitor[str]):
    """
    Convenience base class for shared code between all pretty-print implementations.
    """

    def __init__(
            self,
            store: 'Optional[PackageStore]' = None,
            context: 'Union[None, CodeContext, PrettyOptions]' = None):
        self.store = store
        if context is None:
            self.context = CodeContext.top_level()
        elif isinstance(context, CodeContext):
            self.context = context
        elif isinstance(context, PrettyOptions):
            self.context = CodeContext.from_options(context)
        else:
            raise TypeError('a CodeContext object required here')

    def lexer(self):
        """
        Return a Pygments lexer that can be used to render the results from this pretty printer,
        or :class:`None` if none are defined or Pygments could not be loaded.
        """
        return None

    def module_indent(self):
        cm = self.context.current_module
        if cm is not None:
            return ' ' * (len(cm.module_name) * 4)
        else:
            return ''

    def render_store(self) -> str:
        """
        Render everything in a :class:`PackageStore`.
        """
        store = self.store
        if store is None:
            raise Exception('cannot render_store because a PackageStore was not provided')

        with StringIO() as buf:
            buf.write('from dazl import create, exercise, module, TemplateMeta, ChoiceMeta\n\n')
            for package in store.packages():
                buf.write(self.visit_package(package))
                buf.write('\n')
            return buf.getvalue()

    def with_module(self, module_ref: 'ModuleRef'):
        return type(self)(store=self.store, context=self.context.with_module(module_ref))

    def with_decl(self, decl_name: Sequence[str], decl_type: Type):
        """
        Return a sub-scoped pretty print visitor under the context of a field with a specified name
        and type.

        :param decl_name: The name of the declaration.
        :param decl_type: The type of the declaration.
        :return: An instance of this type.
        """
        return type(self)(store=self.store, context=self.context.with_decl(decl_name, decl_type))

    def with_type_abs(self, type_abs: 'Sequence[TypeVarWithKind]'):
        return type(self)(store=self.store, context=self.context.with_type_abs(type_abs))

    def with_type_app(self, type_app: 'Sequence[Type]'):
        return type(self)(store=self.store, context=self.context.with_type_app(type_app))

    def with_expression(self):
        return type(self)(store=self.store, context=self.context.with_expression())

    def with_statement_block(self):
        return type(self)(store=self.store, context=self.context.with_statement_block())

    def visit_package(self, package: 'Package') -> 'str':
        """
        Simply render each package as the contents of its constituent models.

        :param package:
            The :class:`Package` of :class:`Module` instances to render.
        :return:
            The string representation of the package, as defined by the string representation of
            each of its modules.
        """
        LOG.info('Printing a package with %d modules:', len(package.modules))
        from ._module_builder import ModuleHierarchy

        module_map = ModuleHierarchy('')
        for module in package.modules:
            if self.context.show_hidden_types or not is_hidden_module_name(module.name.segments):
                module_map.add_module(module)

        lines = []
        for event_kind, ref, module in module_map:
            if event_kind == ModuleHierarchy.START:
                lines.append(self.visit_module_ref_start(ref))
            elif event_kind == ModuleHierarchy.ITEM:
                child = self.with_module(ref)
                indent = child.module_indent()
                module_contents = '\n'.join(indent + line
                                            for line in child.visit_module(module).splitlines())
                lines.append(module_contents or (indent + 'pass'))
            elif event_kind == ModuleHierarchy.END:
                lines.append(self.visit_module_ref_end(ref))

        return '\n'.join(lines)

    def visit_module(self, module: 'Module') -> 'str':
        """
        Attempt to render the contents of a module.

        :param module: The module to render.
        :return: A string that represents the full contents of this module.
        """
        at_least_one = False

        lines = []
        # render raw values
        for value in module.values:
            if self.context.show_hidden_types or not value.name_with_type.name[0].startswith('$'):
                at_least_one = True
                lines.append(self.visit_def_value(value) + '\n\n')

        # now render data (and templates)
        data_types_by_name = {'.'.join(dt.name.segments): dt for dt in module.data_types}
        templates_by_name = {'.'.join(t.tycon.segments): t for t in module.templates}

        bare_data_types = {}
        template_data_types = {}
        for key in sorted({*data_types_by_name.keys(), *templates_by_name.keys()}):
            data_type = data_types_by_name.get(key)
            template = templates_by_name.get(key)
            if template is None:
                bare_data_types[key] = (None, data_type)
            else:
                template_data_types[key] = (template, data_type)

        for template, data_type in (*bare_data_types.values(), *template_data_types.values()):
            if self.context.show_hidden_types or not data_type.name.segments[0].startswith('$'):
                at_least_one = True
                lines.append(self.visit_def_template(template, data_type))
                lines.append('')

        if not at_least_one:
            self.visit_empty_block_body()

        return '\n'.join(lines)

    def visit_empty_block_body(self):
        return ''

    def visit_module_ref_start(self, module_ref: 'ModuleRef') -> 'str':
        """
        Render the "start" of a module.
        """
        return ''

    def visit_module_ref_end(self, module_ref: 'ModuleRef') -> 'str':
        """
        Render the "end" of a module.
        """
        return ''

    def visit_def_data_type(self, def_data_type: 'DefDataType') -> str:
        return self.visit_def_template(None, def_data_type)

    def visit_def_template(
            self, template: 'DefTemplate', def_data_type: 'Optional[DefDataType]' = None) -> str:
        """
        Attempt to render the :class:`DefTemplate`. If this method successfully returns, then the
        corresponding :class:`DefValue` and :class:`DefDataType` objects are skipped.

        :param template: The :class:`DefTemplate` to attempt to render.
        :param def_data_type: The corresponding :class:`DefDataType` for that template (if known).
        :return: A rendered version of the template.
        """
        raise NotImplementedError

    def visit_daml_data_type(self, data_type: DamlDataType) -> str:
        """
        Render the specified data type.

        :param data_type:
        :return:
        """
        raise NotImplementedError

    def visit_daml_template(self, template: DamlTemplate) -> str:
        """
        Render a template instance.
        """
        raise NotImplementedError

    def visit_def_value(self, def_value: 'DefValue') -> str:
        scope = self.with_decl(def_value.name_with_type.name, def_value.name_with_type.type)
        return scope.visit_expr(def_value.expr)

    def visit_expr(self, expr: 'Expr') -> 'str':
        try:
            expr_text = super(PrettyPrintBase, self).visit_expr(expr)
            if expr_text is None:
                LOG.warning('All visit_expr_* methods should return something (expr_%s did not)',
                            expr._Sum_name)
                return self._visit_expr_default()
            else:
                return expr_text
        except:
            LOG.exception('Could not render an expression!')
            return self._visit_expr_default()

    def visit_expr_var(self, var: str) -> 'str':
        """
        Render the variable. The default implementation merely returns the variable, unchanged.

        :param var: The variable to render.
        :return: The rendered value.
        """
        if self.context.decl_name is not None:
            child = self.with_statement_block()
            return child.visit_expr_var_decl(var, self.context)
        else:
            return self.visit_expr_var_inline(var)

    def visit_expr_var_decl(self, var: str, context: 'CodeContext') -> 'str':
        return self._visit_expr_decl(context, self.visit_expr_var_inline(var))

    def visit_expr_var_inline(self, var: str) -> 'str':
        return var

    def visit_expr_val(self, val: 'ValName') -> 'str':
        if self.context.decl_name is not None:
            child = self.with_statement_block()
            return child.visit_expr_val_decl(val, self.context)
        else:
            return self.visit_expr_val_inline(val)

    def visit_expr_val_decl(self, val: 'ValName', context: 'CodeContext') -> 'str':
        return self._visit_expr_decl(context, self.visit_expr_val_inline(val))

    def visit_expr_val_inline(self, val: 'ValName'):
        return val.full_name_unambiguous

    def visit_expr_builtin(self, builtin: 'BuiltinFunction') -> 'str':
        return builtin.name

    def visit_expr_prim_con(self, prim_con: 'PrimCon') -> 'str':
        if self.context.decl_name is not None:
            child = self.with_statement_block()
            return child.visit_expr_prim_con_decl(prim_con, self.context)
        else:
            return self.visit_expr_prim_con_inline(prim_con)

    def visit_expr_prim_con_decl(self, prim_con: 'PrimCon', context: 'CodeContext') -> str:
        return self._visit_expr_decl(context, self.visit_expr_prim_con_inline(prim_con))

    def visit_expr_prim_con_inline(self, prim_con: 'PrimCon') -> 'str':
        if PrimCon.CON_UNIT == prim_con:
            return self.visit_expr_prim_con_inline_unit()
        elif PrimCon.CON_TRUE == prim_con:
            return self.visit_expr_prim_con_inline_true()
        elif PrimCon.CON_FALSE == prim_con:
            return self.visit_expr_prim_con_inline_false()
        else:
            return repr(prim_con)

    def visit_expr_prim_con_inline_true(self) -> 'str':
        return 'True'

    def visit_expr_prim_con_inline_false(self) -> 'str':
        return 'False'

    def visit_expr_prim_con_inline_unit(self) -> 'str':
        return 'Unit'

    def visit_expr_prim_lit(self, prim_lit: 'PrimLit') -> 'str':
        """
        Visit a primitive literal.
        """
        if self.context.decl_name is not None:
            child = self.with_statement_block()
            return child.visit_expr_prim_lit_decl(prim_lit, self.context)
        else:
            return self.visit_expr_prim_lit_inline(prim_lit)

    def visit_expr_prim_lit_decl(self, prim_lit: 'PrimLit', context: 'CodeContext') -> str:
        return self._visit_expr_decl(context, self.visit_expr_prim_lit_inline(prim_lit))

    def visit_expr_prim_lit_inline(self, prim_lit: 'PrimLit') -> str:
        if prim_lit.text is not None:
            return self.visit_expr_prim_lit_inline_text(prim_lit.text)
        elif prim_lit.int64 is not None:
            return self.visit_expr_prim_lit_inline_int64(prim_lit.int64)
        elif prim_lit.party is not None:
            return self.visit_expr_prim_lit_inline_party(prim_lit.party)
        elif prim_lit.decimal is not None:
            return self.visit_expr_prim_lit_inline_decimal(prim_lit.decimal)
        elif prim_lit.date is not None:
            return self.visit_expr_prim_lit_inline_date(prim_lit.date)
        elif prim_lit.timestamp is not None:
            return self.visit_expr_prim_lit_inline_timestamp(prim_lit.timestamp)
        else:
            return repr(prim_lit)

    def visit_expr_prim_lit_inline_decimal(self, decimal: str) -> str:
        """
        Visit a primitive decimal literal. The default implementation merely returns the original
        string that is the specified value, which tends to be a good default in most languages.

        :param decimal: The numeric value to format.
        :return: The text value.
        """
        return decimal

    def visit_expr_prim_lit_inline_int64(self, int64: int) -> str:
        """
        Visit a primitive text literal. The default implementation uses the JSON encoding of the
        specified value, which tends to be a good default in most languages.

        :param int64: The numeric value to format.
        :return: The text value.
        """
        return json.dumps(int64)

    def visit_expr_prim_lit_inline_text(self, text: str) -> str:
        """
        Visit a primitive text literal. The default implementation uses the JSON encoding of the
        specified value, which tends to be a good default in most languages.

        :param text: The text value to format.
        :return: The text value.
        """
        return json.dumps(text)

    def visit_expr_prim_lit_inline_party(self, party: str) -> str:
        """
        Visit a primitive party literal. The default implementation uses the Python repr encoding,
        which formats strings with a single quote.

        :param party: The text value to format.
        :return: The text value, with quotes escaped.
        """
        return repr(party)

    def visit_expr_prim_lit_inline_date(self, date: int) -> str:
        return to_date(date).isoformat()

    def visit_expr_prim_lit_inline_timestamp(self, timestamp: float) -> str:
        return to_datetime(timestamp).isoformat()

    def visit_expr_rec_con(self, rec_con: 'Expr.RecCon') -> 'str':
        if self.context.decl_name is not None:
            child = self.with_statement_block()
            return child.visit_expr_rec_con_decl(rec_con, self.context)
        else:
            return self.visit_expr_rec_con_inline(rec_con)

    def visit_expr_rec_con_decl(self, rec_con: 'Expr.RecCon', context: 'CodeContext') -> 'str':
        expr_text = self.visit_expr_rec_con_inline(rec_con)
        return self._visit_expr_decl(context, expr_text)

    def visit_expr_rec_con_inline(self, rec_con: 'Expr.RecCon') -> 'str':
        raise NotImplementedError

    def visit_expr_rec_proj(self, rec_proj: 'Expr.RecProj') -> 'str':
        pass

    def visit_expr_enum_con(self, enum_con: 'Expr.EnumCon') -> 'str':
        return enum_con.enum_con

    def visit_expr_variant_con(self, variant_con: 'Expr.VariantCon') -> 'str':
        pass

    def visit_expr_struct_con(self, struct_con: 'Expr.StructCon') -> 'str':
        pass

    def visit_expr_struct_proj(self, struct_proj: 'Expr.StructProj') -> 'str':
        pass

    def visit_expr_app(self, app: 'Expr.App') -> 'str':
        """
        Visit an application (function called with one or more arguments).
        """
        if self.context.decl_name is not None:
            child = self.with_statement_block()
            return child.visit_expr_app_decl(app, self.context)
        else:
            return self.visit_expr_app_inline(app)

    def visit_expr_app_decl(self, app: 'Expr.App', context: 'CodeContext'):
        """
        Visit the declaration of a field whose value is the application of a function with one or
        more parameters. The default implementation assumes that the declaration is identical to the
        inline case.

        :param app:
            The :class:`Expr.App` that is the value of the declaration.
        :param context:
            The _enclosing_ (not the current) context, which includes information about the name and
            type of the declaration.
        :return:
            A string that represents the definition of a value with the name specified by context.
        """
        expr_text = self.visit_expr_app_inline(app)
        return self._visit_expr_decl(context, expr_text)

    def visit_expr_app_inline(self, app: 'Expr.App') -> str:
        """
        Visit an application used in the middle of an expression.
        """
        raise NotImplementedError('visit_expr_app_inline needs an implementation')

    def visit_expr_ty_app(self, ty_app: 'Expr.TyApp') -> 'str':
        """
        Visit the application of a type parameter with a body parameterized on type.

        The default implementation merely creates a child context with type arguments applied, and
        renders the body of the expression at that child context.

        :param ty_app:
            The :class:`Expr.TypeApp` to render.
        :return:
            A string that represents the :class:`Expr.TypeApp`.
        """
        return self.with_type_app(ty_app.types).visit_expr(ty_app.expr)

    def visit_expr_abs(self, abs_: 'Expr.Abs') -> 'str':
        """
        Visit an abstraction (function).
        """
        if self.context.decl_name is not None:
            child = self.with_statement_block()
            return child.visit_expr_abs_decl(abs_, self.context)
        else:
            return self.visit_expr_abs_inline(abs_)

    def visit_expr_abs_decl(self, abs_: 'Expr.Abs', context: 'CodeContext'):
        """
        Visit the declaration of an abstraction (function). The default implementation assumes that
        function declarations are identical to the inline case (which is not normally the case in
        most languages, but many support this as an alternate syntax).

        :param abs_:
            The :class:`Expr.Abs` that is the value of the declaration.
        :param context:
            The _enclosing_ (not the current) context, which includes information about the name and
            type of the declaration.
        :return:
            A string that represents the definition of a value with the name specified by context.
        """
        expr_text = self.visit_expr_abs_inline(abs_)
        return self._visit_expr_decl(context, expr_text)

    def visit_expr_abs_decl_eq(self, abs_: 'Expr.Abs', context: 'CodeContext'):
        """
        Visit the declaration of an abstraction (function) that is the implementation of the
        equality check in the ``GHC.Classes.Eq`` typeclass.

        This is special-cased because in almost all languages, special syntax is required to
        overload equality.

        :param abs_:
            The :class:`Expr.Abs` that is the value of the declaration.
        :param context:
            The _enclosing_ (not the current) context, which includes information about the name and
            type of the declaration.
        :return:
            A string that represents the definition of a value with the name specified by context.
        """
        expr_text = self.visit_expr_abs_inline(abs_)
        return self._visit_expr_decl(context, expr_text)

    def visit_expr_abs_decl_ne(self, abs_: 'Expr.Abs', context: 'CodeContext'):
        """
        Visit the declaration of an abstraction (function) that is the implementation of the
        equality check in the ``GHC.Classes.Eq`` typeclass.

        This is special-cased because in almost all languages, special syntax is required to
        overload inequality.

        :param abs_:
            The :class:`Expr.Abs` that is the value of the declaration.
        :param context:
            The _enclosing_ (not the current) context, which includes information about the name and
            type of the declaration.
        :return:
            A string that represents the definition of a value with the name specified by context.
        """
        expr_text = self.visit_expr_abs_inline(abs_)
        return self._visit_expr_decl(context, expr_text)

    def visit_expr_abs_inline(self, abs_: 'Expr.Abs') -> str:
        """
        Visit an inline function used in the middle of an expression.
        """
        raise NotImplementedError('visit_expr_abs_inline needs an implementation')

    def visit_expr_ty_abs(self, ty_abs: 'Expr.TyAbs') -> 'str':
        """
        Visit the abstraction of a type parameter with a body parameterized on type.

        The default implementation merely creates a child context with type arguments applied, and
        renders the body of the expression at that child context.

        :param ty_abs:
            The :class:`Expr.TypeAbs` to render.
        :return:
            A string that represents the :class:`Expr.TypeAbs`.
        """
        return self.with_type_abs(ty_abs.param).visit_expr(ty_abs.body)

    def visit_expr_case(self, case: 'Case') -> 'str':
        return None

    def visit_expr_casealt(self, alt: 'CaseAlt', type: 'Optional[Type]' = None) -> str:
        pattern_text = alt.Sum_match(
            self.visit_expr_casealt_default,
            self.visit_expr_casealt_variant,
            self.visit_expr_casealt_prim_con,
            self.visit_expr_casealt_nil,
            self.visit_expr_casealt_cons,
            self.visit_expr_casealt_optional_none,
            self.visit_expr_casealt_optional_some,
            self.visit_expr_casealt_enum)
        body_text = self.visit_expr(alt.body)
        return self._visit_expr_casealt(pattern_text, body_text)

    def _visit_expr_casealt(self, pattern_text: str, body_text: str) -> str:
        return f'{pattern_text} -> {maybe_parentheses(body_text)}'

    def visit_expr_casealt_default(self, default: 'Unit'):
        return '_'

    def visit_expr_casealt_variant(self, variant: 'CaseAlt.Variant'):
        var_con = Expr.VariantCon(
            # TODO: Probably not correct
            tycon=Type.Con(tycon=variant.con, args=()),
            variant_con=variant.variant,
            variant_arg=Expr(var=variant.binder))
        return self.visit_expr_variant_con(var_con)

    def visit_expr_casealt_prim_con(self, prim_con: 'PrimCon'):
        return self.visit_expr_prim_con(prim_con)

    def visit_expr_casealt_nil(self, nil: 'Unit', type: 'Optional[Type]' = None):
        return self.visit_expr_nil(Expr.Nil(type))

    def visit_expr_casealt_cons(self, cons: 'CaseAlt.Cons', type: 'Optional[Type]' = None):
        return self.visit_expr_cons(Expr.Cons(
            front=(Expr(var=cons.var_head),),
            tail=Expr(var=cons.var_tail),
            type=type))

    def visit_expr_casealt_optional_none(self, optional_none: 'Unit', type: 'Optional[Type]' = None):
        return self.visit_expr_optional_none(Expr.OptionalNone(type=type))

    def visit_expr_casealt_optional_some(self, optional_some: 'CaseAlt.OptionalSome', type: 'Optional[Type]' = None):
        return self.visit_expr_optional_some(Expr.OptionalSome(type=type, body=Expr(var=optional_some.var_body)))

    def visit_expr_casealt_enum(self, enum: 'CaseAlt.Enum'):
        return self.visit_expr_enum_con(Expr.EnumCon(enum.con, enum.constructor))

    def visit_expr_let(self, let: 'Block') -> 'str':
        pass

    def visit_expr_nil(self, nil: 'Expr.Nil') -> 'str':
        if self.context.decl_name is not None:
            child = self.with_statement_block()
            return child.visit_expr_nil_decl(nil, self.context)
        else:
            return self.visit_expr_nil_inline(nil)

    def visit_expr_nil_decl(self, nil: 'Expr.Nil', context: 'CodeContext') -> str:
        expr_text = self.visit_expr_nil_inline(nil)
        return self._visit_expr_decl(context, expr_text)

    def visit_expr_nil_inline(self, nil: 'Expr.Nil'):
        raise NotImplementedError

    def visit_expr_cons(self, cons: 'Expr.Cons') -> 'str':
        pass

    def visit_expr_update(self, update: 'Update') -> 'str':
        pass

    def visit_expr_scenario(self, scenario: 'Scenario') -> 'str':
        pass

    def visit_expr_rec_upd(self, rec_upd: 'Expr.RecUpd') -> 'str':
        pass

    def visit_expr_struct_upd(self, struct_upd: 'Expr.StructUpd') -> 'str':
        pass

    def visit_expr_optional_none(self, optional_none: 'Expr.OptionalNone') -> 'str':
        pass

    def visit_expr_optional_some(self, optional_some: 'Expr.OptionalSome') -> 'str':
        pass

    # noinspection PyBroadException
    def visit_type(self, type: 'Type') -> 'str':
        """
        Return the string representation of the :class:`Type`, or ``var`` if it could not be
        computed. This implementation tries very hard to not fail.
        """
        default_type = self._visit_type_default()
        try:
            unpacked_types = []

            for unpacked_type in unpack_arrow_type(type):
                try:
                    type_str = super(PrettyPrintBase, self).visit_type(unpacked_type)
                except:  # noqa
                    LOG.exception('Failed to render a Type!')
                    type_str = None
                unpacked_types.append(type_str if type_str is not None else default_type)
            if len(unpacked_types) == 1:
                ret = unpacked_types[0]
            else:
                ret = self._visit_type_function(unpacked_types[0:-1], unpacked_types[-1])
            return ret if ret is not None else default_type
        except:  # noqa
            LOG.exception('Failed to render a Type!')
            return default_type

    def visit_type_var(self, var: 'Union[str, Type.Var]') -> 'str':
        """
        Render a type variable. The default implementation simply returns the original type
        variable.

        :param var: The :class:`Type.Var` to unpack, or a simple string.
        :return: The rendering of this type variable.
        """
        if isinstance(var, Type.Var):
            return var.var
        elif isinstance(var, str):
            return var
        else:
            raise TypeError('visit_type_var(...) expects either a Type.Var or a str')

    def visit_type_con(self, con: 'Type.Con') -> 'str':
        pass

    def visit_type_prim(self, prim: 'Type.Prim') -> 'str':
        pass

    def visit_type_forall(self, forall: 'Type.Forall') -> 'str':
        pass

    def visit_type_tuple(self, tuple: 'Type.Tuple') -> 'str':
        pass

    def visit_type_nat(self, nat: int) -> 'str':
        return str(nat)

    def _visit_type_function(self, arguments: 'Sequence[Type]', return_type: 'Type') -> str:
        """
        Render a function type with the specified arguments and return type.

        :param arguments:
            Arguments to the function type.
        :param return_type:
            The return type of the function.
        :return:
            A string that represents successive type abstractions that, themselves, either return
            further abstractions or a fully applied value.
        """

    def _visit_expr_default(self) -> str:
        """
        Overridden to return a string to use when failing to render an expression.
        """
        return '...'

    def _visit_expr_decl(self, context, expr_text):
        """
        Visit the declaration of a field whose value is specified by a textual string. The default
        implementation simply returns a string of the format ``<name> = <value>``, which happens to
        be the correct implementation in almost all languages.

        :param context:
            The _enclosing_ (not the current) context, which includes information about the name and
            type of the declaration.
        :param expr_text:
            The text to use as the value of the expression.
        :return:
            A string that represents the definition of a value with the name specified by context.
        """
        local_name = '.'.join(context.decl_name)
        return f'{local_name} = {expr_text}'

    def _visit_type_default(self) -> str:
        """
        Overridden to return a string to use when failing to render a type.
        """
        return '...'


class CodeContext:
    """
    The context for evaluating a pretty-print expression.
    """

    @classmethod
    def top_level(cls) -> 'CodeContext':
        return cls()

    @classmethod
    def from_options(cls, context):
        return cls(show_hidden_types=context.show_hidden_types)

    def __init__(
            self,
            *,
            in_expression: bool = False,
            show_hidden_types: bool = False,
            current_module: Optional[ModuleRef] = None,
            decl_name: Optional[Sequence[str]] = None,
            decl_type: Optional[Type] = None,
            type_abs: Optional[Sequence[TypeVarWithKind]] = None,
            type_app: Optional[Sequence[Type]] = None):
        self.in_expression = in_expression
        self.show_hidden_types = show_hidden_types
        self.current_module = current_module
        self.decl_name = decl_name
        self.decl_type = decl_type
        self.type_abs = type_abs
        self.type_app = type_app

    def with_module(self, module: ModuleRef) -> 'CodeContext':
        if self.decl_name is not None or self.decl_type is not None or self.type_abs is not None \
                or self.type_app is not None:
            raise RuntimeError('Cannot declare a module inside a declaration')
        return CodeContext(
            in_expression=False,
            show_hidden_types=self.show_hidden_types,
            current_module=module,
            decl_name=None,
            decl_type=None,
            type_abs=None,
            type_app=None)

    def with_decl(self, decl_name: Sequence[str], decl_type: 'Type') -> 'CodeContext':
        return CodeContext(
            in_expression=False,
            show_hidden_types=self.show_hidden_types,
            current_module=self.current_module,
            decl_name=decl_name,
            decl_type=decl_type,
            type_abs=self.type_abs,
            type_app=self.type_app)

    def with_type_abs(self, type_abs: Optional[Sequence[TypeVarWithKind]]):
        return CodeContext(
            in_expression=self.in_expression,
            show_hidden_types=self.show_hidden_types,
            current_module=self.current_module,
            decl_name=self.decl_name,
            decl_type=self.decl_type,
            type_abs=(self.type_abs or ()) + tuple(type_abs),
            type_app=self.type_app)
        pass

    def with_type_app(self, type_app: 'Optional[Sequence[Type]]'):
        return CodeContext(
            in_expression=True,
            show_hidden_types=self.show_hidden_types,
            current_module=self.current_module,
            decl_name=None,
            decl_type=None,
            type_abs=None,
            type_app=(self.type_app or ()) + tuple(type_app))

    def with_expression(self):
        return CodeContext(
            in_expression=True,
            show_hidden_types=self.show_hidden_types,
            current_module=self.current_module,
            decl_name=None,
            decl_type=None,
            type_abs=None,
            type_app=None)

    def with_statement_block(self):
        return CodeContext(
            in_expression=False,
            show_hidden_types=self.show_hidden_types,
            current_module=self.current_module,
            decl_name=None,
            decl_type=None,
            type_abs=None,
            type_app=self.type_app)


def decode_special_chars(pp: str) -> str:
    return pp.replace('$u002b', '+').replace('$u005b', '[').replace('$u005d', ']'). \
        replace('$u003c', '<').replace('$u003e', '>').replace('$u003a', ':'). \
        replace('$u0022', '"').replace('$u0028', '(').replace('$u0029', ')'). \
        replace('$u002f', '/').replace('$u002c', ',').replace('$u003d', '='). \
        replace('$u002a', '*')


class _PrettyPrinters:
    """
    Holder for
    """

    def __init__(self):
        self._printers = {}  # type: Dict[str, TType[PrettyPrintBase]]

    # noinspection PyShadowingBuiltins
    def register(self, format: str, pp_type: 'TType[PrettyPrintBase]') -> None:
        self._printers[format] = pp_type

    # noinspection PyShadowingBuiltins
    def get(self, format: str) -> 'TType[PrettyPrintBase]':
        for key, format_type in self._printers.items():
            if key.startswith(format):
                return format_type


_PRETTY_PRINTERS = _PrettyPrinters()

get_pretty_printer_type = _PRETTY_PRINTERS.get
register_pretty_printer = _PRETTY_PRINTERS.register


def pretty_print_syntax(fmt: str) -> 'Callable[[TType[PrettyPrintBase]], TType[PrettyPrintBase]]':
    def impl(pp):
        register_pretty_printer(fmt, pp)
        return pp

    return impl
