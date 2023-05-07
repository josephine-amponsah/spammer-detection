
from fastapi import FastAPI, Depends, Request, Form
from modules.processors import retrieve_data, collect_data
import requests
import tasks
import json
import asyncio
from tasks import process_classify_data, celery_app
from modules.dataModels import DataSet, OutputData, ProcessedData
from fastapi . encoders import jsonable_encoder
from apify_client import ApifyClient
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import pika

app = FastAPI()
templates = Jinja2Templates(directory="templates")
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/")
def form(request: Request):
    return templates.TemplateResponse("detector.html", {"request": request})


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='response_queue')


@app.post('/user', response_class=HTMLResponse)
async def retrieve_user(request: Request, username: str = Form(...)):
    # sourcery skip: inline-immediately-returned-variable, remove-unnecessary-else, swap-if-else-branches
    profile = collect_data(username)
    if len(profile) == 0:
        return templates.TemplateResponse('detector.html', {'request': request, "message": "Profile not found"})
    elif profile[0]["fullName"] == "Restricted profile":
        return templates.TemplateResponse('detector.html', {'request': request, "message": "Restricted Profile"})
    else:
        result = celery_app.send_task('tasks.process_classify_data', args=[
                                      profile], kwargs={'queue_name': 'response_queue'}, reply_to='response_queue')

        return templates.TemplateResponse('detector.html', {'request': request, 'task_id': result.task_id, 'message': 'Profile data found! Proceed to verify Authenticity'})


@app.get('/user/{task_id}')
async def classify_user(request: Request, task_id: str):
    result = celery_app.AsyncResult(task_id, app=celery_app)
    if result.ready():
        return templates.TemplateResponse('detector.html', {'request': request, 'status': result.result})
    else:
        return templates.TemplateResponse('detector.html', {'request': request, 'status': 'Verifying authenticity'})

    # placeholder = 'Verifying Status'
    # result = placeholder
    # message = []

    # def callback(channel, method, properties, body):
    #     message.append(body)
    # channel.basic_consume('response_queue', on_message_callback=callback)
    # # if method_frame:
    # #     response = json.loads(body)
    # #     channel.basic_ack(method_frame.delivery_tag)
    # #     return templates.TemplateResponse('detector.html', {'request': request, 'status': result})
    # # else:
    # #     await asyncio.sleep(1)

    # while not message:
    #     connection.process_data_events()

    # # Close the connection and return the message as the response
    # connection.close()
    # return templates.TemplateResponse('detector.html', {'request': request, 'status': message})
