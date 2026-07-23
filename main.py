import os
import re
import requests

TOKEN = os.environ["BALE_TOKEN"]

CHANNEL_ID = "goldha"

# دریافت قیمت دلار از API رسمی TGJU
url = "https://api.tgju.org/v1/market/list-data?category_ids=28070&extra_data=1&lang=fa"

headers = {
    "User-Agent": "Mozilla/5.0"
}

data = requests.get(url, headers=headers).json()["data"]

price = None
time = None

for row in data:
    if 'profile/price_dollar_rl' in row[0]:
        price = re.sub("<.*?>", "", row[1]).strip()
        time = row[2]
        break

message = f"""💵 قیمت لحظه‌ای دلار

💰 {price} ریال

🕒 آخرین بروزرسانی:
{time}

📢 @goldha"""

send_url = f"https://tapi.bale.ai/bot{TOKEN}/sendMessage"

response = requests.post(send_url, data={
    "chat_id": CHANNEL_ID,
    "text": message
})

print(response.status_code)
print(response.text)
