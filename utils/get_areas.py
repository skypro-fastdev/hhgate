import requests
import json

response = requests.get("https://api.hh.ru/areas")

with open('references/areas_ref.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, indent=4, ensure_ascii=False)
