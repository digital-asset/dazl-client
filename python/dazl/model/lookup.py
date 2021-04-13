# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains the logic for fuzzy lookups (specifically, template references) are performed
in dazl.
"""
from typing import Any, Iterator, Tuple, Union
import warnings

from ..damlast.daml_lf_1 import PackageRef


def validate_template(template: "Any") -> "Tuple[Union[str, PackageRef], str]":
    warnings.warn(
        "validate_template is deprecated; use dazl.damlast.lookup.validate_template",
        DeprecationWarning,
        stacklevel=2,
    )
    from ..damlast.lookup import validate_template as validate_template_new

    if template == "*" or template is None:
        return "*", "*"

    return validate_template_new(template, allow_deprecated_identifiers=True)


def template_reverse_globs(primary_only: bool, package_id: str, type_name: str) -> "Iterator[str]":
    """
    Return an iterator over strings that glob to a specified type.
    """
    package_id = package_id or "*"
    type_name = type_name or "*"

    if package_id != "*":
        if type_name != "*":
            if ":" not in type_name:
                # this is a historical use of template name here; assume the last dot was supposed
                # to have been a colon instead
                m, delim, e = type_name.rpartition(".")
                if delim:
                    yield f"{package_id}:{m}:{e}"
                    if primary_only:
                        return
            yield f"{package_id}:{type_name}"
            if primary_only:
                return
        if not primary_only or type_name == "*":
            yield f"{package_id}:*"
    if type_name != "*":
        if ":" not in type_name:
            # this is a historical use of template name here; assume the last dot was supposed
            # to have been a colon instead
            m, delim, e = type_name.rpartition(".")
            if delim:
                yield f"*:{m}:{e}"
                if primary_only:
                    return
        yield f"*:{type_name}"
        if primary_only:
            return
    yield "*:*"
