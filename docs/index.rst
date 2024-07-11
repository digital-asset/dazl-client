.. Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
   SPDX-License-Identifier: Apache-2.0

dazl: DA client library for Python
==================================

Version |release|

Dependencies
------------

You will need Python 3.6 or later and a Daml Ledger.

Getting Started
---------------

This section assumes that you already have a running ledger with the standard `daml new` model
loaded, and have imported `dazl`.

Connect to the ledger and submit a single command:

.. literalinclude:: ../python/tests/unit/test_docs.py
   :language: python
   :pyobject: test_send_single_command
   :lines: 2-
   :dedent: 4

Connect to the ledger as a single party, print all contracts, and close:

.. literalinclude:: ../python/tests/unit/test_docs.py
   :language: python
   :pyobject: test_read
   :lines: 2-
   :dedent: 4

Connect to the ledger using asynchronous callbacks:

.. literalinclude:: ../python/tests/unit/test_docs.py
   :language: python
   :pyobject: test_read_using_callback
   :lines: 2-
   :dedent: 4


Code
----

Build-time dependencies are handled using `Poetry <https://python-poetry.org/>`_.

Support
-------

The dazl library is supported by the Daml community. If you are in need of support, have questions or just want to engage in friendly conversation anything Daml, contact us on our `Daml Community Forum <https://discuss.daml.com>`_.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   basics
   testing
   migrating
   dazl
   glossary
