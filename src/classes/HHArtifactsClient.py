import asyncio

import aiohttp
from async_property import async_property
from fastapi import HTTPException
from loguru import logger


class HHArtifactsClient:

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token

    @async_property
    async def headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.access_token}"}

    async def upload_and_wait_till_ready(self, path):

        photo_id = await self.upload_photo(path)

        if photo_id is None:
            raise HTTPException(status_code= 400, detail={"error": "Cant upload photo"})

        logger.info(f"Uploaded photo {photo_id}")

        for i in range(5):
            await asyncio.sleep(2)
            photo_obj = await self.get_photo_by_id(photo_id)
            state: str = photo_obj["state"]["id"]
            logger.info(f"Fetchin photo {photo_id}: state: {state}")
            if state == "ok":
                return photo_obj

    async def upload_photo(self, path) -> int:

        url = "https://api.hh.ru/artifacts"
        headers = await self.headers
        split_path = '.'.split(path)
        mime_type = split_path[-1]
        valid_mime_types_list = ['jpg', 'jpeg', 'psd', 'png']


        form_data = aiohttp.FormData()
        form_data.add_field('type', 'photo')
        form_data.add_field('file', open(path, 'rb'), filename=path)

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=form_data, ssl=False) as response:

                logger.info(f"Sending {path} to url {url} Status {response.status}")

                if mime_type not in valid_mime_types_list:
                    raise HTTPException(
                        status_code=400,
                        detail='Загружаемая фотография должна быть формата jpeg, jpg, png или psd'
                    )

                if response.status == 201:
                    json_data = await response.json()
                    return json_data["id"]

                if response.status == 400:
                    json_data = await response.json()
                    raise HTTPException(status_code= 400, detail=json_data)


    async def all_photos(self) -> list[dict[str, str]]:
        url = "https://api.hh.ru/artifacts/photo"
        headers = await self.headers
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers,  ssl=False) as response:

                if response.status == 200:
                    json_data = await response.json()
                    return json_data.get("items")

                if response.status == 400:
                    raise HTTPException(response.status, await response.json())

                raise HTTPException(response.status, await response.json())

    async def get_photo_by_id(self, id: int) -> dict[str, str | dict]:
        all_photos = await self.all_photos()
        for photo in all_photos:
            if photo["id"] == id:
                return photo
