# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from pathlib import Path
from typing import Mapping

import yaml

DAZL_ROOT = Path(__file__).absolute().parent.parent.parent.parent
DAML_ROOT = DAZL_ROOT / "python" / "tests" / "resources"


def load_dars() -> Mapping[str, Path]:
    """
    Ensure that the DARs in the test project are all pre-cooked.
    """
    import os
    import subprocess

    dar_dir = DAZL_ROOT / "_fixtures/src"  # type: Path

    dars = dict[str, Path]()
    for d in dar_dir.iterdir():
        if d.is_dir():
            daml_yaml_path = d / "daml.yaml"
            if not daml_yaml_path.exists():
                continue
            with daml_yaml_path.open() as f:
                daml_yaml = yaml.safe_load(f)
            dar_path = d / f".daml/dist/{daml_yaml['name']}-{daml_yaml['version']}.dar"
            dars[d.name] = dar_path

    if any(not dar_path.exists() for dar_path in dars.values()):
        env = os.environ.copy()
        daml_bin = os.path.expanduser("~/.daml/bin")
        if daml_bin not in env.get("PATH", ""):
            env["PATH"] = f"{daml_bin}:{env.get('PATH', '')}"

        code = subprocess.run(["make", "dars"], cwd=str(DAZL_ROOT), env=env)
        if code.returncode != 0:
            raise RuntimeError("Could not build test dars!")

    return dars


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
SCUModels1 = DARS["scu-assets1"]
SCUModels2 = DARS["scu-assets2"]
Simple = DARS["simple"]
TestServer = DARS["test-server"]
UploadTest = DARS["upload-test"]


if __name__ == "__main__":
    print(DARS)
