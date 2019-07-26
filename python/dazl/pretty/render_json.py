import json
from io import StringIO
from typing import Any, Union

from dazl.damlast.daml_lf_1 import Package
from dazl.model.types import ModuleRef, TypeReference
from dazl.model.types_store import find_dependencies
from dazl.pretty.util import indent
from dazl.util.tools import boundary_iter
from ._render_base import AstVisitor, pretty_print_syntax
from ..damlast.daml_lf_1 import DefDataType, DefTemplate, Expr, Module, Type, PrimType


JsonValue = Any


@pretty_print_syntax('json')
class JsonPrettyPrint(AstVisitor[JsonValue, JsonValue, JsonValue, JsonValue]):

    syntax = 'json'

    def lexer(self):
        try:
            from pygments.lexers.javascript import JavascriptLexer
        except ImportError:
            return None
        return JavascriptLexer()

    def render_store(self) -> str:
        base_dict = {"templates": {}, "definitions": {}}
        base_dict.update()
        for archive in self.store.archives():
            package_dict = self.visit_package(archive.hash, archive.package)
            base_dict['templates'].update(package_dict['templates'])
            base_dict['definitions'].update(package_dict['definitions'])

        required_types = [repr(t) for t in find_dependencies(
            self.store, [TypeReference.parse(template_id) for template_id in base_dict['templates']])]
        print(required_types)

        defs = {key: value for key, value in base_dict['definitions'].items() if key in required_types}

        base_dict['definitions'] = defs

        return _pretty_dump(base_dict)

    def visit_package(self, package_id: str, package: 'Package') -> 'JsonValue':
        package_dict = {"templates": {}, "definitions": {}}
        for module in package.modules:
            module_ref = ModuleRef(package_id=package_id, module_name=module.name.segments)
            module_dict = self.with_module(module_ref).visit_module(module)
            package_dict['templates'].update(module_dict['templates'])
            package_dict['definitions'].update(module_dict['definitions'])
        return package_dict

    def visit_module(self, module: 'Module') -> 'JsonValue':
        def type_name(segments) -> str:
            return '.'.join(self.context.current_module.module_name) + ':' + \
                '.'.join(segments) + '@' + self.context.current_module.package_id

        return dict(
            templates={type_name(template.tycon.segments): self.visit_def_template(template)
                       for template in module.templates},
            definitions={type_name(data_type.name.segments): self.visit_def_data_type(data_type)
                         for data_type in module.data_types})

    def visit_def_data_type(self, data_type: 'DefDataType') -> 'JsonValue':
        if data_type.record:
            return {"record": {fwt.field: self.visit_type(fwt.type) for fwt in data_type.record.fields}}
        elif data_type.variant:
            return {"variant": {fwt.field: self.visit_type(fwt.type) for fwt in data_type.variant.fields}}
        elif data_type.enum:
            return {"enum": data_type.enum.constructors}
        else:
            return {".unknown": {}}

    def visit_def_template(self, template: 'DefTemplate') -> 'JsonValue':
        return {}

    def visit_type_con(self, con: 'Type.Con') -> 'JsonValue':
        ret = dict(con=repr(con.tycon), args=[self.visit_type(arg) for arg in con.args])
        if not ret['args']:
            del ret['args']
        return ret

    def visit_type_prim(self, prim: 'Type.Prim') -> 'JsonValue':
        ret = dict(prim=type_prim_text(prim.prim), args=[self.visit_type(arg) for arg in prim.args])
        if not ret['args']:
            del ret['args']
        return ret

    def visit_type_var(self, var: 'Union[str, Type.Var]') -> 'JsonValue':
        if isinstance(var, Type.Var):
            var = var.var
        return dict(var=var)

    def visit_type_forall(self, forall: 'Type.Forall') -> 'JsonValue':
        return dict(forall=self.visit_type(forall.body), vars=[str(x) for x in forall.vars])

    def visit_type_tuple(self, tuple: 'Type.Tuple') -> 'JsonValue':
        return dict(tuple=[self.visit_type(fwt.type) for fwt in tuple.fields])

    def visit_expr_rec_con_inline(self, rec_con: 'Expr.RecCon') -> 'str':
        pass

    def visit_expr_app_inline(self, app: 'Expr.App') -> str:
        pass

    def visit_expr_abs_inline(self, abs_: 'Expr.Abs') -> str:
        pass

    def visit_expr_nil_inline(self, nil: 'Expr.Nil'):
        pass


def type_prim_text(prim: 'PrimType') -> 'str':
    if prim == PrimType.MAP_GENERIC:
        return 'Map'
    elif prim == PrimType.UNIT:
        return 'Unit'
    elif prim == PrimType.BOOL:
        return 'Bool'
    elif prim == PrimType.INT64:
        return 'Int'
    elif prim == PrimType.DECIMAL:
        return 'Decimal'
    elif prim == PrimType.CHAR or prim == PrimType.TEXT:
        return 'Text'
    elif prim == PrimType.TIMESTAMP:
        return 'Time'
    elif prim == PrimType.RELTIME:
        return 'RelTime'
    elif prim == PrimType.PARTY:
        return 'Party'
    elif prim == PrimType.LIST:
        return 'List'
    elif prim == PrimType.UPDATE:
        return 'Update'
    elif prim == PrimType.SCENARIO:
        return 'Scenario'
    elif prim == PrimType.DATE:
        return 'Date'
    elif prim == PrimType.CONTRACT_ID:
        return 'ContractId'
    elif prim == PrimType.OPTIONAL:
        return 'Optional'
    elif prim == PrimType.ARROW:
        return 'Arrow'
    elif prim == PrimType.MAP:
        return 'TextMap'
    else:
        raise ValueError(f'Unknown PrimType: {prim}')


def _pretty_dump(value: JsonValue) -> str:
    """
    Tries to print JSON output in a slightly more readable format with careful usage of whitespace.
    """
    try:
        with StringIO() as buf:
            buf.write('{\n')
            buf.write('  "templates": ')
            buf.write(indent(json.dumps(value['templates'], indent=2), 2).lstrip())
            buf.write(',\n')
            buf.write('  "definitions": {\n')
            for is_last_def, (key, value) in boundary_iter(value['definitions'].items()):
                buf.write('    "' + key + '": ')
                (ctor, ctor_value), = value.items()
                buf.write('{\"' + ctor + '\":')
                if not ctor_value:
                    buf.write(' {}')
                else:
                    buf.write('\n')
                    for is_last_field, (field, field_value) in boundary_iter(ctor_value.items()):
                        buf.write('      \"' + field + '\": ' + json.dumps(field_value))
                        if is_last_field:
                            buf.write('}')
                        else:
                            buf.write(',\n')
                buf.write('}')
                if not is_last_def:
                    buf.write(',')
                buf.write('\n')

            buf.write('  }\n')
            buf.write('}\n')
            return buf.getvalue()
    except Exception:
        return json.dumps(value, indent=2)
