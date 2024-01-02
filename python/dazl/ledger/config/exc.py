# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

__all__ = ["ConfigError", "ConfigWarning"]


class ConfigError(ValueError):
    pass


class ConfigWarning(Warning):
    pass
