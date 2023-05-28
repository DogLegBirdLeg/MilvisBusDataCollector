import pika
from config import mq
from logic.bus_finder.bus_finder import find_bus
from multiprocessing import Process


def receive_command():
    parameters = pika.URLParameters(f'amqp://{mq.user}:{mq.passwd}@{mq.host}:{mq.port}/%2F')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='schedule')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='schedule',
                          auto_ack=False,
                          on_message_callback=callback)
    channel.start_consuming()


def callback(ch, method, properties, body):
    start_point, line_id = str(body, 'utf-8').split('/')
    process = Process(target=find_bus, args=(start_point, line_id))
    process.start()
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':
    receive_command()
