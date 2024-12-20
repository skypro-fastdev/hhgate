import aiohttp
from typing import Any
from fastapi import HTTPException


class HHApplicationClient:

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token

    @property
    def headers(self) -> dict[str, str]:
        return {'Authorization': f'Bearer {self.access_token}",  "Content-Type": "application/json'}

    async def post_application(self, student_data) -> Any:
        url = 'https://api.hh.ru/negotiations'
        headers = self.headers

        post_body = {
            'message': f'{student_data.message}',
            'resume_id': f'{student_data.resume_id}',
            'vacancy_id': f'{student_data.vacancy_id}'
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=post_body, ssl=False) as response:
                errors_list = [403, 408, 504, 500]
                if response.status == 200:
                    content = await response.json()
                    return content
                elif response.status in errors_list:
                    raise HTTPException(status_code=response.status)
