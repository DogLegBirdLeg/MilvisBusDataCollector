import pika
from config import mq


def call_producer(bus_no, line_id):
    parameters = pika.URLParameters(f'amqp://{mq.user}:{mq.passwd}@{mq.host}:{mq.port}/%2F')
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()
    channel.queue_declare(queue='bus')

    message = str(bus_no) + '/' + line_id

    channel.basic_publish(exchange='',
                          routing_key='bus',
                          body=message)

    connection.close()
