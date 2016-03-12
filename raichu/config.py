MESSAGE_BROKER_BACKENDS = {
    'rabbitmq': {
        'ENGINE': 'raichu.backends.rabbitmq',
        'HOST': 'localhost',
        'PORT': 15672,
    },
    'zeromq': {
        'ENGINE': 'raichu.backends.zeromq',
        'HOST': 'localhost',
        'PORT': 5556,
    }
}
