import os
import requests

#=========================
# تنظیمات
#=========================

BALE_TOKEN = os.environ["BALE_TOKEN"]
RUBIK_TOKEN = os.environ["RUBIK_TOKEN"]

BALE_CHANNEL = "@goldha"
RUBIKA_CHANNEL = "@gold_pric"

BRS_KEY = "YOUR_BRS_API_KEY"

headers = {
    "User-Agent":"Mozilla/5.0"
}

#=========================
# دریافت اطلاعات
#=========================

url = f"https://Api.BrsApi.ir/Market/Gold_Currency.php?key={BRS_KEY}"

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)

exit()
gold = {i["symbol"]:i for i in data["gold"]}
cur = {i["symbol"]:i for i in data["currency"]}

def price(dic,key):
    return f'{dic[key]["price"]:,}'

time = cur["USDT_IRT"]["time"]
date = cur["USDT_IRT"]["date"]

#=========================
# متن پیام
#=========================

message = f"""#قیمت لحظه ای #طلا ، #دلار و ارز 📝

⏰ {date} - ساعت {time}

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

💸 دلار آمریکا : {price(cur,"USD")} تومان
💸 تتر : {price(cur,"USDT_IRT")} تومان
💶 یورو : {price(cur,"EUR")} تومان
💷 پوند انگلیسی : {price(cur,"GBP")} تومان
💵 دلار استرالیا : {price(cur,"AUD")} تومان
💵 دلار کانادا : {price(cur,"CAD")} تومان
💵 درهم امارات : {price(cur,"AED")} تومان
💵 ریال قطر : {price(cur,"QAR")} تومان
💵 افغانی : {price(cur,"AFN")} تومان
💵 یوان چین : {price(cur,"CNY")} تومان
💶 لیر ترکیه : {price(cur,"TRY")} تومان

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

🟡 گرم 18 عیار : {price(gold,"IR_GOLD_18K")} تومان
🟠 گرم 24 عیار : {price(gold,"IR_GOLD_24K")} تومان
🟡 طلای آب شده : {price(gold,"IR_GOLD_MELTED")} تومان
🟡 اونس طلا : {price(gold,"XAUUSD")} دلار

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

🌕 سکه امامی : {price(gold,"IR_COIN_EMAMI")} تومان
🌕 سکه بهار آزادی : {price(gold,"IR_COIN_BAHAR")} تومان
🌕 نیم سکه : {price(gold,"IR_COIN_HALF")} تومان
🌕 ربع سکه : {price(gold,"IR_COIN_QUARTER")} تومان
🌕 سکه گرمی : {price(gold,"IR_COIN_1G")} تومان
"""

#=========================
# ارسال بله
#=========================

requests.post(
    f"https://tapi.bale.ai/bot{BALE_TOKEN}/sendMessage",
    data={
        "chat_id":BALE_CHANNEL,
        "text":message+"\n\n📢 @goldha"
    }
)

#=========================
# ارسال روبیکا
#=========================

requests.post(
    f"https://botapi.rubika.ir/v3/{RUBIK_TOKEN}/sendMessage",
    json={
        "chat_id":RUBIKA_CHANNEL,
        "text":message+"\n\n📢 @gold_pric"
    }
)

print("Done")
