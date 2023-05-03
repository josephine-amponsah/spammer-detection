from celery import Celery
from modules.processors import retrieve_data, process_data, classifyer

celery_app = Celery(
    'tasks', broker='pyamqp://guest@localhost//', backend="rpc://")


@celery_app.task
def process_classify_data(data):
    df = retrieve_data(data)
    clean_data = process_data(df)
    result = classifyer(clean_data)
    return result


celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
)
