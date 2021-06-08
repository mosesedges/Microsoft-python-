import os
from dotenv import load_dotenv
import requests
import json


load_dotenv()

password = os.getenv('USERS')

print(password)

response = requests.get(password)

scode = response.status_code

results = response.json()

results = json.dumps(results)

print(results)