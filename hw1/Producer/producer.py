import pika
print('Starting producer...')
from time import sleep
sleep(5)
print('Producer started')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit'))
channel = connection.channel()

from sys import stdin, stdout

cur_key = 0
while True:
    a = stdin.readline()
    channel.publish(exchange='', routing_key='queue0', body=str(cur_key) + '\t' + str(a))
    cur_key += 1
