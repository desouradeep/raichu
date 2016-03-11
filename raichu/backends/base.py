class BaseBackend(object):
    """Base class for backends."""
    default_port = None
    extra_options = None

    connection_errors = ()
    channel_errors = ()

    def __init__(self, connection, **kwargs):
        self.connection = connection
        self.extra_options = kwargs.get("extra_options")

    def queue_declare(self, *args, **kwargs):
        """Declare a queue by name."""
        pass

    def queue_delete(self, *args, **kwargs):
        """Delete a queue by name."""
        pass

    def exchange_declare(self, *args, **kwargs):
        """Declare an exchange by name."""
        pass

    def queue_bind(self, *args, **kwargs):
        """Bind a queue to an exchange."""
        pass

    def get(self, *args, **kwargs):
        """Pop a message off the queue."""
        pass

    def declare_consumer(self, *args, **kwargs):
        pass

    def consume(self, *args, **kwargs):
        """Iterate over the declared consumers."""
        pass

    def cancel(self, *args, **kwargs):
        """Cancel the consumer."""
        pass

    def ack(self, delivery_tag):
        """Acknowledge the message."""
        pass

    def queue_purge(self, queue, **kwargs):
        """Discard all messages in the queue. This will delete the messages
        and results in an empty queue."""
        return 0

    def reject(self, delivery_tag):
        """Reject the message."""
        pass

    def requeue(self, delivery_tag):
        """Requeue the message."""
        pass

    def purge(self, queue, **kwargs):
        """Discard all messages in the queue."""
        pass

    def message_to_python(self, raw_message):
        """Convert received message body to a python datastructure."""
        return raw_message

    def prepare_message(self, message_data, delivery_mode, **kwargs):
        """Prepare message for sending."""
        return message_data

    def publish(self, message, exchange, routing_key, **kwargs):
        """Publish a message."""
        pass

    def close(self):
        """Close the backend."""
        pass

    def establish_connection(self):
        """Establish a connection to the backend."""
        pass

    def close_connection(self, connection):
        """Close the connection."""
        pass

    def flow(self, active):
        """Enable/disable flow from peer."""
        pass

    def qos(self, prefetch_size, prefetch_count, apply_global=False):
        """Request specific Quality of Service."""
        pass
