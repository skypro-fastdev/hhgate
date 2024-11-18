import requests
import json

response = requests.get("https://api.hh.ru/professional_roles")

with open('prof_roles.json', 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, indent=4, ensure_ascii=False)