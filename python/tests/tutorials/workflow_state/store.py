# Copyright (c) 2017-2020 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import asyncio
import logging

LOG = logging.getLogger('store')


class ContractStore:
    def __init__(self, loop=None, verbose=False):
        self.verbose = verbose
        self.binds = dict()
        self.loop = loop or asyncio.get_event_loop()

    def save(self, name, cid, cdata):
        if self.verbose:
            LOG.critical('Saving %s %s %s', name, cid, cdata)
        name = self._resolve_name(name)
        future = self.binds.get(name)
        if future is None or future.done():
            future = self.loop.create_future()
            self.binds[name] = future
        future.set_result((cid, cdata))

    def find(self, name):
        """
        Find the contract under the given name.

        :param name: The "name" of the contract.
        :return: A ``Future`` that resolves to a (cid, cdata) tuple.
        """
        if self.verbose:
            LOG.critical('Finding in store %s', name)
        else:
            LOG.info('Finding in store %s', name)
        name = self._resolve_name(name)
        future = self.binds.get(name)
        if future is None:
            future = self.loop.create_future()
            self.binds[name] = future
        return future

    def delete(self, name):
        if self.verbose:
            LOG.critical('Deleting from store %s', name)
        name = self._resolve_name(name)
        future = self.binds.get(name)
        if future is not None:
            future.cancel()
            del self.binds[name]

    def archive(self, cid):
        """
        Mark the contract as archived.

        :param cid: The contract ID that is no longer active.
        """
        for key, future in self.binds.items():
            if future.done():
                if future.result() == cid:
                    del self.binds[key]

    def _resolve_name(self, name):
        if isinstance(name, list):
            return '_'.join(name)
        return name

    def match(self, is_match):
        xs = []
        for key, future in self.binds.items():
            cid, value = future.result()
            if is_match(key, cid, value):
                xs.append((key, cid, value))
        return xs
