import pandas as pd
import numpy as np
import json
import joblib
import sklearn
from apify_client import ApifyClient
from modules.dataModels import DataSet, OutputData, ProcessedData
from typing import List, Optional

data_file = "data.json"

# data collection function


def retrieve_data(profile):
    wanted = ["username", "fullName", "biography", "followersCount", "followsCount",
              "highlightReelCount", "igtvVideoCount", "postsCount", "latestPosts"]
    dict = {}
    for i in wanted:
        if i == 'latestPosts':
            list = []
            posts = profile[0][i]
            for index, y in enumerate(posts):
                list.append(posts[index]['likesCount'])
            dict["likes_"] = list
        else:
            dict[i] = profile[0][i]
    with open(data_file, "w") as file:
        json.dump(dict, file)


def get_likes(profile):
    for k, v in profile.items():
        if k == 'latestPosts':
            info = list()
            for index, y in enumerate(v):
                info.append(v[index]['likesCount'])
            # index +=1

    med_likes = info.mean()
    return med_likes


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
