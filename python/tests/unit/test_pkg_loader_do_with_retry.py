# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# noinspection PyPackageRequirements
import pytest

from dazl.damlast import DarFile
from dazl.damlast.daml_lf_1 import PackageRef, TypeConName
from dazl.damlast.errors import NameNotFoundError
from dazl.damlast.lookup import MultiPackageLookup
from dazl.damlast.util import package_ref
from dazl.protocols.pkgloader_aio import PackageLoader

from .dars import AllKindsOf

ALL_KINDS_OF_PKG_REF = PackageRef(
    "e32da8a173e9667e1cd6557a12bf3edbbb6e5a9eb017c3363280ba0b22100bc4"
)


class PackageLoaderTest:
    def __init__(self, template_name):
        self.lookup = MultiPackageLookup()
        self.loader = PackageLoader(self.lookup, DarFile(AllKindsOf))
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


@pytest.mark.asyncio
async def test_pkg_loader_do_with_retry_unspecified_package():
    test = PackageLoaderTest(f"{ALL_KINDS_OF_PKG_REF}:AllKindsOf:OneOfEverything")

    # call a function with a loader wrapper
    name = await test.loader.do_with_retry(test.some_fn)

    # the lookup now has only one archive, corresponding to the package ref that we loaded;
    # first, we had to have an exception raised; then we get the call that succeeds
    assert len(test.lookup.archives()) == 1
    assert package_ref(name) == ALL_KINDS_OF_PKG_REF
    assert test.call_order == ["exception", "good call"]


@pytest.mark.asyncio
async def test_pkg_loader_do_with_retry_specified_package():
    test = PackageLoaderTest("*:AllKindsOf:OneOfEverything")

    # call a function with a loader wrapper
    name = await test.loader.do_with_retry(test.some_fn)

    # the lookup now has only one archive, corresponding to the package ref that we loaded;
    # first, we had to have an exception raised; then we get the call that succeeds
    assert len(test.lookup.archives()) > 1
    assert package_ref(name) == ALL_KINDS_OF_PKG_REF
    assert test.call_order == ["exception", "good call"]


@pytest.mark.asyncio
async def test_pkg_loader_do_with_retry_will_fail_on_unknown_templates():
    test = PackageLoaderTest("*:Nonsense:Nonsense")

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
