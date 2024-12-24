import aiohttp
from typing import Any
from fastapi import HTTPException

ERRORS_LIST = [403, 404, 408, 410, 504, 500]


class HHVacanciesClient:

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token

    @property
    def headers(self) -> dict[str, str]:
        return {'Authorization': f'Bearer {self.access_token}",  "Content-Type": "application/json'}

    async def post_application(self, student_data) -> Any:
        url = 'https://api.hh.ru/negotiations'
        headers = self.headers

        print(student_data)

        post_body = {
            'message': student_data['message'],
            'resume_id': student_data['resume_id'],
            'vacancy_id': student_data['vacancy_id']
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=post_body, ssl=False) as response:
                if response.status == 200:
                    content = await response.json()
                    return content
                elif response.status in ERRORS_LIST:
                    raise HTTPException(status_code=response.status)

    async def get_vacancy(self, hh_vacancy_id: str) -> str:
        url = f'https://api.hh.ru/vacancies/{hh_vacancy_id}'
        # headers = self.headers

        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as response:
                if response.status == 200:
                    content = await response.json()
                    return content
                elif response.status in ERRORS_LIST:
                    raise HTTPException(status_code=response.status)
                # else:
                #     content = await response.json()
                #     return content
