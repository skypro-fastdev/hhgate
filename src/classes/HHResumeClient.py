from pprint import pprint
from typing import Any
import aiohttp

from fastapi import HTTPException
from utils.search_areas_service import search_areas


class HHResumeClient:

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token

    @property
    def headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.access_token}",  "Content-Type": "application/json"}

    async def get_resumes(self) -> str | None:
        url = "https://api.hh.ru/resumes/mine"
        headers = self.headers
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    response.raise_for_status()
                    content = await response.json()
                    return content
        except Exception as e:
            return f'Произошла ошибка\n {e}'

    async def post_resume(self, student_data) -> Any:
        url = 'https://api.hh.ru/resumes'
        headers = self.headers

        post_body = {
            # "birth_date": student_data['student_birth_date'],
            # "first_name": student_data['student_first_name'],
            # "last_name": student_data['student_last_name'],
            # "gender": { "id": student_data['student_gender'] },
            # "area":
            #     {
            #         "id": search_areas(student_data['student_location']),
            #     },
            # "citizenship": [
            #     {
            #         "id": "113"
            #     }],
            # "work_ticket": [
            #     {
            #         "id": "113"
            #     }],
            # "relocation": {
            #     "type":
            #         {
            #             "id": "no_relocation"
            #         }
            # },
            # "business_trip_readiness":
            #     {
            #         "id": "never"
            #     },
            # "title": student_data['profession_pretty'],
            # "schedules": [
            #     {
            #         "id": "fullDay",
            #         "name": "Полный день"
            #     },
            #     {
            #         "id": "remote",
            #         "name": "Удаленная работа"
            #     }],
            # "travel_time":
            #     {
            #         "id": 'any'
            #     },
            # "professional_roles": [
            #     {
            #         "id": "165"
            #     }],
            # "experience": [
            #
            #     {
            #         "area": {
            #             "id": "113"
            #         },
            #         "company": student_data['recent_job_organisation'],
            #         "company_id": None,
            #         "company_url": None,
            #         "position": student_data['recent_job_position'],
            #         "description": student_data['recent_job_experience'],
            #         "employer": None,
            #         "start": student_data['recent_job_from'],
            #         "end": student_data['recent_job_to'],
            #
            #     },
            #
            #     {
            #         "area": {
            #             "id": "113"
            #         },
            #         "company": student_data['previous_job_organisation'],
            #         "company_id": None,
            #         "company_url": None,
            #         "position": student_data['previous_job_position'],
            #         "description": student_data['previous_job_experience'],
            #         "employer": None,
            #
            #         "start": student_data['previous_job_from'],
            #         "end": student_data['previous_job_to'],
            #
            #     }


            # ],
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
                        "organization": student_data.get('education_faculty'),
                        "organization_id": None,
                        "result": student_data['education_industry'],
                        "result_id": None,
                        "year": student_data['education_to']
                    }]
            },
            # "skills": student_data['about'],

            # "skill_set": student_data['skill_set'],

        #     "contact": [
        #         {
        #             "preferred": False,
        #             "type": {
        #                 "id": "email",
        #                 "name": "Эл. почта"
        #             },
        #             "value": student_data['student_mail'],
        #         },
        #
        #
        #         {
        #             "comment": None,
        #             "need_verification": False,
        #             "preferred": True,
        #             "type": {
        #                 "id": "cell",
        #                 "name": "Мобильный телефон"
        #             },
        #             "value": {
        #                 "city": "904",
        #                 "country": "7",
        #                 "formatted": "7-000-000-0000",
        #                 "number": "8853522"
        #             },
        #             "verified": False
        #         }]
        }

        # Если есть фото – добавляем фото

        if student_data.get('hh_photo_id'):
            post_body["photo"] = {
                "id": student_data.get('hh_photo_id'),
                "small": student_data.get('hh_photo_small'),
                "medium": student_data.get('hh_photo_medium'),
            }


        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=post_body, ssl=False) as response:
                if response.status == 201:
                    return {"hh_id": response.headers.get("Location")}
                elif response.status == 400:
                    error_details = (await response.json())
                    raise HTTPException(status_code=400, detail=error_details)
