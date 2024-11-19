import aiohttp
from async_property import async_property

from src.classes.post_body_tmp import post_body


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

    async def post_resume(self) -> str | None:
        url = 'https://api.hh.ru/resumes'
        headers = await self.headers

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=post_body) as response:
                    response.raise_for_status()
                    content = await response.json()
                    return content.headers['Location']
        except Exception as e:
            return f'Произошла ошибка\n {e}'
