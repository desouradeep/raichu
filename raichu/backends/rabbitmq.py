import pika
from raichu.backends.base import BaseBackend


class Backend(BaseBackend):
    """
    Connection for RabbitMQ backend
    """

    def __init__(self, *args, **kwargs):
        connection_type = kwargs.get('connection_type', None)
        connection_parameters = kwargs.get('connection_parameters', {})

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

    def queue_declare(self, routing_key, **kwargs):
        """
        Declare queue by name
        """
        queue = self.channel.queue_declare(
            queue=routing_key)
        print '[x] Queue %s declared' % (routing_key)
        return queue

    def queue_bind(self, queue_name='', exchange_name='',
            routing_key='', **kwargs):
        """Bind a queue to an exchange."""
        self.channel.queue_bind(
            exchange=exchange_name, queue=queue_name,
            routing_key=routing_key)
        print '[x] Queue %s bound to %s' % (
            queue_name, exchange_name)

    def exchange_declare(self, exchange_name, type, **kwargs):
        """
        Declare an exchange by name
        """
        exchange = self.channel.exchange_declare(
            exchange=exchange_name, type=type)
        print '[x] Exchange %s declared' % (exchange_name)
        return exchange

    def publish(self, message, exchange, routing_key, **kwargs):
        """
        Publish a message
        """
        self.channel.basic_publish(
            exchange=exchange, routing_key=routing_key,
            body=message)
        print "[x] Sent %r" % (message)

    def close_connection(self, connection):
        """Close the connection."""
        self.connection.close()

    def consume(self, queue, callback, no_ack=False, **kwargs):
        self.channel.basic_consume(
            callback, no_ack=no_ack, queue=queue)
        self.channel.start_consuming()

