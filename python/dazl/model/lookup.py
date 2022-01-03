# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module has been relocated to ``dazl.damlast.lookup``.
"""

from typing import Iterator, Tuple
import warnings

from ..damlast.daml_lf_1 import PackageRef
from ..damlast.lookup import validate_template as _validate_template

__all__ = ["validate_template", "template_reverse_globs"]

warnings.warn(
    "dazl.model.lookup is deprecated; use dazl.damlast.lookup instead.",
    DeprecationWarning,
    stacklevel=2,
)


def validate_template(template) -> "Tuple[PackageRef, str]":
    """
    Return a module and type name component from something that can be interpreted as a template.

    This function is deprecated and will be removed in dazl v8; please use
    ``dazl.damlast.lookup.validate_template`` instead.

    :param template:
        Any object that can be interpreted as an identifier for a template.
    """
    warnings.warn(
        "dazl.model.lookup.validate_template is deprecated and will be removed in dazl v8; "
        "use dazl.damlast.lookup.validate_template instead",
        DeprecationWarning,
        stacklevel=2,
    )

    return _validate_template(template, allow_deprecated_identifiers=True)


def template_reverse_globs(primary_only: bool, package_id: str, type_name: str) -> "Iterator[str]":
    """
    Return an iterator over strings that glob to a specified type.
    """
    # noinspection PyProtectedMember
    from ..client.events import _template_reverse_globs

    warnings.warn(
        "template_reverse_globs is deprecated; use either "
        "dazl.damlast.lookup.matching_normalizations (for template_reverse_globs(False, ...)) or "
        "dazl.damlast.lookup.normalize(for template_reverse_globs(True, ...)). "
        "Note that the new functions do NOT support periods as a delimiter between "
        "module names and entity names; you MUST use a colon.",
        DeprecationWarning,
    )
    return _template_reverse_globs(primary_only, package_id, type_name)
