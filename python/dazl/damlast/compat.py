# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Compatibility methods
---------------------

These functions should only be used internally by code that is helping in the transition from the
deprecated :class:`dazl.model.types.Type` hierarchy to :class:`dazl.damlast.daml_lf_1.Type`.
These functions will be removed WITHOUT an intermediate deprecation warning, as they are considered
internal only.
"""
from typing import TYPE_CHECKING, Tuple, Union
import warnings

from .daml_lf_1 import TypeConName

if TYPE_CHECKING:
    # avoid import cycles; `dazl.model` should depend on `dazl.damlast`, and not the other way
    # around
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        from ..model.types import Type as DeprecatedType, TypeReference as DeprecatedTypeReference


def parse_template(
    template_id: "Union[str, DeprecatedType, TypeConName]",
) -> "Tuple[TypeConName, DeprecatedTypeReference]":
    """
    Return both the "new-style" Type and the "old-style" Type for _either_ a string, "new-style"
    Type, or "old-style" Type. This is used in places where we can't easily mark a symbol as
    deprecated (particularly, constructors for types that are NOT to be deprecated as part of this
    transition).
    """
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        from ..model.types import (
            Type as DeprecatedType,
            TypeReference as DeprecatedTypeReference,
            UnresolvedTypeReference,
            RecordType,
        )
    from ..damlast.lookup import parse_type_con_name

    if isinstance(template_id, str):
        name = parse_type_con_name(template_id, allow_deprecated_identifiers=True)
        return name, DeprecatedTypeReference(name)

    elif isinstance(template_id, TypeConName):
        return template_id, DeprecatedTypeReference(template_id)

    elif isinstance(template_id, DeprecatedType):
        warnings.warn(
            "usage of dazl.model.types.Type is deprecated; use TypeConName instead",
            DeprecationWarning,
            stacklevel=3,
        )

        if isinstance(template_id, DeprecatedTypeReference):
            return template_id.con, template_id

        elif isinstance(template_id, UnresolvedTypeReference):
            name = parse_type_con_name(template_id.name, allow_deprecated_identifiers=True)
            return name, DeprecatedTypeReference(name)

        elif isinstance(template_id, RecordType):
            if template_id.name is None:
                raise ValueError(
                    "template_id must point to a named record that corresponds to a template"
                )

            return template_id.name.con, DeprecatedTypeReference(template_id.name.con)
        else:
            raise ValueError("unknown dazl.model.types.Type implementation")
    else:
        raise ValueError("template_id must be a TypeConName")
