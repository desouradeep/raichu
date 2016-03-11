import json
from time import sleep
from random import randint

from raichu.backends import rabbitmq


exchange_name = 'rabbit_exchange'
exchange_type = 'fanout'
queue_name = 'rabbit_queue'
routing_key = 'rabbit_queue'

raichu_rabbit = rabbitmq.Backend()
raichu_rabbit.exchange_declare(exchange_name, exchange_type)
raichu_rabbit.queue_declare(routing_key)
raichu_rabbit.queue_bind(queue_name, exchange_name, routing_key)

def publish():
	message = {'data': randint(0, 100)}
	message = json.dumps(message)
	raichu_rabbit.publish(message, exchange_name, routing_key)


while True:
	publish()
	sleep(0.1)

raichu_rabbit.connection.close()