import pika
from config import mq


def receive_command():
    parameters = pika.URLParameters(f'amqp://{mq.user}:{mq.passwd}@{mq.host}:{mq.port}/%2F')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='station')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='station',
                          auto_ack=False,
                          on_message_callback=callback)
    channel.start_consuming()


def callback(ch, method, properties, body):
    station_id, call_datetime = str(body, 'utf-8').split('/')
    Collecter.collect(station_id, call_datetime)
    ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    receive_command()