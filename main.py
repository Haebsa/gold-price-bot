import requests

url = "https://www.tgju.org/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print(response.text[:1000])
