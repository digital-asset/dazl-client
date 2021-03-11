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
* Python 3.8+
* GNU Make
* [Poetry](https://python-poetry.org/) for build/dependency management
* [DAML SDK](https://www.daml.com)

Examples
--------

All of the examples below assume you imported `dazl`, and are running a ledger with the default scenario generated with `daml new`.

Connect to the ledger and submit a single command:

```py
with dazl.simple_client('http://localhost:6865', 'Alice') as client:
    contract = { 'issuer' : 'Alice', 'owner' : 'Alice', 'name' : 'hello world!' }
    client.ready()
    client.submit_create('Main.Asset', contract)
```

Connect to the ledger as a single party, print all contracts, and close:

```py
with dazl.simple_client('http://localhost:6865', 'Alice') as client:
    # wait for the ACS to be fully read
    client.ready()
    contract_dict = client.find_active('*')
print(contract_dict)
```

Connect to the ledger using asynchronous callbacks:

```py
from dazl.protocols.reading import ReadyEvent

network = dazl.Network()
network.set_config(url='http://localhost:6865')

alice = network.aio_party('Alice')


@alice.ledger_ready()
async def onReady(event: ReadyEvent):
    contracts = await event.acs_find_one('Main.Asset')
    print(contracts)


network.run_until_complete()
```


Building locally
----------------
You will need to have [Poetry](https://python-poetry.org) installed, and the dependencies fetched using `poetry install`. Then do:

```sh
make build
```

If you see errors about incompatible python versions, switch your environment to python3 using `poetry env use python3`, for instance.

Building Documentation
----------------------
The above command will build documentation in the root `docs/` dir. Committing this into source control and pushing to github will cause github-pages to be updated.

Tests
-----

Tests in dazl are written using [pytest](https://docs.pytest.org/en/latest/). You can run them by doing:

```sh
make test
```
