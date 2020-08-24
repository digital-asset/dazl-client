# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains the logic for fuzzy lookups (specifically, template references) are performed
in dazl.
"""

from typing import Any, Iterator, Tuple


def validate_template(template: Any) -> 'Tuple[str, str]':
    """
    Return a module and type name component from something that can be interpreted as a template.

    :param template:
        Any object that can be interpreted as an identifier for a template.
    :return:
        A tuple of package ID and ``Module.Name:EntityName`` (the package-scoped identifier for the
        type). The special value ``'*'`` is used if either the package ID, module name, or both
        should be wildcarded.
    :raise ValueError:
        If the object could not be interpreted as a thing referring to a template.
    """
    from ..damlast.daml_lf_1 import TypeConName
    from ..damlast.util import package_ref, package_local_name
    from .types import RecordType, TypeReference, UnresolvedTypeReference

    if template == '*' or template is None:
        return '*', '*'

    if isinstance(template, UnresolvedTypeReference):
        template = template.name

    if isinstance(template, str):
        components = template.split(':')
        if len(components) == 3:
            # correct number of colons for a fully-qualified name
            pkgid, m, e = components
            return pkgid, f'{m}:{e}'

        elif len(components) == 2:
            # one colon, so assume the package ID is unspecified
            m, e = components
            return '*', f'{m}:{e}'

        elif len(components) == 1:
            # no colon whatsoever
            # TODO: Add a deprecation warning in the appropriate place
            m, _, e = components[0].rpartition('.')
            return '*', f'{m}:{e}'
            # raise ValueError('string must be in the format PKG_REF:MOD:ENTITY or MOD:ENTITY')

    elif isinstance(template, RecordType):
        template = template.name

    if isinstance(template, TypeReference):
        template = template.con

    if isinstance(template, TypeConName):
        return package_ref(template), package_local_name(template)
    else:
        raise ValueError(f"Don't know how to convert {template!r} into a template")


def template_reverse_globs(primary_only: bool, package_id: str, type_name: str) -> 'Iterator[str]':
    """
    Return an iterator over strings that glob to a specified type.
    """
    package_id = package_id or '*'
    type_name = type_name or '*'

    if package_id != '*':
        if type_name != '*':
            if ':' not in type_name:
                # this is a historical use of template name here; assume the last dot was supposed
                # to have been a colon instead
                m, delim, e = type_name.rpartition('.')
                if delim:
                    yield f'{package_id}:{m}:{e}'
                    if primary_only:
                        return
            yield f'{package_id}:{type_name}'
            if primary_only:
                return
        if not primary_only or type_name == '*':
            yield f'{package_id}:*'
    if type_name != '*':
        if ':' not in type_name:
            # this is a historical use of template name here; assume the last dot was supposed
            # to have been a colon instead
            m, delim, e = type_name.rpartition('.')
            if delim:
                yield f'*:{m}:{e}'
                if primary_only:
                    return
        yield f'*:{type_name}'
        if primary_only:
            return
    yield '*:*'
