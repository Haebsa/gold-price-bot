import requests
import re

url = "https://www.tgju.org/profile/price_dollar_rl"

headers = {
    "User-Agent": "Mozilla/5.0"
}

html = requests.get(url, headers=headers).text

for x in [
    "api.tgju.org",
    "__NEXT_DATA__",
    "price",
    "fetch(",
    "axios",
    "market"
]:
    print("======", x)
    print(x in html)
