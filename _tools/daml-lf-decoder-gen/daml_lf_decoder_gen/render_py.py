import io
from collections import defaultdict
from typing import List, Sequence, TextIO, TypeVar, Iterable, Collection

from . import adt


Self = TypeVar('Self')


def render_py(package: 'adt.Package') -> str:
    with io.StringIO() as buf:
        PythonModelRenderer(buf).write_package(package)
        return buf.getvalue()


def render_pyi(package: 'adt.Package') -> str:
    with io.StringIO() as buf:
        PythonModelTypingRenderer(buf).write_package(package)
        return buf.getvalue()


class CodeRenderer:
    def __init__(self, buf: 'TextIO', indent: int = 0):
        self._buf = buf
        self._indent = indent

    def write_package(self, package: 'adt.Package'):
        raise NotImplementedError('write_package must be implemented')

    def write_line(self, code: str = None) -> None:
        if not code:
            self._buf.write("\n")
        else:
            for line in code.splitlines():
                if not line:
                    self._buf.write("\n")
                else:
                    self._buf.write(' ' * (self._indent * 4) + line + "\n")

    def write_member(self, code: str = None) -> None:
        """
        Like :meth:`write_line`, but implies a certain amount of whitespace after the member.
        """
        self.write_line(code)
        self.write_line()
        if self._indent == 0:
            self.write_line()

    def indent(self: Self) -> 'Self':
        return type(self)(self._buf, self._indent + 1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


# region Python renderers

class PythonRendererBase(CodeRenderer):

    def _local_name(self, fqn: str) -> str:
        cmp = fqn.split('.')
        return '.'.join(cmp[self._indent:])

    def write_package(self, package: 'adt.Package'):
        self.write_file_header()
        self.write_type_decls(package.type_declarations)

    def write_file_header(self):
        raise NotImplementedError

    def write_type_decls(self, decls: 'Sequence[adt.TypeDecl]') -> None:
        sorted_decls = defaultdict(list)
        for decl in decls:
            local_name = self._local_name(decl.name)
            if '.' in local_name:
                # This type might need to be physically nested in another type
                pfx, _, _ = local_name.partition('.')
                sorted_decls[pfx].append(decl)
            else:
                sorted_decls[local_name].insert(0, decl)

        for s in sorted_decls.values():
            self.write_type_decl(s[0], s[1:])

    def write_type_decl(self, decl: 'adt.TypeDecl', inner_decls: 'Sequence[adt.TypeDecl]') -> None:
        if isinstance(decl, adt.Product):
            self.write_product(decl, inner_decls)
        elif isinstance(decl, adt.Sum):
            self.write_sum(decl, inner_decls)
        elif isinstance(decl, adt.Enum):
            self.write_enum(decl, inner_decls)
        elif isinstance(decl, adt.TypeSyn):
            self.write_syn(decl, inner_decls)
        else:
            raise ValueError(f'Unknown type declaration: {decl!r}')

    def write_product(self, decl: 'adt.Product', inner_decls: 'Sequence[adt.TypeDecl]') -> None:
        raise NotImplementedError

    def write_sum(self, decl: 'adt.Sum', inner_decls: 'Sequence[adt.TypeDecl]') -> None:
        raise NotImplementedError

    def write_enum(self, decl: 'adt.Enum', inner_decls: 'Sequence[adt.TypeDecl]') -> None:
        raise NotImplementedError

    def write_syn(self, decl: 'adt.TypeSyn', inner_decls: 'Sequence[adt.TypeDecl]') -> None:
        raise NotImplementedError


class PythonModelRenderer(PythonRendererBase):

    def write_file_header(self):
        self.write_member("from enum import Enum as __Enum")
        self.write_line("# Marker object that denotes the absence of a provided kwargs value.")
        self.write_line("_MISSING = object()")
        self.write_line()
        self.write_line()

    def write_product(self, decl: 'adt.Product', inner_decls: 'Sequence[adt.TypeDecl]') -> None:
        """
        Generate Python code for a product type.
        """
        self.write_line(f"class {self._local_name(decl.name)}:  # Product")
        with self.indent() as i:
            i.write_member(_py_docstring(decl.doc))
            i.write_member(_py_slots_decl(_protected_name(f.name) for f in decl.fields))
            i.write_member(_py_init_def(decl.fields))
            for prop in decl.fields:
                i.write_member(_py_adt_property(prop, False, False))
            i._write_setattr_block()

            if inner_decls:
                i.write_type_decls(inner_decls)

    def write_sum(self, decl: 'adt.Sum', inner_decls: 'Sequence[adt.TypeDecl]') -> None:
        """
        Generate Python code for a sum type.
        """
        self.write_line(f"class {self._local_name(decl.name)}:")
        with self.indent() as i:
            # write the constructor
            i.write_member(_py_docstring(decl.doc))
            i.write_member(_py_slots_decl([
                '__ctor', '__value',
                *(_protected_name(field.name)
                  for field in decl.fields
                  if field.name not in decl.cases)]))
            i.write_member(_py_init_def(decl.fields, decl.cases))
            for prop in decl.fields:
                i.write_member(_py_adt_property(prop, prop.name in decl.cases, False))

            # Write the match method
            match_params = ['self']
            with io.StringIO() as fun_body_buf:
                for n, case in enumerate(f for f in decl.fields if f.name in decl.cases):
                    pub_name = _public_name(case.name)
                    match_params.append(pub_name)

                    if n == 0:
                        fun_body_buf.write(f'if self.__ctor == \"{case.name}\":\n')
                    else:
                        fun_body_buf.write(f'elif self.__ctor == \"{case.name}\":\n')
                    fun_body_buf.write(f'    return {pub_name}(self.__value)\n')

                fun_body_buf.write('else:\n')
                fun_body_buf.write('    raise ValueError(f"unknown case: {self.__ctor}")\n')

                i.write_line(f"def match({', '.join(match_params)}):")
                i.indent().write_line(fun_body_buf.getvalue())
                i.write_line()

            i._write_setattr_block()

            i.write_type_decls(inner_decls)

    def write_enum(self, decl: 'adt.Enum', inner_decls: 'Sequence[adt.TypeDecl]') -> None:
        """
        Generate Python code for an enum type.
        """
        self.write_line(f'class {decl.name}(__Enum):')
        with self.indent() as i:
            i.write_member(_py_docstring(decl.doc))
            for value in decl.values:
                i.write_line(f'{value.name} = {value.value}')
        self.write_line()

    def write_syn(self, decl: 'adt.TypeSyn', inner_decls: 'Sequence[adt.TypeDecl]') -> None:
        """
        Write a "fake" type synonym by emulating what the Typing module does.

        This is written as a function instead of using ``typing.NewType`` so that we have a natural
        place to put value validation eventually (we do not currently do much more than the typing
        module does).
        """
        if inner_decls:
            raise ValueError('Cannot generate code where a type synonym has inner declarations')

        local_name = self._local_name(decl.name)
        self.write_line(f"def {local_name}(value):")
        self.write_line("    return value")
        self.write_line()
        if self._indent == 0:
            self.write_line()
        self.write_line(f"{local_name}.__supertype__ = {_render_py_type(decl.type)}")
        self.write_line()
        if self._indent == 0:
            self.write_line()

    def _write_setattr_block(self):
        self.write_line("def __setattr__(self, key, value):")
        with self.indent() as i:
            i.write_line(_py_docstring("Overridden to prevent modifications; this is a read-only type."))
            i.write_line('raise Exception("this object is read-only")')
            i.write_line()


class PythonModelTypingRenderer(PythonRendererBase):

    def write_file_header(self):
        self.write_line("from enum import Enum as __Enum")
        self.write_line("from typing import \\")
        self.write_line("    Callable as __Callable, \\")
        self.write_line("    NewType as __NewType, \\")
        self.write_line("    TypeVar as __TypeVar, \\")
        self.write_line("    overload as __overload")
        self.write_line()
        self.write_line("__T = __TypeVar(\"T\")")
        self.write_line()
        self.write_line()

    def write_product(self, decl: 'adt.Product', inner_decls: 'Sequence[adt.TypeDecl]') -> None:
        self.write_line(f"class {self._local_name(decl.name)}:")
        with self.indent() as i:
            i.write_member(_py_init_def(decl.fields))
            for prop in decl.fields:
                i.write_member(_py_adt_property(prop, False, True))

            if inner_decls:
                i.write_type_decls(inner_decls)

    def write_sum(self, decl: 'adt.Sum', inner_decls: 'Sequence[adt.TypeDecl]') -> None:
        """
        Generate Python code for a sum type.
        """
        self.write_line(f"class {self._local_name(decl.name)}:")

        common_ctor_params = []  # type: List[str]
        case_ctor_params = []  # type: List[str]
        match_params = ['self']  # type: List[str]
        for field in decl.fields:
            pub_name = _public_name(field.name)
            field_type_str_embedded = _render_py_type(field.type, False)
            field_type_str = _render_py_type(field.type, True)
            ctor_param = f"{pub_name}: {field_type_str}"
            if field.name in decl.cases:
                case_ctor_params.append(ctor_param)
                match_params.append(f"{pub_name}: \"__Callable[[{field_type_str_embedded}], __T]\"")
            else:
                common_ctor_params.append(ctor_param)

        with self.indent() as i:
            for case_ctor_param in case_ctor_params:
                ctor_params = ['self', *common_ctor_params, case_ctor_param]
                i.write_line("@__overload")
                i.write_line(f"def __init__({', '.join(ctor_params)}): ...")
                i.write_line()

            for prop in decl.fields:
                case = prop.name in decl.cases
                i.write_line(_py_adt_property(prop, case, True))

            i.write_line(f"def match({', '.join(match_params)}) -> __T: ...")

            i.write_type_decls(inner_decls)

    def write_enum(self, decl: 'adt.Enum', inner_decls: 'Sequence[adt.TypeDecl]') -> None:
        """
        Generate Python code for an enum type.
        """
        self.write_line(f'class {decl.name}(__Enum):')
        with self.indent() as i:
            i.write_member(_py_docstring(decl.doc))
            for value in decl.values:
                i.write_line(f'{value.name} = {value.value}')
        self.write_line()

    def write_syn(self, decl: 'adt.TypeSyn', inner_decls: 'Sequence[adt.TypeDecl]') -> None:
        if inner_decls:
            raise ValueError('Cannot generate code where a type synonym has inner declarations')

        local_name = self._local_name(decl.name)
        self.write_line(f'{local_name} = __NewType("{local_name}", {_render_py_type(decl.type)})')
        self.write_line()


# endregion

# region Python Fragments

def _render_py_type(typ: 'adt.TypeRef', quote: bool = True) -> str:
    if isinstance(typ, adt.SeqType):
        return f'\"Sequence[{_render_py_type(typ.arg, False)}]\"'
    elif isinstance(typ, adt.OptionalType):
        return f'\"Optional[{_render_py_type(typ.arg, False)}]\"'
    elif typ is adt.TYPE_STRING:
        return 'str'
    elif typ is adt.TYPE_BOOL:
        return 'bool'
    elif quote:
        return f'"{typ.name}"'
    else:
        return typ.name


def _protected_name(name):
    return '_' + name


def _public_name(name):
    import keyword
    if keyword.iskeyword(name):
        return name + '_'
    else:
        return name


def _py_init_def(fields: 'Sequence[adt.Field]', cases: 'Collection[str]' = ()):
    slots = ['__ctor', '__value'] if cases else []
    args_params = ['self']
    kwargs_params = []
    ctor_lines = []
    for field in fields:
        pub_name = _public_name(field.name)
        if field.name in cases:
            kwargs_params.append(f"{pub_name} = _MISSING")
            ctor_lines.append(f"if {pub_name} is not _MISSING:")
            ctor_lines.append('    ' + _py_setattr('__ctor', _py_quote(pub_name)))
            ctor_lines.append('    ' + _py_setattr('__value', pub_name))
        else:
            protected_name = _protected_name(field.name)
            slots.append(protected_name)
            args_params.append(pub_name)
            ctor_lines.append(_py_setattr(protected_name, pub_name))

    with io.StringIO() as buf:
        buf.write("def __init__(" + ', '.join(args_params + kwargs_params) + '):\n')
        if ctor_lines:
            for ctor_line in ctor_lines:
                buf.write('    ')
                buf.write(ctor_line)
                buf.write('\n')
        else:
            buf.write('    pass\n')
        return buf.getvalue()


def _py_setattr(attr_name: str, attr_expr: str) -> str:
    return f"object.__setattr__(self, \"{attr_name}\", {attr_expr})"


def _py_slots_decl(attr_names: 'Iterable[str]') -> str:
    count = 0
    with io.StringIO() as buf:
        buf.write("__slots__ = ")
        for field in attr_names:
            if count > 0:
                buf.write(', ')
            count += 1
            buf.write(_py_quote(field))

        if count == 0:
            buf.write('()')
        elif count == 1:
            buf.write(',')

        return buf.getvalue()


_py_quote = repr


def _py_docstring(doc: str) -> str:
    return f'"""\n{doc}\n"""\n' if doc else None


def _py_adt_property(field: 'adt.Field', case: bool, typing: bool) -> str:
    """
    Render a string that represents a :class:`adt.Field` that may or may not represent a case in a
    Sum type, and optionally as it should be rendered in a typing file.

    :param field:
        The :class:`adt.Field` to render a property definition/declaration for.
    :param case:
        ``True`` to render the Python property as a possible value of an enclosing Sum type;
        ``False`` to render this Python property as a simple field.
    :param typing:
        ``True`` to render the Python property as it would exist in a typing file (no body,
        type declarations); ``False`` to render the Python property as it exists in real code
        (actual body, no type declarations).
    """
    pub_name = _public_name(field.name)
    field_type = adt.OptionalType(field.type) if case else field.type

    with io.StringIO() as buf:
        buf.write("@property\n")
        buf.write(f'def {pub_name}(self)')
        if typing:
            buf.write(f" -> " + _render_py_type(field_type) + ": ...\n")
        else:
            buf.write(':\n')
            if docstring := _py_docstring(field.doc):
                for line in docstring.splitlines():
                    buf.write('    ' + line + '\n')
            if case:
                buf.write(f"    return self.__value if self.__ctor == \"{field.name}\" else None\n")
            else:
                buf.write(f"    return self.{_protected_name(field.name)}\n")

        return buf.getvalue()

# endregion
