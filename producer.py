import pika
from datetime import datetime
from config import mq


def call_producer(station):
    parameters = pika.URLParameters(f'amqp://{mq.user}:{mq.passwd}@{mq.host}:{mq.port}/%2F')
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    channel.queue_declare(queue='station')

    call_datetime = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    message = station + '/' + call_datetime
    channel.basic_publish(exchange='',
                          routing_key='station',
                          body=message)

    connection.close()