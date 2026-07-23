import requests

for cid in range(28050, 28090):
    try:
        url = f"https://api.tgju.org/v1/market/list-data?category_ids={cid}&extra_data=1&lang=fa"
        data = requests.get(url, timeout=5).json().get("data", [])

        if data:
            print(f"\n===== Category {cid} =====")
            for row in data[:3]:
                print(row[0])
    except:
        pass
