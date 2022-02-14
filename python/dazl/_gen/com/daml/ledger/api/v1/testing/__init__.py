# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# fmt: off
# isort: skip_file

from .time_service_pb2 import GetTimeRequest, GetTimeResponse, SetTimeRequest
from .time_service_pb2_grpc import TimeServiceStub

__all__ = [
    "GetTimeRequest",
    "GetTimeResponse",
    "SetTimeRequest",
    "TimeServiceStub",
]
