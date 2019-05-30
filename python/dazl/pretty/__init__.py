# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
:mod:`dazl.pretty` package
==========================

This module contains utilities for pretty-printing various types in dazl.

.. automodule:: dazl.pretty.render_daml
.. automodule:: dazl.pretty.util
"""

from typing import Optional, Type, TYPE_CHECKING

from ._render_base import PrettyPrintBase, pretty_print_syntax
from .options import PrettyOptions
from .render_csharp import CSharpPrettyPrint
from .render_daml import DamlPrettyPrinter, DEFAULT_PRINTER as DAML_PRETTY_PRINTER
from .render_python import PythonPrettyPrint
from .util import maybe_parentheses
from ..model.types_store import PackageStore

if TYPE_CHECKING:
    from .pygments_daml_lexer import DAMLLexer as _DAMLLexer_TYPE


def _import_daml_lexer() -> 'Optional[Type[_DAMLLexer_TYPE]]':
    # pygments isn't absolutely required, but if it's loaded, also provide our lexer
    try:
        from .pygments_daml_lexer import DAMLLexer
        return DAMLLexer
    except ImportError:
        return None


DAMLLexer = _import_daml_lexer()


ALL_PRINTER_TYPES = [CSharpPrettyPrint, DamlPrettyPrinter, PythonPrettyPrint]


# noinspection PyShadowingBuiltins,PyShadowingNames
def get_pretty_printer(format: str, options: 'PrettyOptions', store: 'PackageStore') \
        -> 'Optional[PrettyPrintBase]':
    for printer in ALL_PRINTER_TYPES:
        if printer.syntax.startswith(format):
            return printer(store, options)
    return None
