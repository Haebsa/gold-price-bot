import requests

for cid in [28069, 28070, 28071, 28072, 28073]:
    print("=" * 50)
    print("Category:", cid)

    url = f"https://api.tgju.org/v1/market/list-data?category_ids={cid}&extra_data=1&lang=fa"

    try:
        data = requests.get(url).json()["data"]

        for row in data[:5]:
            print(row[0])

    except Exception as e:
        print(e)
