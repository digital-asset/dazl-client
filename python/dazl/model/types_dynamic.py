# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Implementation of a codegen proxy type that can be used as a stand-in for codegen types when real
types are unavailable at the "right time".
"""

from dataclasses import dataclass
from typing import Any, Optional


@dataclass(frozen=True)
class NamedRecord:
    name: str
    arguments: dict


class ProxyMeta(type):
    """
    Metaclass for generated record types.
    """
    def __new__(mcs, name, bases, namespace, proxy_name: str):
        result = type.__new__(mcs, name, bases, dict(namespace))
        result._proxy_name = proxy_name
        return result

    def __str__(self):
        return self._proxy_name

    def __repr__(self):
        return self._proxy_name


def generated_type_proxy_root(package_id: 'Optional[str]' = None, root_module_name: 'str' = None) \
        -> Any:
    from typing import Dict
    from threading import RLock

    if not root_module_name:
        raise ValueError('root_module_name must be non-empty and specified')

    lock = RLock()
    types = dict()  # type: Dict[str, Any]

    def get_or_create_proxy(name: str):
        """
        Create a proxy type that looks like a record with a specified name. This name ultimately
        gets resolved later.
        """
        class GeneratedTypeProxy(metaclass=ProxyMeta, proxy_name=name):

            def __getattr__(self, item):
                """
                Create a new type reference with another component suffixed to the path of this
                component.
                """
                if not item:
                    raise AttributeError(item)

                return get_or_create_proxy(f'{name}.{item}')

            def __call__(self, *args, **kwargs):
                """
                Create a record-like structure.
                """
                if len(args):
                    # TODO: Handle the case where arguments are passed positionally. This is "hard"
                    #  because we don't necessarily have the metadata available to resolve
                    #  positional arguments to named arguments.
                    raise ValueError('positional arguments are not supported')
                return NamedRecord(name, kwargs)

            def __str__(self):
                """
                Return the name of the template.
                """
                return str(type(self))

        with lock:
            proxy = types.get(name)
            if proxy is None:
                proxy = types[name] = GeneratedTypeProxy()
            return proxy

    return get_or_create_proxy(root_module_name)


