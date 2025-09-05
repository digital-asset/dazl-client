Daml Python bindings (formerly known as dazl)
=============================================

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/digital-asset/dazl-client/blob/main/LICENSE)
<a href="https://circleci.com/gh/digital-asset/dazl-client">
<img src="https://circleci.com/gh/digital-asset/dazl-client.svg?style=svg">
</a>

Copyright (c) 2017-2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All Rights Reserved.
SPDX-License-Identifier: Apache-2.0


Rich Python bindings for accessing Canton 2.x Ledger API-based applications. It is not intended for use with Canton 3.x.

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
* Python 3.10+
* Go 1.23
* [Daml SDK](https://www.daml.com)
    * Daml 2: 2.10 or later

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

* Direnv (https://direnv.net/)
* Nix (https://nixos.org/download/)

Once you have these prerequisites in place:

```sh
make build
```

Tests
-----

Tests in the Daml Python bindings are written using [pytest](https://docs.pytest.org/en/latest/). You can run them by doing:

```sh
make test
```

Support
-------

The Daml Python bindings library are supported under the Daml Enterprise license. If you do not have a Daml Enterprise license and are in need of support, have questions or just want to engage in friendly conversation anything Daml, contact us on our [Daml Community Forum](https://discuss.daml.com).
