import os
import re
import requests

# =====================
# توکن‌ها
# =====================

BALE_TOKEN = os.environ["BALE_TOKEN"]
RUBIK_TOKEN = os.environ["RUBIK_TOKEN"]


# =====================
# کانال‌ها
# =====================

BALE_CHANNEL = "@goldha"
RUBIKA_CHANNEL = "@gold_pric"


# =====================
# دریافت قیمت دلار TGJU
# =====================

url = "https://api.tgju.org/v1/market/list-data?category_ids=28070&extra_data=1&lang=fa"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

data = response.json()["data"]


price = None
time = None


for row in data:
    if "profile/price_dollar_rl" in row[0]:
        price = re.sub("<.*?>", "", row[1]).strip()
        time = row[2]
        break


if price is None:
    print("قیمت پیدا نشد")
    exit()


# =====================
# متن پیام
# =====================
# =====================
# متن مخصوص بله
# =====================

bale_message = f"""
💵 قیمت لحظه‌ای دلار

💰 {price} ریال

🕒 آخرین بروزرسانی:
{time}

📢 کانال بله:
@goldha
"""


# =====================
# متن مخصوص روبیکا
# =====================

rubika_message = f"""
💵 قیمت لحظه‌ای دلار

💰 {price} ریال

🕒 آخرین بروزرسانی:
{time}

📢 کانال روبیکا:
@gold_pric
"""

# =====================
# ارسال به بله
# =====================

bale_url = f"https://tapi.bale.ai/bot{BALE_TOKEN}/sendMessage"


bale_data = {
    "chat_id": BALE_CHANNEL,
    "text": bale_message
}


bale_response = requests.post(
    bale_url,
    data=bale_data
)


print("Bale:")
print(bale_response.text)



# =====================
# ارسال به روبیکا
# =====================

rubika_url = f"https://botapi.rubika.ir/v3/{RUBIK_TOKEN}/sendMessage"


rubika_data = {
    "chat_id": RUBIKA_CHANNEL,
    "text": rubika_message
}


rubika_response = requests.post(
    rubika_url,
    json=rubika_data
)


print("Rubika:")
print(rubika_response.text)
