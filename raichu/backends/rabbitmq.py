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

    def queue_declare(self, queue, **kwargs):
        """
        Declare queue by name
        """
        return self.channel.queue_declare(queue=queue)

    def exchange_declare(self, exchange, type, **kwargs):
        """
        Declare an exchange by name
        """
        return self.channel.exchange_declare(
            exchange=exchange, type=type)

    def publish(self, message, exchange, routing_key, **kwargs):
        """
        Publish a message
        """
        self.channel.basic_publish(
            exchange=exchange, routing_key=routing_key,
            body=message)
        print "[x] Sent %r" % (message)
        self.connection.close()

