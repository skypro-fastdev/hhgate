import requests
import asyncio
import aiohttp
import aiofiles

from async_property import async_property

from src.classes.post_body_tmp import post_body
from src.config import HH_ACCESS_TOKEN


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
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            content = response.json()
            return content
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    async def post_resume(self) -> str | None:
        url = 'https://api.hh.ru/resumes'
        headers = await self.headers

        try:
            response = requests.post(
                url=url,
                headers=headers,
                json=post_body
            )

            return response.headers["Location"]
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None


client = HHResumeClient(access_token=HH_ACCESS_TOKEN)
