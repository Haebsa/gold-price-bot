import os
import requests

TOKEN = os.environ.get("BALE_TOKEN")

url = f"https://tapi.bale.ai/bot{TOKEN}/getMe"

response = requests.get(url)

print(response.status_code)
print(response.text)
