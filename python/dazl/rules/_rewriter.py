# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This module implements a rewriter over arbitrary ``tuple`` instances.
"""

from collections import defaultdict
from typing import Any, Callable, Tuple


from .. import LOG


class RewriteContext:
    """
    Recursive object rewriter, based on type-specific callbacks.

    For tuple types, constituent values are recursively rewritten, and if any value is actually
    changed, a new tuple of the same type is created.
    """
    def __init__(self):
        self._type_dispatch = dict()
        self._context_objects = defaultdict(set)

    def context_object(self, typ, name) -> None:
        """
        Supply objects of the specified type as named parameters to rewrite callbacks. Because
        rewriting happens bottom-up, these context objects will necessarily be pre-modified
        (original) values. Additionally, the context object will only be supplied on *child*
        objects, and not the original handler.

        :param typ:
        :param name:
        """
        self._context_objects[typ].add(name)

    def register(self, typ, fn=None, *, recurse=None):
        if fn is None:
            return lambda func: self.register(typ, func, recurse=recurse)
        else:
            self._type_dispatch[typ] = (fn, recurse)
            return fn

    def register_ro(self, typ, fn=None, *, recurse=None):
        """
        Register a handler that does not modify the visited node (the return value is ignored).
        """
        def _wrapper(value, *args, **kwargs):
            fn(value, *args, **kwargs)
            return value
        self.register(typ, fn=_wrapper, recurse=recurse)
        return fn

    def __call__(self, value, *args, **kwargs):
        return self.rewrite(value, *args, **kwargs)

    def rewrite(self, tuple_value, *args, **kwargs):
        # ``None`` cannot be rewritten
        if tuple_value is None:
            return None

        tuple_class = type(tuple_value)
        fn, recurse = self.dispatch(tuple_class)
        if recurse is None:
            recurse = issubclass(tuple_class, (tuple, list, dict)) or \
                      (hasattr(tuple_value, '__getnewargs__') and hasattr(tuple_value, '__dict__'))

        if recurse:
            if tuple_class == tuple:
                # Tuples are frequently subclassed, with different __getnewargs__ behavior for most subtypes.
                # Assume that raw tuples are to be unpacked, and anything else is treated specially (possibly
                # caught by other branches, particularly __getnewargs__).
                old_values = tuple_value
                ctor = lambda *values: tuple(values)
            elif hasattr(tuple_value, '__getnewargs__'):
                old_values = tuple_value.__getnewargs__()
                ctor = tuple_class
            elif isinstance(tuple_value, dict):
                old_values = tuple(tuple_value.values())
                ctor = lambda *values: dict(zip(tuple_value.keys(), values))
            elif isinstance(tuple_value, list):
                old_values = tuple_value
                ctor = lambda *values: list(values)
            else:
                old_values = tuple_value
                ctor = tuple_class

            child_kwargs = dict(kwargs)
            extra_kwargs = {n: tuple_value for n in self._context_objects.get(tuple_class, ())}
            child_kwargs.update(extra_kwargs)

            new_values = [self.rewrite(i, *args, **child_kwargs) for i in old_values]
            changed = False
            for old_value, new_value in zip(old_values, new_values):
                if old_value is not new_value:
                    changed = True
                    break
            if changed:
                try:
                    tuple_value = ctor(*new_values)
                except:
                    LOG.error('Failed to construct %r with arguments %r', ctor, new_values)
                    raise

        return fn(tuple_value, *args, **kwargs)

    def dispatch(self, typ) -> Tuple[Callable[..., Any], bool]:
        disp = self._type_dispatch.get(typ)
        return disp if disp is not None else (_identity, None)


# noinspection PyUnusedLocal
def _identity(value, *args, **kwargs):
    """
    Merely return the original value, unchanged.

    :param value: The value to return.
    :param args: Unused.
    :param kwargs: Unused.
    :return: The original value.
    """
    return value
