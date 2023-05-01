import pandas as pd
import numpy as np
import json
import joblib
import sklearn
from apify_client import ApifyClient 
from modules.dataModels import DataSet , OutputData , ProcessedData
from typing import List , Optional

def get_likes(profile):
    for k, v in profile.items():
            if k == 'latestPosts':
                info = list()
                for index, y in enumerate(v):
                    info.append(v[index]['likesCount'])
                # index +=1
                
    med_likes = info.mean()
    return med_likes

def retrieve_data(profile):

    username = profile["username"]
    full_name = profile["fullName"]
    biography  = profile["biography"]
    followers  = profile["followersCount"]
    follows  = profile["followsCount"]
    likes  = get_likes(profile)
    reel_count = profile["highlightReelCount"]
    igtv_count =  profile["igtvVideoCount"]
    post_count = profile["postsCount"]
    
    return profile

def post_info(posts):
    # likes = posts.likes
    return

def process_data(data: DataSet):
    # user_digits = username.digits
    # full_digits = username.digits
    # full_len = username.digits
    # full_characters = username.digits
    # bio_len = username.digits
    # bio_emojis = bio_len
    
    return

def classifyer(input, data: ProcessedData):
    # model = joblib.load('../models/final_model.pkl')
    return