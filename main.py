import os
import requests

TOKEN = os.environ.get("BALE_TOKEN")

print("TOKEN EXISTS:", TOKEN is not None)

url = f"https://tapi.bale.ai/bot{TOKEN}/getMe"

response = requests.get(url)

print("Status:", response.status_code)
print("Response:", response.text)
