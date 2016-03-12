import zmq

from raichu.backends.base import BaseBackend


class Backend(BaseBackend):
    """
    ZMQ Backend
    """
    # Connection type will define the messaging pattern
    CONNECTION_TYPES = {
        'PUBSUB': (zmq.PUB, zmq.SUB),
        'REQREP': (zmq.REP, zmq.REQ),
        'PAIR': (zmq.PAIR, zmq.PAIR),
        'PUSHPULL': (zmq.PULL, zmq.PUSH),
    }

    def __init__(self, *args, **kwargs):
        self.connection_type = kwargs.get('connection_type', 'PUBSUB')
        if self.connection_type not in self.CONNECTION_TYPES:
            self.connection_type = 'PUBSUB'
        self.sender, self.receiver = self.CONNECTION_TYPES.get(
            self.connection_type)
        self.context = zmq.Context()
        self.topic = kwargs.get('exchange_name', '')
        self.socket = None

    def exchange_declare(self, topic, *args, **kwargs):
        self.topic = topic

    def queue_declare(self, topic='', action='', *args, **kwargs):
        if action == 'PUBLISH':
            action_type = self.sender
        elif action == 'CONSUME':
            action_type = self.receiver
        else:
            print action, '='*50
            raise NotImplementedError

        self.socket = self.context.socket(action_type)

    def queue_bind(self, cc='', dd='', de='', action=None, *args, **kwargs):
        if action == 'PUBLISH':
            self.socket.bind("tcp://*:%s" % 5556)
        elif action == 'CONSUME':
            self.socket.connect('tcp://localhost:%s' % 5556)
        else:
            raise NotImplementedError

    def publish(self, data, *args, **kwargs):
        message = ' '.join([self.topic, data])
        self.socket.send(message)
        print message

    def consume(self, topic='exchange', callback=None, *args, **kwargs):
        print self.connection_type
        if self.connection_type == 'PUBSUB':
            self.socket.setsockopt(zmq.SUBSCRIBE, topic)
        #import ipdb; ipdb.set_trace()
        while True:
            data = self.socket.recv()
            messagedata = ' '.join(data.split()[1:])
            if callback:
                callback(body=messagedata)
