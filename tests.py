import json

import requests

test = requests.get("http://127.0.0.1:5000/how10")


tim = test.json()

