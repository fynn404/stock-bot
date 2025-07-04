# core/fetch_data.py
import json
import requests

def get_fear_greed_data():
    url = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-GB;q=0.6",
        "if-none-match": 'W/7450644115985830759',
        "origin": "https://edition.cnn.com",
        "priority": "u=1, i",
        "referer": "https://edition.cnn.com/",
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


# if __name__ == "__main__":
#     data = get_fear_greed_data()
#     print(data)
#     with open('data.json', 'w', encoding='utf-8') as f:
#         json.dump(data, f, ensure_ascii=False, indent=4) 
