# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from dazl.damlast import DarFile
from dazl.damlast.lookup import MultiPackageLookup

from .dars import AllKindsOf


def test_wildcard_template_names():
    with DarFile(AllKindsOf) as dar:
        lookup = MultiPackageLookup(dar.archives())

    # make sure that looking for templates, wildcarded by package ref, actually work and return
    # things
    names = [name for ref in lookup.package_ids() for name in lookup.template_names(f"{ref}:*")]
    assert len(names) == 2
