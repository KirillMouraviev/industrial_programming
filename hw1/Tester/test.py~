import pika
print('Starting tester...')
from time import sleep
sleep(5)
print('Tester started')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
channel = connection.channel()
channel.queue_declare(queue='queue0')

import redis
pool = redis.ConnectionPool(host='redis', port=6379, db=0)
r = redis.Redis(host='redis', port=6379, db=0)

from time import sleep
cur_key = 0
while True:
    sleep(0.01)
    word = r.get(cur_key)
    if word is not None:
        print(word)
        cur_key += 1
