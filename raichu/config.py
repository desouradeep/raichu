MESSAGE_BROKER_BACKENDS = {
    'rabbitmq': {
        'ENGINE': 'raichu.backends.rabbitmq',
        'HOST': 'localhost',
        'PORT': 15672,
    },
    'zmq': {
        'ENGINE': 'raichu.backends.zmq',
        'HOST': 'localhost',
        'PORT': 5556,
    }
}
