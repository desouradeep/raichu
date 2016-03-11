import pika
from raichu.backends.base import BaseBackend


class Backend(BaseBackend):
    """
    Connection for RabbitMQ backend
    """

    def __init__(self, *args, **kwargs):
        connection_type = kwargs.get('connection_type', None)
        connection_parameters = kwargs.get('connection_parameters', {})

        self.exchange_type = kwargs.get('exchange_type', 'fanout')
        self.exchange_name = kwargs.get('exchange_name', '')

        self.queue_name = kwargs.get('queue_name', 'queue')
        self.routing_key = kwargs.get('routing_key', self.queue_name)

        if 'host' in connection_parameters:
            host = connection_parameters['host']
        else:
            host = 'localhost'

        if connection_type == 'blocking':
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host))
        else:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host))

        self.channel = self.connection.channel()

    def queue_declare(self, **kwargs):
        """
        Declare queue by name
        """
        queue = self.channel.queue_declare(
            queue=self.routing_key)
        print '[x] Queue %s declared' % (self.routing_key)
        return queue

    def queue_bind(self, **kwargs):
        """Bind a queue to an exchange."""
        self.channel.queue_bind(
            exchange=self.exchange_name, queue=self.queue_name,
            routing_key=self.routing_key)
        print '[x] Queue %s bound to %s' % (
            self.queue_name, self.exchange_name)

    def exchange_declare(self, **kwargs):
        """
        Declare an exchange by name
        """
        exchange = self.channel.exchange_declare(
            exchange=self.exchange_name, type=self.exchange_type)
        print '[x] Exchange %s declared' % (self.exchange_name)
        return exchange

    def publish(self, message, **kwargs):
        """
        Publish a message
        """
        self.channel.basic_publish(
            exchange=self.exchange_name, routing_key=self.routing_key,
            body=message)
        print "[x] Sent %r" % (message)

    def close_connection(self, connection):
        """Close the connection."""
        self.connection.close()

    def consume(self, callback, no_ack=False, **kwargs):
        self.channel.basic_consume(
            callback, no_ack=no_ack, queue=self.queue_name)
        self.channel.start_consuming()

