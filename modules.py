# python  -m venv <foldername> *** to create a virtual environment
#  ../<foldername>/Scripts/activate *** to activate a virtual environment

import os
from dotenv import load_dotenv
import requests
import json


load_dotenv()

password = os.getenv('USERS')

print(password)

response = requests.get(password)

s_code = response.status_code

results = response.json()

results = json.dumps(results)

print(results)
print()
