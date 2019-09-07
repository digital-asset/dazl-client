import json
import os
import dazl


def main():
    party = os.getenv('DAML_LEDGER_PARTY')
    url = os.getenv('DAML_LEDGER_URL')
    print(f'Starting a ledger for party {party!r} on {url}...')

    network = dazl.Network()
    network.set_config(url=url)
    client = network.aio_party(party)

    @client.ledger_ready()
    def ensure_setup(event):
        return dazl.create_and_exercise('Sample:Setup', {'party': client.party}, 'Execute', {})

    @client.ledger_created('Sample.HelloMessage')
    def on_message(event):
        if (event.cdata['receiver'] == client.party) and (event.cdata['sender'] != client.party):
            return dazl.exercise_by_key('Sample.HelloRole', client.party, 'SayHello', {
                'to': event.cdata['sender'],
                'message': f'Thank you for telling me, {json.dumps(event.cdata["message"])}'
            })

    network.run_forever()


if __name__ == '__main__':
    main()
