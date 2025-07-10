import urllib.error
import urllib.request
from src.config import BASE_URL
import json
from src.utils.error_message import error_message
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'tasks.json')


def fetch_user_Event(username):
    url = f"{BASE_URL}{username}/events"

    with urllib.request.urlopen(url) as response:
        try:
            if response.status == 200:
                data = response.read()
                parsed_data = json.loads(data)
                with open(DATA_FILE, "w") as file:
                    json.dump(parsed_data, file, indent=4)
                return parsed_data
            else:
                return None
        except urllib.error.HTTPError as e:
            if e.code == 404:
                error_message(e)
            else:
                error_message(e)
            return None

        
        

