# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import logging

from dazl.damlast import DarFile
from dazl.damlast.daml_lf_1 import PackageRef, TypeConName
from dazl.damlast.errors import NameNotFoundError
from dazl.damlast.lookup import MultiPackageLookup
from dazl.damlast.util import package_ref
from dazl.ledger.aio import PackageLoader as AsyncPackageLoader
from dazl.ledger.blocking import PackageLoader as BlockingPackageLoader
import pytest

from .dars import AllKindsOf

ALL_KINDS_OF_PKG_REF = PackageRef(
    "31bffd91b6041cc9b1f44e8e1f0af522c3f353f2c61a2ac662ad4a1396e29c2a"
)


def test_pkg_ref_up_to_date():
    from .dars import AllKindsOf

    with DarFile(AllKindsOf) as dar:
        logging.info("package IDs in AllKindsOf: %s", dar.package_ids())
        assert ALL_KINDS_OF_PKG_REF in dar.package_ids()


class PackageLoaderTest:
    def __init__(self, template_name):
        self.lookup = MultiPackageLookup()
        self.loader = AsyncPackageLoader(self.lookup, DarFile(AllKindsOf))
        self.call_order = []
        self.template_name = template_name

        # the lookup should always start out empty
        assert len(self.lookup.archives()) == 0

    def some_fn(self) -> "TypeConName":
        try:
            name = self.lookup.template_name(self.template_name)
            self.call_order.append("good call")
            return name
        except:
            self.call_order.append("exception")
            raise


class AsyncPackageLoaderTest(PackageLoaderTest):
    def __init__(self, template_name):
        super().__init__(template_name)
        self.loader = AsyncPackageLoader(self.lookup, DarFile(AllKindsOf).async_package_service())


class BlockingPackageLoaderTest(PackageLoaderTest):
    def __init__(self, template_name):
        super().__init__(template_name)
        self.loader = BlockingPackageLoader(
            self.lookup, DarFile(AllKindsOf).blocking_package_service()
        )


@pytest.mark.asyncio
async def test_pkg_loader_do_with_retry_unspecified_package_async():
    test = AsyncPackageLoaderTest(f"{ALL_KINDS_OF_PKG_REF}:AllKindsOf:OneOfEverything")

    # call a function with a loader wrapper
    name = await test.loader.do_with_retry(test.some_fn)

    # the lookup now has only one archive, corresponding to the package ref that we loaded;
    # first, we had to have an exception raised; then we get the call that succeeds
    assert len(test.lookup.archives()) == 1
    assert package_ref(name) == ALL_KINDS_OF_PKG_REF
    assert test.call_order == ["exception", "good call"]


def test_pkg_loader_do_with_retry_unspecified_package_blocking():
    test = BlockingPackageLoaderTest(f"{ALL_KINDS_OF_PKG_REF}:AllKindsOf:OneOfEverything")

    # call a function with a loader wrapper
    name = test.loader.do_with_retry(test.some_fn)

    # the lookup now has only one archive, corresponding to the package ref that we loaded;
    # first, we had to have an exception raised; then we get the call that succeeds
    assert len(test.lookup.archives()) == 1
    assert package_ref(name) == ALL_KINDS_OF_PKG_REF
    assert test.call_order == ["exception", "good call"]


@pytest.mark.asyncio
async def test_pkg_loader_do_with_retry_specified_package_async():
    test = AsyncPackageLoaderTest("*:AllKindsOf:OneOfEverything")

    # call a function with a loader wrapper
    name = await test.loader.do_with_retry(test.some_fn)

    # the lookup now has only one archive, corresponding to the package ref that we loaded;
    # first, we had to have an exception raised; then we get the call that succeeds
    assert len(test.lookup.archives()) > 1
    assert package_ref(name) == ALL_KINDS_OF_PKG_REF
    assert test.call_order == ["exception", "good call"]


def test_pkg_loader_do_with_retry_specified_package_blocking():
    test = BlockingPackageLoaderTest("*:AllKindsOf:OneOfEverything")

    # call a function with a loader wrapper
    name = test.loader.do_with_retry(test.some_fn)

    # the lookup now has only one archive, corresponding to the package ref that we loaded;
    # first, we had to have an exception raised; then we get the call that succeeds
    assert len(test.lookup.archives()) > 1
    assert package_ref(name) == ALL_KINDS_OF_PKG_REF
    assert test.call_order == ["exception", "good call"]


@pytest.mark.asyncio
async def test_pkg_loader_do_with_retry_will_fail_on_unknown_templates_async():
    test = AsyncPackageLoaderTest("*:Nonsense:Nonsense")

    # call a function with a loader wrapper
    try:
        await test.loader.do_with_retry(test.some_fn)
        assert False, "This call was not supposed to succeed"
    except NameNotFoundError:
        # a NameNotFoundError is what we are expecting here
        pass
    except Exception:
        # any other exception is unexpected
        raise

    # all packages will have been loaded; the function will have been called twice, and raise
    # exceptions both times
    assert len(test.lookup.archives()) >= 1
    assert test.call_order == ["exception", "exception"]


def test_pkg_loader_do_with_retry_will_fail_on_unknown_templates_blocking():
    test = BlockingPackageLoaderTest("*:Nonsense:Nonsense")

    # call a function with a loader wrapper
    try:
        test.loader.do_with_retry(test.some_fn)
        assert False, "This call was not supposed to succeed"
    except NameNotFoundError:
        # a NameNotFoundError is what we are expecting here
        pass
    except Exception:
        # any other exception is unexpected
        raise

    # all packages will have been loaded; the function will have been called twice, and raise
    # exceptions both times
    assert len(test.lookup.archives()) >= 1
    assert test.call_order == ["exception", "exception"]
