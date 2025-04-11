# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from asyncio import Event, ensure_future, get_event_loop, sleep
from typing import AbstractSet, Optional

from dazl.damlast import DarFile
from dazl.damlast.daml_lf_1 import PackageRef
from dazl.damlast.lookup import MultiPackageLookup
from dazl.ledger.aio import PackageLoader, PackageService
from dazl.ledger.auth import TokenOrTokenProvider
from dazl.prim import TimeDeltaLike
import pytest

from .dars import AllKindsOf

ALL_KINDS_OF_PKG_REF = PackageRef(
    "e32da8a173e9667e1cd6557a12bf3edbbb6e5a9eb017c3363280ba0b22100bc4"
)


def load_some_bytes() -> tuple[PackageRef, bytes]:
    with DarFile(AllKindsOf) as dar:
        # noinspection PyProtectedMember
        for a in dar._pb_archives():
            return PackageRef(a.hash), a.payload
    raise Exception()


@pytest.mark.asyncio
async def test_pkg_loader_only_fetches_once(executor):
    pkg_ref, contents = load_some_bytes()

    class MockPackageService(PackageService):
        def __init__(self):
            self.call_count = 0

        async def get_package(
            self,
            package_id: PackageRef,
            /,
            *,
            token: Optional[TokenOrTokenProvider] = None,
            timeout: Optional[TimeDeltaLike] = None,
        ) -> bytes:
            self.call_count += 1
            if package_id != pkg_ref:
                raise Exception
            return contents

        async def list_package_ids(
            self,
            *,
            token: Optional[TokenOrTokenProvider] = None,
            timeout: Optional[TimeDeltaLike] = None,
        ) -> AbstractSet[PackageRef]:
            return frozenset([pkg_ref])

    conn = MockPackageService()
    lookup = MultiPackageLookup()
    loader = PackageLoader(lookup, conn)

    # first, call the PackageLoader.load coroutine
    pkg1 = await loader.load(pkg_ref)

    # now call it again
    pkg2 = await loader.load(pkg_ref)

    # we should have only called package_bytes once
    assert conn.call_count == 1

    # the two Package objects that come back should be identical; creating Package objects are
    # expensive but they are also immutable, so the two calls should return the same instance
    # as an optimization
    assert pkg1 is pkg2


@pytest.mark.asyncio
async def test_pkg_loader_consolidates_concurrent_fetch(executor):
    loop = get_event_loop()
    pkg_ref, contents = load_some_bytes()

    evt1 = Event()
    evt2 = Event()

    class MockPackageService(PackageService):
        def __init__(self):
            self.call_count = 0

        async def get_package(
            self,
            package_id: PackageRef,
            /,
            *,
            token: Optional[TokenOrTokenProvider] = None,
            timeout: Optional[TimeDeltaLike] = None,
        ) -> bytes:
            self.call_count += 1
            if package_id != pkg_ref:
                raise Exception
            evt1.set()
            await evt2.wait()
            return contents

        async def list_package_ids(
            self,
            *,
            token: Optional[TokenOrTokenProvider] = None,
            timeout: Optional[TimeDeltaLike] = None,
        ) -> AbstractSet[PackageRef]:
            # we don't expect this method to be called in the test
            raise Exception

    conn = MockPackageService()
    lookup = MultiPackageLookup()
    loader = PackageLoader(lookup, conn)

    # first, call the PackageLoader.load coroutine
    fut1 = ensure_future(loader.load(pkg_ref))

    # wait until we are definitely in the MockPackageService.package_bytes call in one of
    # PackageLoader's background threads
    await loop.run_in_executor(executor, lambda: evt1.wait())

    # now schedule a _second_ PackageLoader.load coroutine; because the first one is still in
    # progress, this should NOT result in a second call to
    # MockPackageService.package_bytes
    fut2 = ensure_future(loader.load(pkg_ref))

    # allow coroutines some time to screw things up
    await sleep(0.1)

    # make sure that neither call to PackageLoader.load has actually come back yet
    assert not fut1.done()
    assert not fut2.done()

    # now unblock MockPackageService.package_bytes, which will return our bytes
    evt2.set()

    # grab the results from both async PackageLoader.load coroutine calls
    pkg1 = await fut1
    pkg2 = await fut2

    # we should have only called package_bytes once
    assert conn.call_count == 1

    # the two Package objects that come back should be identical; creating Package objects are
    # expensive but they are also immutable, so the two calls should return the same instance
    # as an optimization
    assert pkg1 is pkg2
