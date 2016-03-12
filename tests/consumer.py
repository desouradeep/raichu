import json
from random import randint
from time import sleep

from tests.base_consumer import BaseConsumer

params = {
    'exchange_name': 'raichu',
    'exchange_type': 'fanout',
    'queue_name': 'raichu',
    'routing_key': 'raichu',
}

def callback(ch=None, method=None, properties=None, body=None):
    #ch.basic_ack(delivery_tag = method.delivery_tag)
    print("[x] %r" % body)

consumer = BaseConsumer('rabbitmq', **params)
consumer.consume(callback=callback)


