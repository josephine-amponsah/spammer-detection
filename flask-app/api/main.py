
from fastapi import FastAPI, Depends, Request, Form
from modules.processors import retrieve_data, collect_data
import requests
import tasks
from tasks import process_classify_data, celery_app
from modules.dataModels import DataSet, OutputData, ProcessedData
from fastapi . encoders import jsonable_encoder
from apify_client import ApifyClient
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/")
def form(request: Request):
    return templates.TemplateResponse("detector.html", {"request": request})


@app.post('/user', response_class=HTMLResponse)
async def retrieve_user(request: Request, username: str = Form(...)):
    # sourcery skip: inline-immediately-returned-variable, remove-unnecessary-else, swap-if-else-branches
    profile = collect_data(username)
    if profile[0]["fullName"] == "Restricted profile":
        return templates.TemplateResponse('detector.html', {'request': request, "message": "Restricted Profile"})
    else:
        result = process_classify_data.delay(profile)
        return templates.TemplateResponse('detector.html', {'request': request, 'task_id': result.task_id, 'message': 'Profile data found.'})


@app.get('/user/{task_id}')
async def classify_user(task_id: str):
    result = celery_app.AsyncResult(task_id, app=celery_app)
    if result.ready():
        return {'result': result.result}
    else:
        return {'message': 'Verifying authenticity'}
