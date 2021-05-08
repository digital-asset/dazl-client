dazl
====

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/digital-asset/dazl-client/blob/master/LICENSE)
<a href="https://circleci.com/gh/digital-asset/dazl-client">
<img src="https://circleci.com/gh/digital-asset/dazl-client.svg?style=svg">
</a>

Copyright (c) 2017-2021 Digital Asset (Switzerland) GmbH and/or its affiliates. All Rights Reserved.
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
* Python 3.6+
* [Daml Connect](https://www.daml.com)
* Python gRPC libraries (1.32.0 or later) and Protobuf

**WARNING:** The next major version of dazl (v8.0.0) will require **Python 3.7** or later.

Examples
--------

All of the examples below assume you imported `dazl`, and are running a ledger with the default scenario generated with `daml new`.

Connect to the ledger and submit a single command:

```py
import asyncio
import dazl

async def main():
    async with dazl.connect('http://localhost:6865', act_as='Alice') as client:
        contract = { 'issuer' : 'Alice', 'owner' : 'Alice', 'name' : 'hello world!' }
        await client.create('Main:Asset', contract)

# Python 3.7+
asyncio.run(main())

# Python 3.6+
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

Connect to the ledger as a single party, print all contracts, and close:

```py
import asyncio
import dazl
from dazl.ledgerutil import ACS

async def main():
    async with dazl.connect('http://localhost:6865', read_as='Alice') as conn:
        async with ACS(conn, {"*": {}}) as acs:
            snapshot = await acs.read()
            
    print(snapshot)

# Python 3.7+
asyncio.run(main())

# Python 3.6+
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

Building locally
----------------

You will need additional dependencies to build locally:

* GNU Make
* [Poetry](https://python-poetry.org/) for build/dependency management

Once you have these prerequisites in place:

```sh
make build
```

If you see errors about incompatible python versions, switch your environment to python3 using `poetry env use python3`, for instance.

Tests
-----

Tests in dazl are written using [pytest](https://docs.pytest.org/en/latest/). You can run them by doing:

```sh
make test
```
