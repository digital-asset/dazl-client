# Copyright (c) 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from argparse import ArgumentParser

from ._base import CliCommand
from ..damlsdk import ensure_sdk_component, SDKComponentNotFoundError, SDKComponentUnknownError


class FetchComponentCommand(CliCommand):
    name = 'fetch'
    hidden = True

    def parser(self):
        arg_parser = ArgumentParser('dazl fetch')
        arg_parser.add_argument('component', metavar='NAME:VERSION', help='name:version of the component to fetch')
        arg_parser.add_argument('--force',
                                help='download and unpack artifacts regardless of whether they exist',
                                action='store_true')
        return arg_parser

    def execute(self, args) -> int:
        component = args.component

        try:
            cmps = component.split(':')
            if len(cmps) == 2:
                result = ensure_sdk_component(cmps[0], cmps[1], force=args.force)
            elif len(cmps) == 1:
                result = ensure_sdk_component(cmps[0], None, force=args.force)
            else:
                print('Invalid component identifier: {component!r}. Must be of the form <component>:<version>.')
                return 4
            if result.downloaded:
                print('Successfully downloaded:')
            else:
                print('Skipped downloading because it already exists locally:')
            print(f'    {result.url}')
            print(f'to')
            print(f'    {result.path}')
            return 0

        except SDKComponentNotFoundError:
            print(f'Could not download {component!r}')
            return 2
        except SDKComponentUnknownError:
            print(f'Don\'t know what {component!r} is.')
            print('Only "sdk", "damlc:<version>" and "sandbox:<version>" are supported.')
            return 3

        return 0
