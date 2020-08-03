# Copyright (c) 2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
import pytest


@pytest.fixture(scope="session")
def sandbox() -> str:
    from dazl import sandbox as test_sandbox
    with test_sandbox([]) as proc:
        logging.info('Shared test sandbox started at %s', proc.url)
        yield proc.url
        logging.info('The tests are done. Shutting down the sandbox...')
