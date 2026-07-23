import requests

url = "https://api.tgju.org/v1/market/list-data?category_ids=28070&extra_data=1&lang=fa"

data = requests.get(url).json()["data"]

for row in data:
    if "geram18" in row[0] or "price_dollar_rl" in row[0]:
        print(row)
