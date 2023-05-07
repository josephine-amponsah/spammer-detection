# flake8: noqa
from pydantic import BaseModel
from typing import List


class DataSet(BaseModel):
    """
    Data model of input for prediction
    """
    username: str
    full_name: str
    biography: str
    followers: int
    follows: int
    likes: List[int] = []
    reel_count: int
    post_count: int


class ProcessedData(BaseModel):
    followersCount: int
    followsCount: int
    highlightReelCount: int
    postsCount: int
    med_likes: float
    user_digits: int
    full_len: int
    full_characters: int
    full_digits: int
    bio_len: int
    bio_emojis: int


class OutputData(BaseModel):
    status: int
