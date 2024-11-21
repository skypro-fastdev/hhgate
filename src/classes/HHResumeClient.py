import json

import aiohttp
from async_property import async_property

from src.config import HH_ACCESS_TOKEN
from utils.search_areas_service import search_areas


class HHResumeClient:

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token

    @async_property
    async def headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.access_token}"}

    async def get_resumes(self) -> str | None:
        url = "https://api.hh.ru/resumes/mine"
        headers = await self.headers
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    response.raise_for_status()
                    content = await response.json()
                    return content
        except Exception as e:
            return f'Произошла ошибка\n {e}'

    async def post_resume(self, student_data) -> str | None:
        url = 'https://api.hh.ru/resumes'
        headers = await self.headers

        # with open('src/classes/test_post_body.json', 'r') as file:
        #     student_data = json.loads(file.read())

        post_body = {
            "birth_date": student_data['student_birth_date'],
            "first_name": student_data['student_first_name'],
            "last_name": student_data['student_last_name'],
            "gender": {
                "id": 'male' if student_data['student_gender'] =='Мужской' else 'female',
            },
            "area":
                {
                    "id": search_areas(student_data['student_location']),
                },
            "citizenship": [
                {
                    "id": "113"
                }],
            "work_ticket": [
                {
                    "id": "113"
                }],
            # TODO need relocation?
            # "relocation": {
            #     "type":
            #         {
            #             "id": "no_relocation"
            #         }
            # },
            # TODO need business_trip_readiness?
            # "business_trip_readiness":
            #     {
            #         "id": "never"
            #     },
            "title": student_data['profession_pretty'],
            # TODO need schedules?
            # "schedules": [
            #     {
            #         "id": "fullDay",
            #         "name": "Полный день"
            #     },
            #     {
            #         "id": "remote",
            #         "name": "Удаленная работа"
            #     }],
            # TODO need travel_time?
            # "travel_time":
            #     {
            #         "id": 'any'
            #     },
            # TODO professional_roles maybe not required
            # "professional_roles": [
            #     {
            #         "id": "165"
            #     }],
            "experience": [
                {
                    "area": {
                        "id": "113"
                    },
                    "company": student_data['previous_job_organisation'],
                    "company_id": None,
                    "company_url": None,
                    "description": student_data['previous_job_experience'],
                    "employer": None,
                    "end": student_data['recent_job_to'],
                    # TODO check out id`s and req fields
                    "industries": [],
                    # TODO maybe industry not required
                    "industry": {
                        "id": "11",
                        "name": "Информационные технологии"
                    },
                    "position": student_data['recent_job_position'],
                    "start": student_data['recent_job_from']
                }],
            "education": {
                "additional": None,
                "attestation": None,
                "elementary": None,
                "level": {
                    "id": "higher",
                    "name": "Высшее"
                },
                "primary": [
                    {
                        "id": None,
                        "name": student_data['education_organisation'],
                        "name_id": None,
                        "organization": "Биотехнология",
                        "organization_id": None,
                        "result": student_data['education_industry'],
                        "result_id": None,
                        "year": int(student_data['education_to'])
                    }]
            },
            "skills": student_data['about'],
            "contact": [
                {
                    "preferred": True,
                    "type": {
                        "id": "email",
                        "name": "Эл. почта"
                    },
                    "value": student_data['student_mail']
                },
                {
                    "comment": None,
                    "need_verification": False,
                    "preferred": False,
                    "type": {
                        "id": "cell",
                        "name": "Мобильный телефон"
                    },
                    "value": {
                        "city": "904",
                        "country": "7",
                        "formatted": "7-000-000-0000",
                        "number": "9048853522"
                    },
                    "verified": False
                }]
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=post_body) as response:
                    response.raise_for_status()
                    content = await response.json()
                    return content.headers['Location']
        except Exception as e:
            return f'Произошла ошибка\n {e}'
