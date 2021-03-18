# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from collections import defaultdict
from inspect import iscoroutine
from typing import Any, Callable, TypeVar, Union
import warnings

from ..client.events import template_reverse_globs
from ..damlast.daml_lf_1 import TypeConName
from .api_types import ArchiveEvent, Boundary, CreateEvent, Event
from .errors import CallbackReturnWarning

__all__ = ["QueryStreamBase"]

from ..damlast.lookup import validate_template

CREATE_EVENT = "create"
ARCHIVE_EVENT = "archive"
BOUNDARY = "boundary"

E = TypeVar("E", bound=Event)


class QueryStreamBase:
    @property
    def _callbacks(self):
        cb = getattr(self, "__cb", None)
        if cb is None:
            cb = defaultdict(list)
            object.__setattr__(self, "__cb", cb)
        return cb

    def on_boundary(self, *args):
        register(self, BOUNDARY, *args)

    def on_create(self, *args):
        register(self, CREATE_EVENT, *args)

    def on_archive(self, *args):
        register(self, ARCHIVE_EVENT, *args)

    async def __aenter__(self):
        """
        Prepare the stream.
        """
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Close the stream.
        """

    async def close(self) -> None:
        """
        Close and dispose of any resources used by this stream.
        """

    async def run(self) -> "None":
        """
        "Runs" the stream. This can be called as an alternative to :meth:`items` when using
        callback-based APIs.
        """
        async for _ in self:
            pass

    async def creates(self):
        """
        Return a stream of :class:`CreateEvent`s. This will include the contracts of the
        Active Contract Set, as well as create events over subsequent transactions.
        """
        async for item in self.items():
            if isinstance(item, CreateEvent):
                yield item

    async def events(self):
        """
        Return a stream of :class:`CreateEvent`s. This will include the contracts of the
        Active Contract Set, as well as create and archive events over subsequent transactions.
        """
        async for item in self.items():
            if isinstance(item, CreateEvent) or isinstance(item, ArchiveEvent):
                yield item

    def items(self):
        """
        Must be overridden by subclasses to provide a stream of events. The implementation is
        expected to call :meth:`_emit_create` and :meth:`_emit_archive` for every encountered event.
        """
        raise NotImplementedError

    def __aiter__(self):
        """
        Returns :meth:`items`, which includes all create and archive events, and boundaries.
        """
        return self.items()

    async def _emit(self, name: str, obj: "Any"):
        for cb in self._callbacks[name]:
            result = cb(obj)
            if result is not None and iscoroutine(result):
                result = await result
            if result is not None:
                warnings.warn(
                    "callbacks should not return anything; the result will be ignored",
                    CallbackReturnWarning,
                )

    async def _emit_create(self, event: "CreateEvent"):
        await self._emit(CREATE_EVENT, event)

    async def _emit_archive(self, event: "ArchiveEvent"):
        await self._emit(ARCHIVE_EVENT, event)

    async def _emit_boundary(self, event: "Boundary"):
        await self._emit(BOUNDARY, event)


def register(q: QueryStreamBase, name: str, *args):
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
    q: QueryStreamBase,
    name: str,
    template_id: Union[None, str, TypeConName],
    fn: Callable[[E], None],
) -> Callable[[E], None]:
    template_search = (
        next(template_reverse_globs(True, *validate_template(template_id)))
        if template_id is not None
        else None
    )
    if template_search == "*:*":
        template_search = None

    def handler(event: E):
        if template_search is not None:
            for match in template_reverse_globs(
                False, *validate_template(event.contract_id.value_type)
            ):
                if template_search == match:
                    fn(event)
                    return
            return
        else:
            fn(event)

    # noinspection PyProtectedMember
    q._callbacks[name].append(handler)
    return fn


def _register_decorator(q: QueryStreamBase, name: str, template_id: Union[None, str, TypeConName]):
    def decorator(fn):
        _register(q, name, template_id, fn)
        return fn

    return decorator
