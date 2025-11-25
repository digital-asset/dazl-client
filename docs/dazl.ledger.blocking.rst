.. Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
   SPDX-License-Identifier: Apache-2.0

:mod:`dazl.ledger.blocking`
===========================

.. py:currentmodule:: dazl.ledger.blocking

.. note::

   There is currently no implementation of this interface! Blocking gRPC support is planned for
   dazl v7.6.0. If you need a blocking API, you must continue to use the :class:`dazl.Network`
   and :meth:`dazl.Network.simple_party` API until dazl v7.6.0.

Protocol that describes the interface for a blocking connection to a Daml ledger. The methods of
an implementation should be thread-safe, with the exception of :meth:`open` and :meth:`close`.

Since ``dazl`` activity is typically dominated by I/O, using a blocking :class:`Connection` with
multiple threads is usually more expensive than using connections. You should consider
using the asyncio variant of this API (:class:`dazl.ledger.aio.Connection`) instead.
