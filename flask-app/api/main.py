
from fastapi import FastAPI, Depends
from modules.processors import retrieve_data, collect_data
import requests
import tasks
from tasks import process_classify_data, celery_app
from modules.dataModels import DataSet, OutputData, ProcessedData
from fastapi . encoders import jsonable_encoder
from apify_client import ApifyClient


app = FastAPI()


@app.get('/user/{username}')
async def retrieve_user(username: str):
    # sourcery skip: inline-immediately-returned-variable, remove-unnecessary-else, swap-if-else-branches
    profile = collect_data(username)
    if profile["fullName"] == "Restricted profile":
        return {"error": "Restricted Profile"}
    else:
        result = process_classify_data.delay(profile)
        return {'task_id': tasks.id, 'message': 'Profile data found.'}


@app.get('user/state')
async def classify_user(taskID: str):
    result = celery_app.AsyncResult(taskID)
    if result.ready():
        return {'result': result.result}
    else:
        return {'message': 'Verifying authenticity'}
