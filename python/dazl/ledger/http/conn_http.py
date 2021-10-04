# Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Implementation of :class:`Connection` that uses Python's native ``http`` under the hood.

All endpoints are implemented except for :func:`stream` and `func`:stream_many, which are implemented
under the hood as a polling request.
"""
