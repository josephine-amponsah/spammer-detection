# flake8: noqa
from pydantic import BaseModel
from typing import List

class DataSet(BaseModel):
    """
    Data model of input for prediction
    """
    username : str
    full_name : str
    biography : str
    followers : int
    follows : int
    likes : List[int] = []
    reel_count : int
    igtv_count : int
    post_count : int

class ProcessedData(BaseModel):
    followers : int
    follows : int
    med_likes : int
    reel_count : int
    igtv_count : int
    post_count : int
    user_digits : int
    full_characters : int
    bio_len : int
    full_len : int
    full_digits: int
    bio_emojis : int
    

class OutputData(BaseModel):
    status : int


    