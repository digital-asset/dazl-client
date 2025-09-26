# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Error types
-----------

.. autoclass:: PackageNotFoundError
.. autoclass:: NameNotFoundError
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ..prim import DazlError

if TYPE_CHECKING:
    from . import daml_lf_1

__all__ = ["PackageNotFoundError", "NameNotFoundError", "AmbiguousMatchError"]


class PackageNotFoundError(DazlError):
    """
    Raised when a :class:`Package` was expected but could not be found.

    This error can also be raised in places where types/values are being resolved; it is an
    indication that the operation MAY succeed if the package of the specified ID is fetched and
    the original option retried.
    """

    def __init__(self, ref: daml_lf_1.PackageRef) -> None:
        super().__init__(ref)
        self.ref = ref

    def __repr__(self):
        return f"PackageNotFoundError({self.ref})"


class NameNotFoundError(DazlError):
    """
    Raised when a :class:`daml_lf_1.DefDataType`, :class:`daml_lf_1.DefValue`, :class:`daml_lf_1.DefTemplate`, or :class:`daml_lf_1.DefInterface` of a specific name was expected, but could not be found.

    Typically this error is raised when the *package ID* is valid, but the name is not. Because
    package IDs are immutable, this error is not normally retryable.
    """

    def __init__(self, ref: Any) -> None:
        super().__init__(ref)
        self.ref = ref


class AmbiguousMatchError(DazlError):
    """
    Raised when a _single_ :class:`daml_lf_1.DefDataType`, :class:`daml_lf_1.DefValue`, :class:`daml_lf_1.DefTemplate`, or :class:`daml_lf_1.DefInterface` of a specific name was expected, but multiple matches were found.
    """
