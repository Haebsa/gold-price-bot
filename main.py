import requests
import re

html = requests.get(
    "https://www.tgju.org/profile/price_dollar_rl",
    headers={"User-Agent": "Mozilla/5.0"}
).text

for url in re.findall(r'https://[^"\']+', html):
    if "api.tgju.org" in url:
        print(url)
