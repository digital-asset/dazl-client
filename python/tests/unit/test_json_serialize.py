# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

def test_serializers():
    # merely import the SCALAR_FORMATTERS symbol, which runs a check to make sure that all
    # scalars can be safely serialized in JSON
    from dazl.protocols.v0.json_ser_command import _SCALAR_FORMATTERS
    assert _SCALAR_FORMATTERS
