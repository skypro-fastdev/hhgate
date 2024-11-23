import json

def search_education_level(user_education: str) -> str:
    with open('education_level.json', 'r', encoding='utf-8') as file:
        education_d = json.loads(file.read())

    for elem in education_d:
        if elem["id"] == user_education:
            return elem
