#!/usr/bin/python
import json
import sys
from time import sleep
from random import randint

from raichu.backends.base import Broker
from raichu.backends import rabbitmq


def publisher(backend):

    broker_parameters = {
        'exchange_name': 'exchange',
        'exchange_type': 'fanout',
        'queue_name': 'queue',
    }

    broker = Broker(backend, **broker_parameters)
    raichu = broker.backend

    raichu.exchange_declare()
    raichu.queue_declare()
    raichu.queue_bind()

    def publish():
        message = {'data': randint(0, 100)}
        message = json.dumps(message)
        raichu.publish(message)


    while True:
        publish()
        sleep(0.1)

    raichu.connection.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        backend = sys.argv[1]
    else:
        backend = 'rabbitmq'

    publisher(backend)

