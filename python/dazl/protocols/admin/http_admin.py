# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from urllib.request import Request, urlopen

from ... import LOG


def admin_upload_package(url: str, contents: bytes) -> None:
    request = Request(url, method='PUT')
    with urlopen(request, contents) as response:
        status = response.getcode()
        if 200 <= status <= 299:
            return None
        else:
            LOG.error('Received %s when trying to upload a DALF to %s', status, url)
