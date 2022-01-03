# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
`asyncio`-flavored protocols and base classes for connecting to a Daml ledger.
"""

from collections import defaultdict
from inspect import iscoroutine
import sys
from typing import Any, Callable, TypeVar, Union, no_type_check
import warnings

from .. import Connection as _Connection, QueryStream as _QueryStream
from ...damlast.daml_lf_1 import TypeConName
from ...damlast.lookup import matching_normalizations, normalize
from ..api_types import ArchiveEvent, Boundary, CreateEvent, Event, ExerciseResponse
from ..errors import CallbackReturnWarning

if sys.version_info >= (3, 8):
    from typing import Protocol, runtime_checkable
else:
    from typing_extensions import Protocol, runtime_checkable


__all__ = ["PackageService", "Connection", "QueryStream", "QueryStreamBase", "PackageLoader"]

Self = TypeVar("Self")
Ret = Union[None, CreateEvent, ExerciseResponse]
E = TypeVar("E", bound=Event)

CREATE_EVENT = "create"
ARCHIVE_EVENT = "archive"
BOUNDARY = "boundary"


class PackageService(Protocol):
    """
    Protocol that describe a service that provides package information. The :class:`Connection`
    protocol extends this interface.
    """

    async def get_package(self, __package_id) -> bytes:
        raise NotImplementedError

    async def list_package_ids(self):
        raise NotImplementedError


@runtime_checkable
class Connection(_Connection, Protocol):
    async def __aenter__(self):
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        raise NotImplementedError


@runtime_checkable
class QueryStream(_QueryStream, Protocol):
    async def __aenter__(self):
        raise NotImplementedError

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    def __aiter__(self):
        raise NotImplementedError


class QueryStreamBase(QueryStream):
    """
    Base implementation of the :class:`QueryStream` protocol
    """

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

    async def __aenter__(self):
        """
        Prepare the stream.
        """
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Close the stream.
        """
        await self.close()

    async def close(self) -> None:
        """
        Close and dispose of any resources used by this stream.
        """

    async def run(self) -> None:
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

            # allow CreateEvent and ExerciseResponse as valid return types for callbacks because
            # it makes inline lambdas easier to write; we don't do anything with them
            if result is not None and not isinstance(result, (CreateEvent, ExerciseResponse)):
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
    template_search = normalize(template_id)

    def handler(event: E):
        if template_search in matching_normalizations(event.contract_id.value_type):
            fn(event)

    # noinspection PyProtectedMember
    q._callbacks[name].append(handler)
    return fn


def _register_decorator(q: QueryStreamBase, name: str, template_id: Union[None, str, TypeConName]):
    def decorator(fn):
        _register(q, name, template_id, fn)
        return fn

    return decorator


# Imports internal to this package are at the bottom of the file to avoid circular dependencies
from .pkgloader import PackageLoader  # noqa
