import requests
import json

url = "https://api.tgju.org/v1/market/list-data?category_ids=28070&extra_data=1&lang=fa"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

print(r.status_code)
print(json.dumps(r.json(), indent=2, ensure_ascii=False)[:6000])
