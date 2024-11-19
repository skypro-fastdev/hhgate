import aiohttp
import requests
from async_property import async_property


class HHArtifactsClient:

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token

    @async_property
    async def headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.access_token}"}

    async def load_photo(self) -> dict[str, str]:
        url = "https://api.hh.ru/artifacts"
        headers = await self.headers
        req_data = {
            'type': 'photo',
            'file': open('src/photo/test_pic_sparrow.jpg', 'rb')
        }

        async with aiohttp.ClientSession() as session:
            with aiohttp.MultipartWriter('form-data') as mp:
                for k, v in req_data.items():
                    part = mp.append(v)
                    part.set_content_disposition('form-data', name=k)
            async with session.post(url, headers=headers, data=mp) as response:
                json_data = await response.json()
                return json_data
