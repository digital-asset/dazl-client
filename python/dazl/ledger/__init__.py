# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""
This module contains the types needed to submit commands to and read events from a
Daml `gRPC Ledger API <https://docs.daml.com/app-dev/ledger-api.html>`_ or
`HTTP JSON API <https://docs.daml.com/json-api/index.html>`_.
"""
from __future__ import annotations

import sys
from typing import Callable, Literal, Protocol, TypeAlias, TypeVar, overload

from . import aio, blocking
from .api_types import (
    ActAs,
    Admin,
    ArchiveEvent,
    Boundary,
    Command,
    CommandMeta,
    CreateAndExerciseCommand,
    CreateCommand,
    CreateEvent,
    Event,
    EventOrBoundary,
    ExerciseByKeyCommand,
    ExerciseCommand,
    ExerciseResponse,
    IdentityProviderAdmin,
    MeteringReport,
    PartyInfo,
    ReadAs,
    Right,
    SubmitResponse,
    User,
)
from .config import ConfigArgs

if sys.version_info >= (3, 11):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = [
    "aio",
    "blocking",
    "connect",
    "ActAs",
    "Admin",
    "ArchiveEvent",
    "Boundary",
    "Command",
    "CommandMeta",
    "CreateAndExerciseCommand",
    "CreateCommand",
    "CreateEvent",
    "Event",
    "EventOrBoundary",
    "ExerciseByKeyCommand",
    "ExerciseCommand",
    "ExerciseResponse",
    "IdentityProviderAdmin",
    "MeteringReport",
    "PartyInfo",
    "PackageService",
    "ReadAs",
    "Right",
    "Connection",
    "QueryStream",
    "User",
]

CreateFn = TypeVar("CreateFn", bound=Callable[[CreateEvent], SubmitResponse])
ArchiveFn = TypeVar("ArchiveFn", bound=Callable[[ArchiveEvent], SubmitResponse])
BoundaryFn = TypeVar("BoundaryFn", bound=Callable[[Boundary], SubmitResponse])

# These are written as Protocols with __call__ instead of a Callable so that they can be safely
# overloaded for the asynchronous variants. See dazl.ledger.aio's typing file.


class OnCreateDecorator(Protocol):
    def __call__(self, fn: CreateFn, /) -> CreateFn: ...


class OnArchiveDecorator(Protocol):
    def __call__(self, fn: ArchiveFn, /) -> ArchiveFn: ...


class OnBoundaryDecorator(Protocol):
    def __call__(self, fn: BoundaryFn, /) -> BoundaryFn: ...


# These overload declarations were painfully constructed in careful consultation with:
#     https://github.com/python/mypy/issues/6580
#
# * ``blocking: Literal[False] = False`` must appear as the very first argument to the first
#   overload; this reflects the _actual_ default value combined with a literal value marker.
#   Putting this parameter in any other position causes the mypy error "Overloaded function
#   signatures 1 and 2 overlap with incompatible return types".
# * All other subsequent overloads must define the ``blocking`` parameter as a _non-optional_
#   positional parameter. Specifying a default value in these cases confuses mypy and MUST be
#   avoided.
# * An explicit overload typed as a bool is also required.
#
# Separately PyCharm thinks the name of the parameter "blocking" conflicts with the import to
# dazl.ledger.blocking above, even though that's not actually the case. Either way we silence
# that warning too.
#
@overload
def connect(**kwargs: Unpack[ConfigArgs]) -> aio.Connection: ...


# noinspection PyShadowingNames
@overload
def connect(*, blocking: Literal[False], **kwargs: Unpack[ConfigArgs]) -> aio.Connection: ...


# noinspection PyShadowingNames
@overload
def connect(*, blocking: Literal[True], **kwargs: Unpack[ConfigArgs]) -> blocking.Connection: ...


# noinspection PyShadowingNames
@overload
def connect(*, blocking: bool, **kwargs: Unpack[ConfigArgs]) -> Connection: ...


# noinspection PyShadowingNames
def connect(*, blocking=False, **kwargs):
    """
    Create a connection from the supplied parameters.

    See the `documentation for this function
    <https://digital-asset.github.io/dazl-client/dazl.ledger.html#dazl.ledger.connect>`_ for more
    details on the parameters it takes and how values are defaulted.
    """
    from .config import Config
    from .grpc.conn_aio import Connection as GrpcConnection

    if blocking:
        from .blocking._aiowrapper import ConnectionThunk

        return ConnectionThunk(lambda: GrpcConnection(Config.create(**kwargs)))
    else:
        cfg = Config.create(**kwargs)
        conn = GrpcConnection(cfg)

    return conn


class PackageService(Protocol):
    """
    Protocol that describe a service that provides package information. The :class:`Connection`
    protocol extends this interface.
    """

    def get_package(self, package_id, /, *, token=None, timeout=None):
        """
        Given a package ID, fetch the binary data for the corresponding DALF.

        :param package_id:
            The package ID of the DALF to retrieve.
        :param token:
            An optional token string, or function/async function that returns a token. If provided,
            this overrides the token passed in at connection construction time.
        :param timeout:
            The maximum length of time to wait before giving up.
        :return:
            The byte array contents of the DALF associated with the package ID.
        """
        raise NotImplementedError

    def list_package_ids(self, *, token=None, timeout=None):
        """
        Fetch a list of all known package IDs.

        :param token:
            An optional token string, or function/async function that returns a token. If provided,
            this overrides the token passed in at connection construction time.
        :param timeout:
            The maximum length of time to wait before giving up.
        """
        raise NotImplementedError


Connection: TypeAlias = aio.Connection | blocking.Connection
QueryStream: TypeAlias = aio.QueryStream | blocking.QueryStream
