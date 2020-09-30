# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
:mod:`dazl.damast` package
==========================

The :mod:`dazl.damlast` module contains types and functions for working with DAML-LF Archives.
The types in this module are for dealing with DAML's type system as encoded in DAML-LF; for
encoding and decoding of values, see :mod:`dazl.values`.

:mod:`dazl.damlast.daml_lf_1`:
    The full definition of a DAML-LF Archive.

:mod:`dazl.damlast.daml_types`:
    Convenience functions for constructing DAML :class:`Type` objects.

:mod:`dazl.damlast.parse`:
    Functions for parsing a DAML-LF Archive from its Protobuf definition.

.. automodule:: dazl.damlast.daml_lf_1
    :members:
.. automodule:: dazl.damlast.daml_types
    :members:
.. automodule:: dazl.damlast.parse
    :members:
"""

from .visitor import PackageVisitor, ModuleVisitor, ExprVisitor, TypeVisitor, IdentityTypeVisitor
