import os
import requests

TOKEN = os.environ["BALE_TOKEN"]
CHAT_ID = 4540440927

url = f"https://tapi.bale.ai/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": "🎉 تست موفق!\n\nربات با موفقیت به کانال متصل شد."
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)
