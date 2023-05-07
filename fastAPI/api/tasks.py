from celery import Celery
from modules.processors import retrieve_data, process_data, classifyer
import pika
import json
import pandas as pd

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='response_queue')

celery_app = Celery(
    'tasks', broker='pyamqp://guest@localhost//', backend="rpc://")


@celery_app.task
def process_classify_data(data, queue_name):
    queue_name = 'response_queue'
    df = retrieve_data(data)
    clean_data = process_data(df)
    clean_data = pd.DataFrame(clean_data)
    clean_data = clean_data.fillna(0)
    result = classifyer(clean_data)
    channel.basic_publish(
        exchange="",
        routing_key=queue_name,
        body=json.dumps(result),
    )

    return result


celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
)
