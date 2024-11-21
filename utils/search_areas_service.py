import json


def search_areas(user_area: str) -> str:
    with open('utils/areas_ref.json', 'r', encoding='utf-8') as file:
        areas_list = json.loads(file.read())

        # print(type(areas_list))

    for elem in areas_list:
        for area in elem['areas']:
            if area['name'].lower() == user_area.lower():
                return area['id']
            else:
                for city in area['areas']:
                    if city['name'].lower() == user_area.lower():
                        return city['id']
