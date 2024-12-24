import aiohttp
from typing import Any
from fastapi import HTTPException

from src.classes.HHResumeBuilder import HHResumeBuilder

ERRORS_LIST = [403, 404, 408, 410, 504, 500]


class HHResumeClient:

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token

    @property
    def headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.access_token}",  "Content-Type": "application/json"}

    async def get_resumes(self) -> str | None:
        url = "https://api.hh.ru/resumes/mine"
        headers = self.headers
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, ssl=False) as response:
                if response.status == 200:
                    content = await response.json()
                    return content
                elif response.status in ERRORS_LIST:
                    raise HTTPException(status_code=response.status)

    async def get_current_resume(self, hh_resume_id: str) -> str:
        url = f"https://api.hh.ru/resumes/{hh_resume_id}"
        headers = self.headers
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, ssl=False) as response:
                if response.status == 200:
                    content = await response.json()
                    return content
                elif response.status in ERRORS_LIST:
                    raise HTTPException(status_code=response.status)

    async def get_similar_vacancies(self, hh_resume_id: str) -> str:
        url = f"https://api.hh.ru/resumes/{hh_resume_id}/similar_vacancies"
        headers = self.headers
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, ssl=False) as response:
                if response.status == 200:
                    content = await response.json()
                    return content
                elif response.status in ERRORS_LIST:
                    raise HTTPException(status_code=response.status)

    async def post_resume(self, student_data) -> Any:
        url = 'https://api.hh.ru/resumes'
        headers = self.headers

        resume_builder = HHResumeBuilder()
        resume_builder.set_profession(
            title=student_data['profession_pretty'],
            professional_roles=student_data['professional_roles']
        )
        resume_builder.add_education(education=
        {
            'education_level': student_data['education_level'],
            'education_organisation': student_data['education_organisation'],
            'education_to': student_data['education_to'],
            'education_faculty': student_data['education_faculty'],
            'education_industry': student_data['education_industry']
        })
        if student_data['previous_job_position']:
            resume_builder.add_experience(experience=
            {
                'organisation': student_data['previous_job_organisation'],
                'position': student_data['previous_job_position'],
                'job_experience': student_data['previous_job_experience'],
                'job_from': student_data['previous_job_from'],
                'job_to': student_data['previous_job_to']
            })
        if student_data['recent_job_position']:
            resume_builder.add_experience(experience=
            {
                'organisation': student_data['recent_job_organisation'],
                'position': student_data['recent_job_position'],
                'job_experience': student_data['recent_job_experience'],
                'job_from': student_data['recent_job_from'],
                'job_to': student_data['recent_job_to']
            })
        if student_data['student_mail']:
            resume_builder.add_contact(contact=
            {
                'student_mail': student_data['student_mail']
            })
        if student_data['student_phone']:
            resume_builder.add_contact(contact={
                'student_phone': student_data['student_phone']
            })
        resume_builder.add_skill(skills_list=student_data['skill_set'])
        resume_builder.set_about_info(about=student_data['about'])
        if student_data.get('hh_photo_id'):
            resume_builder.add_photo(photo=
            {
                "id": student_data.get('hh_photo_id'),
                "small": student_data.get('hh_photo_small'),
                "medium": student_data.get('hh_photo_medium'),
            })
        resume_builder.set_location(
            area=student_data['student_location']
        )
        resume_builder.set_personal_data(
            birth_date=student_data['student_birth_date'],
            first_name=student_data['student_first_name'],
            last_name=student_data['student_last_name'],
            gender=student_data['student_gender']
        )
        resume_builder.add_languages(student_data['student_english_level'])

        post_body = resume_builder.build()

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=post_body, ssl=False) as response:
                if response.status == 201:
                    return {'hh_id': response.headers.get('Location')}
                elif response.status == 400:
                    errors_description = []
                    error_details = (await response.json())
                    for items in error_details['errors']:
                        errors_description.append(' '.join(['Ошибка,', items['value'], items['description']]))
                    raise HTTPException(status_code=400, detail=errors_description)
                elif response.status in ERRORS_LIST:
                    raise HTTPException(status_code=response.status)
