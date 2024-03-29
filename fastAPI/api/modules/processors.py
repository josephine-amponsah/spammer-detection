import pandas as pd
import numpy as np
import json
import joblib
import sklearn
from apify_client import ApifyClient
from modules.dataModels import DataSet, OutputData, ProcessedData
from typing import List, Optional
from pydantic import parse_file_as
import re
import emoji

data_file = "data.json"
input_file = "input.json"
# data collection function


def collect_data(username):
    client = ApifyClient(
        token='apify_api_BdgKVIBQfeQk9rBpUdoOlNhBG7484q15CTd0')
    input_data = {
        "usernames": [username]
    }
    # print("Before client.actor")
    run = client.actor(
        "apify/instagram-profile-scraper").call(run_input=input_data)
    # print("After client.actor")
    dataset = client.dataset(run['defaultDatasetId'])
    profile = dataset.list_items().items
    return profile


def retrieve_data(profile):
    wanted = ["username", "fullName", "biography", "followersCount", "followsCount",
              "highlightReelCount", "postsCount", "latestPosts"]
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
    # with open(data_file, "w") as file:
    #     json.dump(dict, file)
    return dict


def get_likes(data):
    likes = data["likes_"]
    med_likes = np.median(likes)
    return med_likes


pattern = r'[^a-zA-Z\d\s:]'


def fullname_features(df):
    features = {}

    fullname = df["fullName"]
    full_len = len(fullname)
    full_digits = len(re.findall(r'\d', fullname))
    full_characters = len(re.findall(pattern, fullname))
    features = {"full_len": full_len, "full_characters": full_characters, "full_digits": full_digits,
                }
    return features


def bio_features(df):
    features = {}

    bio = df["biography"]
    bio = bio.replace('\n', ' ')
    bio = bio.replace(' ', '')
    bio_len = len(bio)
    bio_emojis = len(emoji.emoji_list(bio))
    features = {"bio_len": bio_len, "bio_emojis": bio_emojis}
    return features


def process_data(df: DataSet):
    name_features = fullname_features(df)
    med_likes = get_likes(df)
    bio_data = bio_features(df)
    username = df["username"]
    user_digits = len(re.findall(r'\d', username))
    merged_dict = {
        **df,
        "med_likes": med_likes,
        'user_digits': user_digits,
        **name_features,
        **bio_data,

    }
    unwanted = ["username", "fullName",
                "biography", "likes_"]
    for key in unwanted:
        merged_dict.pop(key, None)
    return merged_dict


def classifyer(data: ProcessedData):
    # df = pd.DataFrame([data])
    model = joblib.load('models/final_model.pkl')
    output = model.predict(data)
    return output
