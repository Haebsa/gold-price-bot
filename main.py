import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

url = "https://www.tgju.org/"

response = requests.get(url, headers=headers, timeout=20)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
text = soup.get_text("\n", strip=True)

lines = text.split("\n")

dollar = None
gold18 = None

for i, line in enumerate(lines):
    if line.strip() == "دلار" and i + 1 < len(lines):
        dollar = lines[i + 1]

    if line.strip() in ["طلا ۱۸", "طلای 18", "طلا 18"] and i + 1 < len(lines):
        gold18 = lines[i + 1]

print("Dollar:", dollar)
print("Gold18:", gold18)
