import os
import requests

TOKEN = os.environ.get("BALE_TOKEN")

CHANNEL_ID = "اینجا شناسه کانال بله را بگذار"

message = """
✅ ربات قیمت طلا و دلار فعال شد

سیستم ارسال خودکار با موفقیت راه‌اندازی شد.
"""

url = f"https://tapi.bale.ai/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHANNEL_ID,
    "text": message
}

response = requests.post(url, data=data)

print(response.text)
