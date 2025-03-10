# Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from argparse import ArgumentParser


class CliCommand:
    @property
    def name(self) -> str:
        raise NotImplementedError("command needs a name")

    @property
    def hidden(self) -> bool:
        return False

    def parser(self) -> ArgumentParser:
        raise NotImplementedError("ArgumentParser not supplied")

    def execute(self, args) -> int:
        raise NotImplementedError("Command not implemented")
