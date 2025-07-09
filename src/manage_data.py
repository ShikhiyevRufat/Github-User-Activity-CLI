import urllib.error
import urllib.request
from src.config import BASE_URL
import json
from src.utils.error_message import error_message

def fetch_user_Event(username):
    url = f"{BASE_URL}{username}/events"

    with urllib.request.urlopen(url) as response:
        try:
            if response.status == 200:
                data = response.read()
                return json.loads(data)
            else:
                return None
        except urllib.error.HTTPError as e:
            if e.code == 404:
                error_message(e)
            else:
                error_message(e)
            return None

        
        

