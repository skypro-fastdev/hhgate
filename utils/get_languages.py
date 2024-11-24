import requests
import json

response = requests.get("https://api.hh.ru/languages")

with open('references/languages_list.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, indent=4, ensure_ascii=False)