import pika
print('Starting consumer...')
from time import sleep
sleep(5)
print('Consumer started')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
channel = connection.channel()
channel.queue_declare(queue='queue0')

import redis
pool = redis.ConnectionPool(host='redis', port=6379, db=0)
r = redis.Redis(host='redis', port=6379, db=0)

def callback(ch, method, properties, body):
    a = str(body, encoding='utf-8').split('\t')
    key = int(a[0])
    value = a[1]
    r.set(key, value)
    print(value)

channel.basic_consume(callback, queue='queue0', no_ack=True)
channel.start_consuming()
