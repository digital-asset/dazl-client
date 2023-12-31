Daml Python bindings (formerly known as dazl)
=============================================

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/digital-asset/dazl-client/blob/main/LICENSE)
<a href="https://circleci.com/gh/digital-asset/dazl-client">
<img src="https://circleci.com/gh/digital-asset/dazl-client.svg?style=svg">
</a>

Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All Rights Reserved.
SPDX-License-Identifier: Apache-2.0


Rich Python bindings for accessing Ledger API-based applications.

Documentation
-------------
The user documentation is available online [here](https://digital-asset.github.io/dazl-client).

Installation
------------
If you just want to use the library, you can install it locally with `pip`:
```sh
pip install --user dazl
```

Requirements
------------
* Python 3.7+
* [Daml Connect](https://www.daml.com)
* Python gRPC libraries (1.32.0 or later) and Protobuf

Examples
--------

All of the examples below assume you imported `dazl`, and are running a ledger with the default scenario generated with `daml new`.

Connect to the ledger and submit a single command:

```py
import asyncio
import dazl

async def main():
    async with dazl.connect(url='http://localhost:6865', act_as='Alice') as client:
        contract = { 'issuer' : 'Alice', 'owner' : 'Alice', 'name' : 'hello world!' }
        await client.create('Main:Asset', contract)

asyncio.run(main())
```

Connect to the ledger as a single party, print all contracts, and close:

```py
import asyncio
import dazl
from dazl.ledgerutil import ACS

async def main():
    async with dazl.connect(url='http://localhost:6865', read_as='Alice') as conn:
        async with ACS(conn, {"*": {}}) as acs:
            snapshot = await acs.read()

    print(snapshot)

asyncio.run(main())
```

Building locally
----------------

You will need additional dependencies to build locally:

* GNU Make 4.3 or later
* [Poetry](https://python-poetry.org/) for build/dependency management

Once you have these prerequisites in place:

```sh
make build
```

If you see errors about incompatible python versions, switch your environment to python3 using `poetry env use python3`, for instance.

Tests
-----

Tests in the Daml Python bindings are written using [pytest](https://docs.pytest.org/en/latest/). You can run them by doing:

```sh
make test
```

Support
-------

The Daml Python bindings library are supported under the Daml Enterprise license. If you do not have a Daml Enterprise license and are in need of support, have questions or just want to engage in friendly conversation anything Daml, contact us on our [Daml Community Forum](https://discuss.daml.com).
