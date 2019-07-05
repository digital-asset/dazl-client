from ast import NodeTransformer, Name, Bytes, Import, ImportFrom
from pathlib import Path

import shutil
from astor import parse_file, to_source, SourceGenerator
from typing import Iterator, Tuple


from .config import CONFIG

def grpc_rewrite():
    final_dir = CONFIG.directories.final
    if final_dir.exists():
        shutil.rmtree(final_dir)
    final_dir.mkdir(parents=True, exist_ok=True)
    
    for p in CONFIG.directories.pyraw.glob('**/*.py'):
        p_rel = p.relative_to(CONFIG.directories.pyraw)
        print(p_rel)
        if str(p_rel).startswith('da/'):
            generate(p, final_dir, 'da', 'daml.daml_lf')
        if str(p_rel).startswith('com/digitalasset/ledger/api/v1/'):
            generate(p, final_dir, 'com.digitalasset.ledger.api.v1', 'daml.ledger_api.v1')
        else:
            generate(p, final_dir, None, None)
        #generate(p, final_dir, )
        #print(x)


def generate(source_file: Path, dest_root: Path, old_prefix: str, new_prefix: str) -> None:
    #a = parse_file('.cache/py-raw/google/rpc/status_pb2.py')
    source_root = CONFIG.directories.pyraw
    old_prefix = None
    original_ast = parse_file(source_file)

    dest_file_p = source_file.relative_to(source_root)

    rewriter = Rewriter({
        'da': 'daml.daml_lf',
        'com.digitalasset.ledger.api.v1': 'daml.ledger_api.v1',
        'sys': None
    }, dest_file_p.with_suffix(''))
    new_ast = rewriter.visit(original_ast)
    #print(rewriter.non_empty_module)
    if rewriter.non_empty_module:
        new_source_text = to_source(new_ast, indent_with='  ', source_generator_class=PrettySourceGeneratorFactory())
        dest_file: Path = dest_root / dest_file_p
        dest_file.parent.mkdir(parents=True, exist_ok=True)
        dest_file.write_text(new_source_text, 'utf8')


class PrettySourceGenerator(SourceGenerator):
    def visit_Expr(self, node):
        return super().visit_Expr(node)


class PrettySourceGeneratorFactory(SourceGenerator):
    """
    A bit of a dumb wrapper around :class:`PrettySourceGenerator` to work around an astor bug that
    does incorrect type-checking of the ``source_generator_class`` parameter before attempting to
    use it.
    """
    def __init__(self):
        """
        No-argument constructor. Note that this instance of SourceGenerator isn't actually used by
        anything except a type-check inside ``astor.to_source``.
        """
        super().__init__(self, 2)

    def __call__(self, *args, **kwargs):
        return PrettySourceGenerator(*args, **kwargs)


class Rewriter(NodeTransformer):
    """
    Python AST translator that takes what the Protobuf/gRPC compiler emits and performs a few
    modifications:

     * Strip gRPC-generated code altogether where there are no services.
     * Change absolute imports to relative imports for gRPC/Protobuf services within the same
       "family".
     * Remove compatibility with Python 2; there is a small tax associated with keeping this
       compatibility around so why bother.
    """

    non_empty_module = False

    def __init__(self, import_mapping: 'Mapping[str, str]', current_module: str):
        super().__init__()
        self.import_mapping = import_mapping
        self.current_module = current_module

    def visit_Assign(self, node):
        """
        Look for the ``_b`` function and remove it.
        """
        if (len(node.targets) == 1 and isinstance(node.targets[0], Name) and node.targets[0].id == '_b'):
            return None
        else:
            return super().generic_visit(node)

    def visit_Import(self, node):
        """
        Remove the ``sys`` import; it is required by the ``_b`` function which is also removed.
        """
        if len(node.names) == 1 and node.names[0].name == 'sys' and node.names[0].asname is None:
            return None
        return node

    def visit_ImportFrom(self, node: ImportFrom):
        for mod, suffix in import_iter(node.module):
            if mod == self.current_module:
                return ImportFrom(module=suffix, names=node.names, level=1)
            # if mod in self.import_mapping:
            #     new_loc = self.import_mapping[mod]
            #     if new_loc is not None:
            #         return ImportFrom(module=suffix, names=node.names, level=1)
            #     else:
            #         return None
        return node

    def visit_Module(self, node):
        """
        Format the contents of the module to contain copyright notices and be pylint compliant.
        """
        nodes = []
        for body_expr in node.body:
            print(body_expr)
        return self.generic_visit(node, intentional=True)

    def visit_Call(self, node):
        """
        Replace calls to the ``_b`` function with a bytestring constant declaration.
        """
        if isinstance(node.func, Name) and node.func.id == '_b':
            return Bytes(node.args[0].s.encode('latin1'))
        else:
            return super().generic_visit(node)

    def generic_visit(self, node, intentional=False):
        if not intentional:
            #print('------------------------------------------------------------------------------------------')
            #print(node)
            #print('------------------------------------------------------------------------------------------')
            self.non_empty_module = True
        return super().generic_visit(node)


def import_iter(base_module) -> 'Iterator[Tuple[str, str]]':
    rindex = len(base_module)

    yield base_module, None
    while rindex >= 0:
        rindex = base_module.rfind('.', 0, rindex)
        if rindex >= 0:
            yield base_module[0:rindex], base_module[rindex + 1:]
