#!/usr/bin/python
import json
import sys
from time import sleep
from random import randint

from raichu.backends.base import Broker
from raichu.backends import rabbitmq

broker_parameters = {
    'exchange_name': 'exchange',
    'exchange_type': 'fanout',
    'queue_name': 'queue',
}

class BasePublisher(object):
    def __init__(backend, **kwargs):
        broker = Broker(backend, **kwargs)
        raichu = broker.backend

        raichu.exchange_declare()
        raichu.queue_declare()
        raichu.queue_bind()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        backend = sys.argv[1]
    else:
        backend = 'rabbitmq'

    publisher(backend)

