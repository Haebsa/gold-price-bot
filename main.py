import os
import re
import requests
import html


BALE_TOKEN = os.environ["BALE_TOKEN"]
RUBIK_TOKEN = os.environ["RUBIK_TOKEN"]

BALE_CHANNEL = "@goldha"
RUBIKA_CHANNEL = "@gold_pric"


# =========================
# دریافت قیمت از نواسان
# =========================

url = "https://www.navasan.tech/wp-navasan.php?usd&eur&aed&usdt&xau&18ayar&sekkeh&bahar&nim&rob&gerami"

response = requests.get(url)

text = response.text


# حذف navasanret
text = re.search(r"navasanret\('(.*)'\);", text, re.S).group(1)

text = text.replace("\\r\\n"," ")
text = text.replace("\\/","/")
text = text.replace("\\\\","")
text = html.unescape(text)

# =========================
# استخراج قیمت ها
# =========================
def get_price(id):

    pattern = rf'id=\\"{id}\\".*?class=\\"val\\">(.*?)<\\/td>'

    result = re.search(pattern, text, re.S)

    if result:
        return result.group(1)

    return "-"


usd = get_price("usd")
eur = get_price("eur")
aed = get_price("aed")
usdt = get_price("usdt")
xau = get_price("xau")
gold18 = get_price("18ayar")
sekkeh = get_price("sekkeh")
bahar = get_price("bahar")
nim = get_price("nim")
rob = get_price("rob")
gerami = get_price("gerami")



# =========================
# متن پیام
# =========================

message = f"""
📊 قیمت لحظه‌ای طلا و ارز

💵 دلار آمریکا:
{usd} تومان

💶 یورو:
{eur} تومان

💲 تتر:
{usdt} تومان

💰 درهم:
{aed} تومان


🟡 طلای ۱۸ عیار:
{gold18} تومان

🟠 اونس طلا:
{xau} تومان


🪙 سکه امامی:
{sekkeh} تومان

🪙 سکه بهار آزادی:
{bahar} تومان

🪙 نیم سکه:
{nim} تومان

🪙 ربع سکه:
{rob} تومان

🪙 سکه گرمی:
{gerami} تومان


⏰ بروزرسانی خودکار

📢 @goldha
"""



# =========================
# ارسال بله
# =========================

requests.post(
    f"https://tapi.bale.ai/bot{BALE_TOKEN}/sendMessage",
    data={
        "chat_id": BALE_CHANNEL,
        "text": message
    }
)



# =========================
# ارسال روبیکا
# =========================

requests.post(
    f"https://botapi.rubika.ir/v3/{RUBIK_TOKEN}/sendMessage",
    json={
        "chat_id": RUBIKA_CHANNEL,
        "text": message
    }
)



print(message)
print("USD:",usd)
print("GOLD:",gold18)
