#!/usr/bin/python
import sys

from raichu.backends.base import Broker
from raichu.backends import rabbitmq


def consumer(backend):
    broker_parameters = {
        'queue_name': 'queue',
    }

    def callback(ch, method, properties, body):
        ch.basic_ack(delivery_tag = method.delivery_tag)
        print("[x] %r" % body)

    broker = Broker('rabbitmq')
    raichu = broker.backend

    raichu.queue_declare()
    raichu.consume(callback)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        backend = sys.argv[1]
    else:
        backend = 'rabbitmq'

    consumer(backend)
