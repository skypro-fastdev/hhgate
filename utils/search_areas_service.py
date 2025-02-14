import json

def search_areas(user_area: str) -> str:
    with open('utils/references/areas_ref.json', 'r', encoding='utf-8') as file:
        areas_list = json.loads(file.read())

    for elem in areas_list:
        for area in elem['areas']:
            if user_area.lower() in area['name'].lower():
                return area['id']
            else:
                for city in area['areas']:
                    if user_area.lower() in city['name'].lower():
                        return city['id']
