import os
import sys
import time
import requests
import pandas as pd
from datetime import datetime as dt

from pprint import pprint
from authorization import get_api_key

API_KEY = get_api_key(api_key_path='../secret.json')

# video_idもしくはそのリストから配信時間やliveChatID,同時接続数などの情報を取得する
def get_streams(limit: int, offset: int):
    '''
    Args:
        API_KEY: Twitch API key
        video_id: str or list of video_id
    returns:
        list of liveStreamingDetails
    '''

    url = "https://api.twitch.tv/kraken/streams/"
    headers = {
        "Client-ID": API_KEY,
        "Accept": 'application/vnd.twitchtv.v5+json',
    }
    params = {
        "limit": limit,
        "offset": offset
    }
    res = requests.get(url, headers=headers, params=params).json()

    return res

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        video_id = args[1]
    res = get_streams(limit=100, offset=0)
