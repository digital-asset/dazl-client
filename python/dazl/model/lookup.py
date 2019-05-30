# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module contains the logic for fuzzy lookups (specifically, template references) are performed
in dazl.
"""

from typing import Any, Iterator, Tuple


def validate_template(template: Any) -> Tuple[str, str]:
    """
    Return a module and type name component from something that can be interpreted as a template.

    :param template:
        Any object that can be interpreted as an identifier for a template.
    :return:
        A tuple of package ID and module name. The special value ``'*'`` is used if either the
        package ID, module name, or both should be wildcarded.
    :raise ValueError:
        If the object could not be interpreted as a thing referring to a template.
    """
    from .types import TemplateMeta, RecordType, TypeReference, UnresolvedTypeReference
    from .types_dynamic import ProxyMeta

    if template == '*' or template is None:
        return '*', '*'

    if isinstance(template, TemplateMeta):
        template = str(template)
    elif isinstance(type(template), ProxyMeta):
        template = str(template)
    elif isinstance(template, UnresolvedTypeReference):
        template = template.name

    if isinstance(template, str):
        if '@' in template:
            t, m = template.split('@')
            return m, t
        elif '/' in template:
            m, t = template.split('/')
            return m, t
        else:
            return '*', template
    elif isinstance(template, RecordType):
        template = template.name

    if isinstance(template, TypeReference):
        return template.module.package_id, template.full_name
    else:
        raise ValueError(f"Don't know how to convert {template!r} into a template")


def template_reverse_globs(primary_only: bool, module: str, type_name: str) -> Iterator[str]:
    """
    Return an iterator over strings that glob to a specified module's type.
    """
    module = module or '*'
    type_name = type_name or '*'

    if module != '*':
        if type_name != '*':
            yield f'{module}/{type_name}'
            if primary_only:
                return
        if not primary_only or type_name == '*':
            yield f'{module}/*'
    if type_name != '*':
        yield f'*/{type_name}'
        if primary_only:
            return
    yield '*/*'
