# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from pathlib import Path
from typing import Mapping

DAZL_ROOT = Path(__file__).absolute().parent.parent.parent.parent
DAML_ROOT = DAZL_ROOT / "python" / "tests" / "resources"


def load_dars() -> "Mapping[str, Path]":
    """
    Ensure that the DARs in the test project are all pre-cooked.
    """
    dar_dir = DAZL_ROOT / "_fixtures/src"  # type: Path

    import subprocess

    code = subprocess.run(["make", "dars"], cwd=str(DAZL_ROOT))
    if code.returncode != 0:
        raise RuntimeError("Could not build test dars!")

    return {d.name: d / f".daml/dist/{d.name}-1.0.0.dar" for d in dar_dir.iterdir() if d.is_dir()}


DARS = load_dars()

# These are primarily defined so that we get good auto-complete in the IDE; it's also a way of
# enforcing that DARs we expect to exist, actually exist.
AllKindsOf = DARS["all-kinds-of"]
AllParty = DARS["all-party"]
Complicated = DARS["complicated"]
DottedFields = DARS["dotted-fields"]
KitchenSink = DARS["kitchen-sink"]
MapSupport = DARS["map-support"]
Pending = DARS["pending"]
PostOffice = DARS["post-office"]
Simple = DARS["simple"]
TestServer = DARS["test-server"]
UploadTest = DARS["upload-test"]


if __name__ == "__main__":
    print(DARS)
