import requests
import json

response = requests.get("https://api.hh.ru/dictionaries")

with open('fields_ref.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, indent=4, ensure_ascii=False)
