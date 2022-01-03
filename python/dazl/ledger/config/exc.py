# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

__all__ = ["ConfigError", "ConfigWarning"]


class ConfigError(ValueError):
    pass


class ConfigWarning(Warning):
    pass
