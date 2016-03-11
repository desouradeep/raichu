import json
from random import randint
from time import sleep

from tests.base_consumer import BaseConsumer

params = {
    'exchange_name': 'exchange',
    'exchange_type': 'fanout',
    'queue_name': 'queue',
    'routing_key': 'queue',
}

def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print("[x] %r" % body)

consumer = BaseConsumer('rabbitmq', **params)
consumer.consume(callback)


