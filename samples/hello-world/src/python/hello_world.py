from dazl import simple_client


with simple_client() as client:
    client.ready()
    client.submit_create('Sample.HelloRole', {'party': client.party})
    cid, cdata = client.find_one('Sample.HelloRole')
    client.submit_exercise(cid, 'SayHello', {
        'to': 'Bob',
        'message': 'Hello World'
    })
