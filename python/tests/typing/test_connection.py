# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys
from typing import AsyncIterator, Awaitable, Callable, Generic, Iterator, ParamSpec, TypeVar

from dazl.ledger import aio, blocking

P = ParamSpec("P")
R = TypeVar("R")


def compare_sigs(_: Callable[P, R]) -> AssertSignature[P, Awaitable[R]]:
    return AssertSignature()


def compare_stream_sigs(
    _: Callable[P, blocking.QueryStream],
) -> AssertSignature[P, aio.QueryStream]:
    return AssertSignature()


def compare_iter_sigs(_: Callable[P, Iterator[R]]) -> AssertSignature[P, AsyncIterator[R]]:
    return AssertSignature()


class AssertSignature(Generic[P, R]):
    def __call__(self, fn: Callable[P, R]) -> None:
        return


def typecheck_test_connection(a: aio.Connection, b: blocking.Connection) -> None:
    """
    Make sure the type signatures for asyncio-based and blocking Connections line up except
    in their return types.

    Note that this test doesn't DO anything; but if our type signatures don't line up,
    mypy will at least complain and fail the build.
    """
    compare_sigs(b.open)(a.open)
    compare_sigs(b.close)(a.close)
    compare_sigs(b.submit)(a.submit)

    compare_sigs(b.create)(a.create)
    compare_sigs(b.exercise)(a.exercise)
    compare_sigs(b.create_and_exercise)(a.create_and_exercise)
    compare_sigs(b.exercise_by_key)(a.exercise_by_key)
    compare_sigs(b.archive)(a.archive)
    compare_sigs(b.archive_by_key)(a.archive_by_key)
    compare_sigs(b.get_ledger_end)(a.get_ledger_end)
    compare_stream_sigs(b.query)(a.query)
    compare_stream_sigs(b.query_many)(a.query_many)
    compare_stream_sigs(b.stream)(a.stream)
    compare_stream_sigs(b.stream_many)(a.stream_many)
    compare_sigs(b.get_user)(a.get_user)
    compare_sigs(b.create_user)(a.create_user)
    compare_sigs(b.list_users)(a.list_users)
    compare_sigs(b.list_user_rights)(a.list_user_rights)
    compare_sigs(b.allocate_party)(a.allocate_party)
    compare_sigs(b.list_known_parties)(a.list_known_parties)
    compare_sigs(b.get_version)(a.get_version)
    # this type signature is actually wrong!
    compare_sigs(b.get_package)(a.get_package)  # type: ignore
    compare_sigs(b.list_package_ids)(a.list_package_ids)
    compare_sigs(b.upload_package)(a.upload_package)
    compare_sigs(b.get_metering_report)(a.get_metering_report)

    compare_sigs(b.get_user)(a.get_user)
    compare_sigs(b.list_users)(a.list_users)


def typecheck_test_querystream(a: aio.QueryStream, b: blocking.QueryStream) -> None:
    compare_iter_sigs(b.creates)(a.creates)
    compare_iter_sigs(b.events)(a.events)
    compare_iter_sigs(b.items)(a.items)
    compare_sigs(b.run)(a.run)
    compare_sigs(b.close)(a.close)
