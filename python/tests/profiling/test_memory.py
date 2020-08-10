"""
Test to check for memory leaks on long-running clients when connected to a ledger that isn't really
doing much other than ticking time.

In a perfect world, memory usage remains flat in this context because dazl is only supposed to store
active contract set information, and not additional things about transactions. Leaks detected by this
test are more likely to be the fault of infrastructural code.
"""

import sys
from asyncio import get_event_loop
from datetime import datetime

from dazl import create, setup_default_logger, Network
from dazl.model.reading import ContractCreateEvent, ReadyEvent
from pympler import muppy, summary


def main(url: str):
    network = Network()
    network.set_config(url=url)

    test_party = network.aio_party('TestA')
    test_party.add_ledger_ready(ready)
    test_party.add_ledger_created('Main:PostmanRole', created)

    other_party = network.aio_party('TestB')
    other_party.add_ledger_ready(ready)

    dump_state()

    network.run_forever()


def ready(event: ReadyEvent):
    print('The ledger is now ready.')
    return create('Main:PostmanRole', {'postman': event.party})


def created(event: ContractCreateEvent):
    print(f'Created happened for {event.cdata}')


def dump_state():
    loop = get_event_loop()
    print(datetime.now())
    all_objects = muppy.get_objects()
    sum1 = summary.summarize(all_objects)
    summary.print_(sum1, limit=100)
    loop.call_later(10, dump_state)


if __name__ == '__main__':
    setup_default_logger()
    main(sys.argv[1])
