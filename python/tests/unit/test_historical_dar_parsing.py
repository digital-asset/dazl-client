# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
import time

from dazl import LOG
from dazl.damlast import DarFile
import pytest

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
