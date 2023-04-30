import pandas as pd
import numpy as np
import json
import joblib
import sklearn
from apify_client import ApifyClient 
from modules.dataModels import DataSet , OutputData , ProcessedData
from typing import List , Optional



def retrieve_data(profile):
    data_list = list()
    for x in profile:
        dict = {}
        for k, v in x.items():
            if k == 'latestPosts':
                info = list()
                for index, y in enumerate(v):
                    info.append(v[index]['likesCount'])
                # index +=1
                dict["likes_"] = info
            else:
                dict[k] = v
        data_list.append(dict)
        
    
    # username = profile.username
    # full_name = profile.full_name
    # biography  = profile.biography
    # followers  = profile.followers
    # follows  = profile.followees
    # # likes : List()
    # reel_count = profile.reels
    # igtv_count =  profile.igtv_count
    # post_count = profile.mediacount
    
    return data_list

def post_info(posts):
    # likes = posts.likes
    return

def process_data(info, data: ProcessedData):
    # user_digits = username.digits
    # full_digits = username.digits
    # full_len = username.digits
    # full_characters = username.digits
    # bio_len = username.digits
    # bio_emojis = bio_len
    
    return

def classify_user(input, data: OutputData):
    # model = joblib.load('../models/final_model.pkl')
    return