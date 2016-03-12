#!/usr/bin/python
from raichu.backends.base import Broker
from raichu.backends import rabbitmq


class BasePublisher(object):
    def __init__(self, backend, **kwargs):
        broker = Broker(backend, **kwargs)
        self.raichu = broker.backend

        self.exchange_name = kwargs.get('exchange_name', '')
        self.exchange_type = kwargs.get('exchange_type', '')
        self.queue_name = kwargs.get('queue_name', 'raichu_queue')
        self.routing_key = kwargs.get('routing_key', self.queue_name)

        self.raichu.exchange_declare(self.exchange_name, self.exchange_type)
        self.raichu.queue_declare(self.routing_key, action='PUBLISH')
        self.raichu.queue_bind(
            self.queue_name, self.exchange_name, self.routing_key,
            action='PUBLISH')

    def publish(self, message, **kwargs):
        self.raichu.publish(
            message, self.exchange_name,
            self.routing_key, **kwargs)
