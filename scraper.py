import requests
from bs4 import BeautifulSoup
import re

headers = {
    "User-Agent": "Mozilla/5.0"
}

URL = "https://www.tgju.org"

def get_prices():
    response = requests.get(URL, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    text = soup.get_text(" ", strip=True)

    prices = {}

    # دلار
    m = re.search(r"دلار\s+([0-9,]+)", text)
    if m:
        prices["dollar"] = int(m.group(1).replace(",", ""))

    # طلای ۱۸ عیار
    m = re.search(r"طلای 18 عیار.*?([0-9,]+)", text)
    if m:
        prices["gold18"] = int(m.group(1).replace(",", ""))

    return prices
