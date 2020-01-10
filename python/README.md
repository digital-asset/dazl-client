dazl
====

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/digital-asset/dazl-client/blob/master/LICENSE)
<a href="https://circleci.com/gh/digital-asset/dazl-client">
<img src="https://circleci.com/gh/digital-asset/dazl-client.svg?style=svg">
</a>

Copyright 2019 Digital Asset (Switzerland) GmbH and/or its affiliates. All Rights Reserved.
SPDX-License-Identifier: Apache-2.0


Rich Python bindings for accessing Ledger API-based applications.

Requirements
------------
* Python 3.6+
* [Poetry](https://python-poetry.org/)
* Although not strictly required for building, you'll probably want the [DAML SDK](https://www.daml.com)

Examples
--------

All of the examples below assume you imported `dazl`.

Connect to the ledger and submit a single command:

```py
with dazl.simple_client('http://localhost:7600', 'Alice') as client:
    client.submit_create('Alice', 'My.Template', { someField: 'someText' })
```

Connect to the ledger as a single party, print all contracts, and close:

```py
with dazl.simple_client('http://localhost:7600', 'Alice') as client:
    # wait for the ACS to be fully read
    client.ready()
    contract_dict = client.find_active('*')
print(contract_dict)
```

Connect to the ledger as multiple parties:

```py
network = dazl.Network()
network.set_config(url='http://localhost:7600')

alice = network.simple_party('Alice')
bob = network.simple_party('Bob')

@alice.ledger_ready()
def set_up(event):
    currency_cid, _ = await event.acs_find_one('My.Currency', {"currency": "USD"})
    return dazl.create('SomethingOf.Value', {
        'amount': 100,
        'currency': currency_cid,
        'from': 'Accept',
        'to': 'Bob' })

@bob.ledger_created('SomethingOf.Value')
def on_something_of_value(event):
    return dazl.exercise(event.cid, 'Accept', { 'message': 'Thanks!' })

network.start()
```


Building locally
----------------
```sh
make package
```

Tests
-----

Tests in dazl are written using [pytest](https://docs.pytest.org/en/latest/). You can run them by doing:

```sh
make test
```
