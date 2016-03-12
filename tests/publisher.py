import json
from random import randint
from time import sleep

from tests.base_publisher import BasePublisher

params = {
    'exchange_name': 'raichu',
    'exchange_type': 'fanout',
    'queue_name': 'raichu',
    'routing_key': 'raichu',
}

publisher = BasePublisher('rabbitmq', **params)

while True:
    message = {'data': randint(0, 100)}
    message = json.dumps(message)
    publisher.publish(message)
    sleep(0.2)
