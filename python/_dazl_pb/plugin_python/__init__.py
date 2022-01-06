# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ..protoc import protoc_plugin
from .plugin import run_all_plugins

__all__ = ["main"]

main = protoc_plugin(run_all_plugins)
