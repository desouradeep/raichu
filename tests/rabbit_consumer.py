from raichu.backends import rabbitmq

exchange_name = 'rabbit_exchange'
exchange_type = 'fanout'
queue_name = 'rabbit_queue'
routing_key = 'rabbit_queue'

def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print("[x] %r" % body)

raichu_rabbit = rabbitmq.Backend('rabbitmq')
raichu_rabbit.exchange_declare(exchange_name, exchange_type)
raichu_rabbit.queue_declare(routing_key)
raichu_rabbit.queue_bind(queue_name, exchange_name, routing_key)

raichu_rabbit.consume(queue_name, callback)


