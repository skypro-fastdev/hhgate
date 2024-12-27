import aiohttp
from typing import Any

from async_property import async_property
from fastapi import HTTPException

ERRORS_LIST = [403, 404, 408, 410, 504, 500]


class HHVacanciesClient:

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token

    @async_property
    async def headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.access_token}"}

    async def post_application(self, message, resume_id, vacancy_id) -> Any:
        url = 'https://api.hh.ru/negotiations'
        headers = await self.headers

        form_data = aiohttp.FormData()
        form_data.add_field(name='message', value=message)
        form_data.add_field(name='resume_id', value=resume_id)
        form_data.add_field(name='vacancy_id', value=vacancy_id)

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=form_data, ssl=False) as response:
                if response.status == 201:
                    content = await response.json(content_type='text/html')
                    return content
                elif response.status in ERRORS_LIST:
                    raise HTTPException(status_code=response.status)


    async def get_vacancy(self, hh_vacancy_id: str) -> str:
        url = f'https://api.hh.ru/vacancies/{hh_vacancy_id}'

        # Хедеры вызывают ошибку 403 на api.hh.ru, временно отключено
        # headers = self.headers

        async with aiohttp.ClientSession() as session:
            # Хедеры вызывают ошибку 403 на api.hh.ru, временно отключено
            async with session.get(url, ssl=False) as response:
                if response.status == 200:
                    content = await response.json()
                    return content
                elif response.status in ERRORS_LIST:
                    raise HTTPException(status_code=response.status)
