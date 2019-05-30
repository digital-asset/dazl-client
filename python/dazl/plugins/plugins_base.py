# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import abc
import argparse

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..client import LedgerClientManager


class Plugin(abc.ABC):
    """
    Definition of a plugin on the DAZL client library.
    """

    def install(self, manager: 'LedgerClientManager') -> None:
        """
        Called in order to have this plugin register its event handlers with the manager.

        :param manager: The ledger client manager to register into.
        """

    def provide_args(self, arg_parser: 'argparse._ActionsContainer') -> None:
        """
        If implemented, load arguments specific to this plugin into the argument parser.

        :param arg_parser: The argument parser to augment.
        """
