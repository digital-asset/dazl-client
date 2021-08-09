# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from collections import defaultdict
import sys
from typing import Any, Callable, TypeVar, Union, no_type_check
import warnings

from ...damlast.daml_lf_1 import TypeConName
from ...damlast.lookup import matching_normalizations, normalize
from ..api_types import CreateEvent, Event, ExerciseResponse
from ..errors import CallbackReturnWarning

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ["CREATE_EVENT", "ARCHIVE_EVENT", "BOUNDARY", "Callbacks", "check_return_type"]

E = TypeVar("E", bound=Event)

CREATE_EVENT = "create"  # type: Literal["create"]
ARCHIVE_EVENT = "archive"  # type: Literal["archive"]
BOUNDARY = "boundary"  # type: Literal["boundary"]


class Callbacks:
    @property
    def _callbacks(self):
        cb = getattr(self, "__cb", None)
        if cb is None:
            cb = defaultdict(list)
            object.__setattr__(self, "__cb", cb)
        return cb

    @no_type_check
    def on_boundary(self, *args):
        register(self, BOUNDARY, *args)

    @no_type_check
    def on_create(self, *args):
        register(self, CREATE_EVENT, *args)

    @no_type_check
    def on_archive(self, *args):
        register(self, ARCHIVE_EVENT, *args)


def check_return_type(obj: "Any") -> None:
    """
    Validate that return type of a callback is ``None``.

    We also allow CreateEvent and ExerciseResponse as valid return types for callbacks because
    it makes inline lambdas easier to write, even those these results are ignored.
    """
    if obj is not None and not isinstance(obj, (CreateEvent, ExerciseResponse)):
        warnings.warn(
            "callbacks should not return anything; the result will be ignored",
            CallbackReturnWarning,
        )


def register(q: Callbacks, name: str, *args):
    if len(args) == 0:
        return _register_decorator(q, name, None)
    elif len(args) == 1:
        if callable(args[0]):
            return _register(q, name, None, args[0])
        elif isinstance(args[0], (str, TypeConName)):
            return _register_decorator(q, name, args[0])
        else:
            raise ValueError("expected a template name or a callback here")
    elif len(args) == 2:
        template_id, fn = args
        _register(q, name, template_id, fn)
    else:
        raise ValueError("too many arguments")


def _register(
    q: Callbacks,
    name: str,
    template_id: "Union[None, str, TypeConName]",
    fn: "Callable[[E], None]",
) -> "Callable[[E], None]":
    template_search = normalize(template_id)

    def handler(event: E):
        if template_search in matching_normalizations(event.contract_id.value_type):
            fn(event)

    # noinspection PyProtectedMember
    q._callbacks[name].append(handler)
    return fn


def _register_decorator(q: Callbacks, name: str, template_id: Union[None, str, TypeConName]):
    def decorator(fn):
        _register(q, name, template_id, fn)
        return fn

    return decorator
