import requests

urls = {
    "dollar": "https://www.tgju.org/profile/price_dollar_rl",
    "gold18": "https://www.tgju.org/profile/geram18"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

for name, url in urls.items():
    r = requests.get(url, headers=headers)
    print("=" * 40)
    print(name)
    print(r.status_code)
    print(r.text[:1500])
