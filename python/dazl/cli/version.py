# Copyright (c) 2017-2022 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from argparse import ArgumentParser

from .. import __version__ as version
from ._base import CliCommand


class VersionCommand(CliCommand):
    name = "version"

    def parser(self) -> ArgumentParser:
        return ArgumentParser()

    def execute(self, args) -> int:
        print(version)
        return 0
