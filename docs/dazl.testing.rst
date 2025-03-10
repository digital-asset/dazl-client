.. Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
   SPDX-License-Identifier: Apache-2.0

:mod:`dazl.testing`
======================

.. py:currentmodule:: dazl.testing

This module provides testing utilities for writing simple tests around a Daml ledger running with a
local sandbox. Call the :func:`sandbox` function which returns an object that controls the lifecycle
of a sandbox process.

Starting up a Daml sandbox and uploading relevant DARs takes long enough (more than one second) that
you'll probably want to start a single sandbox to run for the duration of the tests. In order to
achieve good test isolation, though, you don't necessarily want to use the same parties for each
test, you should also use :func:`connect_with_new_party`, which will automatically allocate and
return a new party on every invocation.

Example:

.. code-block:: python

   # this assumes a daml.yaml file exists in the same location as your Python code;
   # you may need to adjust this location for your own project
   project_root = path.dirname(__file__)

   async def main():
      async with sandbox(project_root=) as sb:
         async with connect_with_new_party(url=sb.url) as p:
            logging.info("Connecting as party: %s", p.party)
            await p.conn.create("Some:Asset", {"owner": p.party, "amount": 1000})

   # Python 3.7+ only
   asyncio.run(main())


.. py:function:: sandbox

   :param project_root:
      The root project directory for your Daml project. If supplied, the DAR from this project is
      automatically uploaded like ``daml start`` does. If ``None``, an empty sandbox is started and
      you must supply your own DAR.
   :type project_root: str or os.PathLike
   :param version:
      The Daml Connect version to use.
   :type version: str
   :param timeout:
      The amount of time to wait for a Sandbox to start before giving up. The defualt is 10 seconds.
   :type timeout: datetime.timedelta

   Launch a sandbox running on a randomized port, optionally using the DARs as specified by a local
   Daml project.

   The resulting object can be used as a context manager _or_ an asynchronous context manager.

.. autofunction:: connect_with_new_party
