KitchenSink
===========

A DAR model over a kitchen sink market, with suppliers, a warehouse, retailers,
and customers. The model is designed to be somewhat sensible, while also
exposing a complete surface area that allows for broad functional testing of a
Ledger API client.

Daml serializable types
-----------------------

This model covers almost all of the
[serializable types](https://docs.daml.com/daml/intro/3_Data.html) on the
read-side (fields of a template, either directly or indirectly) and write-side
(similarly, fields of a template via `create` commands, or fields of a choice
argument):

+--------------+----------------------------------+------------------------+
| Daml type    | read-side                        | write-side             |
+--------------+----------------------------------+------------------------+
| `Unit`       | _none_                           | various no-arg choices |
| `Bool`       | `Order.expedite`                 | `Cart.Finish.expedite` |
| `Int`        | various fields                   | _same_                 |
| `Numeric`    | `Order.payment`                  | `Cart.Finish.payent`   |
| `Text`       | various fields                   | _same_                 |
| `Party`      | all templates                    | _same_                 |
| `Date`       | `Customer.birthday`              | _same_                 |
| `Timestamp`  | `WarehouseRetailer.activeAt`     | _same_                 |
| `ContractId` | _none_                           | various choices        |
| `Optional`   | `WarehouseRetailer.terminatedAt` | _same_                 |
| `List`       | `Customer.address`               | _same_                 |
| `TextMap`    | `Item.metadata`                  | _same_                 |
| `GenMap`     | `Cart.contents`                  | _same_                 |
| enums        | `Item.state`                     | _same_                 |
| variants     | _none_                           | _none_                 |
| records      | `SKU`                            | `SKU`                  |
+--------------+----------------------------------+------------------------+

Contract keys
-------------

Most templates have a defined key, so constructs such as "exercise by key" can
be tested effectively.

Multi-party tokens
------------------

The `suppliers` and `retailers` parties are meant to represent groups that have
relationships with a given `warehouse`, and invoking some of those choices
require a multi-party token that grants a supplier or retailer `readAs` rights
over the relevant contracts.
