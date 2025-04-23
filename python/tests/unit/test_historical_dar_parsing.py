# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from pathlib import Path
import time

from dazl import LOG
from dazl.damlast import DarFile
from dazl.damlast.lookup import MultiPackageLookup
import pytest

from .dars import KitchenSink

ARCHIVES: Path = Path(__file__).absolute().parent.parent.parent.parent / "_fixtures" / "archives"

dars = list(ARCHIVES.glob("**/*.dar"))


@pytest.mark.parametrize("dar", dars)
def test_dar_version_compatibility(dar):
    short_dar = dar.relative_to(ARCHIVES)
    start_time = time.time()
    dar_file = DarFile(dar)
    archives = dar_file.archives()
    end_time = time.time()
    LOG.info(
        "Successfully read %s in %0.2f seconds with package IDs %r.",
        short_dar,
        end_time - start_time,
        [a.hash for a in archives],
    )


def test_dar_kitchen_sink():
    start_time = time.time()
    dar_file = DarFile(KitchenSink)
    archives = dar_file.archives()
    end_time = time.time()
    LOG.info(
        "Successfully read Kitchen Sink in %0.2f seconds with package IDs %r.",
        end_time - start_time,
        [a.hash for a in archives],
    )

    lookup = MultiPackageLookup(dar_file.archives())
    iface = lookup.interface("KitchenSink.Interfaces.HasLocation:HasLocation")
    assert iface is not None
