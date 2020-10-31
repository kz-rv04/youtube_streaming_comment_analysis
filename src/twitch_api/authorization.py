import json

def get_api_key(api_key_path='./secret.json'):
    with open(api_key_path, mode="r") as f:
        keys = json.load(f)
    return keys['API_KEY']