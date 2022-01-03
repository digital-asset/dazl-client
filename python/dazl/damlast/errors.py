# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Error types
-----------

.. autoclass:: PackageNotFoundError
.. autoclass:: NameNotFoundError
"""

from typing import TYPE_CHECKING, Any

from ..prim import DazlError

if TYPE_CHECKING:
    from . import daml_lf_1

__all__ = ["PackageNotFoundError", "NameNotFoundError"]


class PackageNotFoundError(DazlError):
    """
    Raised when a :class:`Package` was expected but could not be found.

    This error can also be raised in places where types/values are being resolved; it is an
    indication that the operation MAY succeed if the package of the specified ID is fetched and
    the original option retried.
    """

    def __init__(self, ref: "daml_lf_1.PackageRef"):
        super().__init__(ref)
        self.ref = ref


class NameNotFoundError(DazlError):
    """
    Raised when a :class:`daml_lf_1.DefDataType`, :class:`daml_lf_1.DefValue`, or
    :class:`daml_lf_1.DefTemplate` of a specific name was expected, but could not be found.

    Typically this error is raised when the *package ID* is valid, but the name is not. Because
    package IDs are immutable, this error is not normally retryable.
    """

    def __init__(self, ref: "Any"):
        super().__init__(ref)
        self.ref = ref
