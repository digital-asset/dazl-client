# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from dazl import LOG
from dazl.damlast import DarFile
import pytest

ARCHIVES: Path = Path(__file__).absolute().parent.parent.parent.parent / "_fixtures" / "archives"

dars = list(ARCHIVES.glob("**/*.dar"))


@pytest.mark.parametrize("dar", dars)
def test_dar_version_compatibility(dar):
    short_dar = dar.relative_to(ARCHIVES)
    dar_file = DarFile(dar)
    archives = dar_file.archives()
    LOG.info("Successfully read %s with package IDs %r.", short_dar, [a.hash for a in archives])
