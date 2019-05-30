# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ..model.core import DazlError


class SDKComponentUnknownError(DazlError):
    def __init__(self, component_name):
        self.component_name = component_name


class SDKComponentNotFoundError(DazlError):
    def __init__(self, component_name):
        self.component_name = component_name
