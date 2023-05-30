import pika
from config import mq


def call_producer(schedule):
    parameters = pika.URLParameters(f'amqp://{mq.user}:{mq.passwd}@{mq.host}:{mq.port}/%2F')
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    channel.queue_declare(queue='schedule')

    channel.basic_publish(exchange='',
                          routing_key='schedule',
                          body=schedule)

    connection.close()
