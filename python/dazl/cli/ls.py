# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from argparse import ArgumentParser

from .. import LOG
from ._base import CliCommand
from ..plugins import LedgerCapturePlugin
from ..client.manager import LedgerClientManager
from ..client.config import configure_parser, get_config


class ListAllCommand(CliCommand):
    name = 'ls'

    def parser(self) -> ArgumentParser:
        arg_parser = ArgumentParser('dazl ls')

        configure_parser(arg_parser, config_file_support=True)
        arg_parser.add_argument('--format', '--fmt', '-F', type=str, default=LedgerCapturePlugin.DEFAULT_FORMATTER_NAME)
        arg_parser.add_argument('--template-filter', '-T', type=str)
        arg_parser.add_argument('--all', '-A', action='store_true')
        return arg_parser

    def execute(self, args) -> int:
        LOG.debug('Executing an ls...')

        final_config = get_config(args, config_file_support=True)

        with LedgerClientManager(final_config) as mgr:
            kwargs = dict()
            if args.template_filter:
                kwargs['template_filter'] = [template.strip() for template in args.template_filter.split(',')]
            if args.all:
                kwargs['include_archived'] = True

            inspector = LedgerCapturePlugin.stdout(**kwargs)
            mgr.register(inspector)
            mgr.run_until_complete()

            inspector.dump_all(fmt=args.format)
            return 0

