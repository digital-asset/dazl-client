# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Awaitable, Callable, TypeVar, Union

from ..protocols.events import BaseEvent
from .commands import EventHandlerResponse

E = TypeVar("E", bound=BaseEvent)
T = TypeVar("T")


EventHandler = Callable[[E], EventHandlerResponse]
AEventHandler = Callable[[E], Union[EventHandlerResponse, Awaitable[EventHandlerResponse]]]


EventHandlerDecorator = Callable[[EventHandler[E]], EventHandler[E]]
AEventHandlerDecorator = Callable[[AEventHandler[E]], AEventHandler[E]]


def fluentize(fn: "Callable[[T], None]", *args, **kwargs) -> "Callable[[T], T]":
    """
    Convert a function that takes a value and returns ``None`` to a function that takes a value
    and returns that value. Additional positional and keyword arguments are passed to the function
    unchanged.
    """
    # Note that there isn't a perfect way to expose the true type signature of this method, which
    # is that it matches the input arguments from the original function and merely changes its
    # return value. All sites where this is used should take care to
    from functools import wraps

    @wraps(fn)
    def impl(*i_args, **i_kwargs):
        fn(*args, *i_args, **kwargs, **i_kwargs)
        return args[0] if args else None

    return impl
