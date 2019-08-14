# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Pre-cook the test DARs for this project.
"""

import logging
import time
from pathlib import Path
from typing import Dict, Mapping, Optional, Sequence

from dazl import setup_default_logger
from dazl.damlsdk.fetch import ensure_sdk_component
from dazl.util.dar import build_dar
from dazl.util.io import find_nearest_ancestor

DAZL_ROOT = find_nearest_ancestor('.dazl-root', Path(__file__).resolve()).parent
DAML_ROOT = DAZL_ROOT / 'python' / 'tests' / 'resources'
CACHE_ROOT = DAZL_ROOT / '.cache' / 'test-dars'


setup_default_logger(logging.DEBUG)


def load_dars(damlc_version: 'Optional[str]' = None) -> 'Mapping[str, Path]':
    """
    Ensure that the DARs in the test project are all pre-cooked.
    """
    dars = dict()  # type: Dict[str, Path]

    if damlc_version is None:
        damlc_version = '100.13.18'

    ensure_sdk_component('damlc', damlc_version)

    start_time = time.time()

    # TODO: parallelize DAR building; this step still takes 40 seconds on my machine
    daml_files: Sequence[Path] = list(DAML_ROOT.glob('*.daml'))
    if not daml_files:
        raise Exception(f'Could not find any DAML files under {DAML_ROOT}')

    for daml_file in daml_files:
        dar_file = CACHE_ROOT / damlc_version / (daml_file.stem + '.dar')
        if dar_file.exists() and dar_file.stat().st_mtime >= daml_file.stat().st_mtime:
            logging.info('Skipping building %s because it is newer than %s', dar_file, daml_file)
        else:
            dar_file.parent.mkdir(parents=True, exist_ok=True)
            build_dar(daml_file, dar_file)

        dars[daml_file.stem] = dar_file

    end_time = time.time()

    logging.info('Finished building %s test DARs in %.2f.', len(dars), end_time - start_time)
    for dar_name, dar_file in dars.items():
        logging.info('    %s: %s', dar_name, dar_file)

    return dars


DARS = load_dars()

# These are primarily defined so that we get good auto-complete in the IDE; it's also a way of
# enforcing that DARs we expect to exist, actually exist.
AllKindsOf = DARS['AllKindsOf']
AllParty = DARS['AllParty']
Complicated = DARS['Complicated']
DottedFields = DARS['DottedFields']
MapSupport = DARS['MapSupport']
Pending = DARS['Pending']
Simple = DARS['Simple']
TestServer = DARS['TestServer']


if __name__ == '__main__':
    print(DARS)
