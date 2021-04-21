# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module has been relocated to ``dazl.client.events`` or ``dazl.damlast.lookup``.
"""

from typing import TYPE_CHECKING, Any, Iterator, Tuple, Union
import warnings

__all__ = ["validate_template", "template_reverse_globs"]

if TYPE_CHECKING:
    from ..damlast.daml_lf_1 import PackageRef


def validate_template(template: "Any") -> "Tuple[Union[str, PackageRef], str]":
    from ..damlast.lookup import validate_template as validate_template_new

    warnings.warn(
        "validate_template is deprecated; use dazl.damlast.lookup.validate_template",
        DeprecationWarning,
        stacklevel=2,
    )

    if template == "*" or template is None:
        return "*", "*"

    return validate_template_new(template)


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
