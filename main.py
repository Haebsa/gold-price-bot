import os
import requests
import json

TOKEN = os.environ["BALE_TOKEN"]

url = f"https://tapi.bale.ai/bot{TOKEN}/getUpdates"

response = requests.get(url)

print(json.dumps(response.json(), indent=2, ensure_ascii=False))
