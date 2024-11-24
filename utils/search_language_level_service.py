import json

def search_language_level(user_lang_level: str) -> str:
    with open('utils/references/languages_level.json', 'r', encoding='utf-8') as file:
        lang_d = json.loads(file.read())

    for elem in lang_d:
        if elem["id"].lower() == user_lang_level.lower():
            return elem