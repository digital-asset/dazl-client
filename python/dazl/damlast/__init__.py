# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
:mod:`dazl.damast`
==================

The :mod:`dazl.damlast` package contains types and functions for working with Daml-LF Archives.
The types in this module are for dealing with Daml's type system as encoded in Daml-LF; for
encoding and decoding of values, see :mod:`dazl.values`.

:mod:`dazl.damlast.daml_lf_1`:
    The full definition of a Daml-LF Archive.

:mod:`dazl.damlast.daml_types`:
    Convenience functions for constructing Daml :class:`Type` objects.

:mod:`dazl.damlast.lookup`:
    Utilities for quickly resolving names to Daml-LF types/values.

:mod:`dazl.damlast.parse`:
    Functions for parsing a Daml-LF Archive from its Protobuf definition.

:mod:`dazl.damlast.protocols`:
    Protocols (interfaces) for components in this package.

:mod:`dazl.damlast.errors`:
    Subclasses of :class:`Error` that may be thrown by classes in this package.

.. automodule:: dazl.damlast.daml_lf_1

    :members:
.. automodule:: dazl.damlast.daml_types
    :members:
.. automodule:: dazl.damlast.lookup
    :members:
.. automodule:: dazl.damlast.parse
    :members:
.. automodule:: dazl.damlast.errors
.. automodule:: dazl.damlast.protocols

"""

from .daml_lf_1 import TypeConName
from .pkgfile import CachedDarFile, DarFile, get_dar_package_ids
from .visitor import ExprVisitor, IdentityTypeVisitor, ModuleVisitor, PackageVisitor, TypeVisitor
