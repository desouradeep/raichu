#!/usr/bin/python
from raichu.backends.base import Broker
from raichu.backends import rabbitmq


class BaseConsumer(object):
    def __init__(self, backend, **kwargs):
        broker = Broker(backend, **kwargs)
        self.raichu = broker.backend

        self.exchange_name = kwargs.get('exchange_name', '')
        self.exchange_type = kwargs.get('exchange_type', '')
        self.queue_name = kwargs.get('queue_name', 'raichu_queue')
        self.routing_key = kwargs.get('routing_key', self.queue_name)

        self.raichu.queue_declare(self.routing_key)

    def consume(self, callback, no_ack=False, **kwargs):
        self.raichu.consume(self.queue_name, callback, no_ack, **kwargs)
