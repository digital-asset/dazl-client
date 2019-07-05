from ast import NodeTransformer, Name, Bytes
from pathlib import Path

from astor import parse_file, to_source, SourceGenerator


def generate(source_file: Path, dest_root: Path, old_prefix: str, new_prefix: str) -> None:
    #a = parse_file('.cache/py-raw/google/rpc/status_pb2.py')
    source_root = 
    old_prefix = 
    original_ast = parse_file(source_file)

    rewriter = Rewriter()
    new_ast = rewriter.visit(original_ast)
    #print(rewriter.non_empty_module)
    if rewriter.non_empty_module:
        new_source_text = to_source(new_ast, source_generator_class=PrettySourceGeneratorFactory())
        dest_root / .write_text(new_source_text)


class PrettySourceGenerator(SourceGenerator):
    def visit_Expr(self, node):
        self.newline(extra=1)
        super().visit_Expr(node)


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
        super().__init__(self, 4)

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

    def visit_ImportFrom(self, node):
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
