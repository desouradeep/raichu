import json
from random import randint
from time import sleep

from tests.base_publisher import BasePublisher

params = {
    'exchange_name': 'exchange',
    'exchange_type': 'fanout',
    'queue_name': 'queue',
    'routing_key': 'queue',
}

publisher = BasePublisher('rabbitmq', **params)

while True:
    message = {'data': randint(0, 100)}
    message = json.dumps(message)
    publisher.publish(message)
    sleep(0.2)
