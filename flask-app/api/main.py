
from fastapi import FastAPI , Depends
from modules.processors import retrieve_data , classifyer
import requests
from modules.dataModels import DataSet , OutputData , ProcessedData
from fastapi . encoders import jsonable_encoder
from apify_client import ApifyClient


app = FastAPI()

@app.get('/user/{username}')
async def retrieve_user(username : str): 
    client = ApifyClient(token = 'apify_api_BdgKVIBQfeQk9rBpUdoOlNhBG7484q15CTd0')# sourcery skip: inline-immediately-returned-variable, remove-unnecessary-else, swap-if-else-branches
    input_data = {
    "usernames": [username]
    }
    # print("Before client.actor")
    run = client.actor("apify/instagram-profile-scraper").call(run_input=input_data)
    # print("After client.actor")
    dataset = client.dataset(run['defaultDatasetId'])
    items = dataset.list_items().items
    output = retrieve_data(items)
    return jsonable_encoder(output)

@app.get('user/state')
async def classify_user(profile: ProcessedData):

    output = classifyer(profile)
    return





