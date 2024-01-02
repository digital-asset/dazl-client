# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
:mod:`dazl.pretty` package
==========================

This module contains utilities for pretty-printing various types in dazl.

"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type

from .util import maybe_parentheses

if TYPE_CHECKING:
    from .pygments_daml_lexer import DAMLLexer as _DAMLLexer_TYPE


__all__ = ["DAMLLexer"]


def _import_daml_lexer() -> "Optional[Type[_DAMLLexer_TYPE]]":
    # pygments isn't absolutely required, but if it's loaded, also provide our lexer
    try:
        from .pygments_daml_lexer import DAMLLexer

        return DAMLLexer
    except ImportError:
        return None


DAMLLexer = _import_daml_lexer()
