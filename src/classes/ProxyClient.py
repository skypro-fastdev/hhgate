import aiohttp
from fastapi import HTTPException

from src.config import PROXY_URL, ERROR_HANDLER_LIST


class ProxyClient:

    def __init__(self):
        self.url = PROXY_URL
        self.error_list = ERROR_HANDLER_LIST

    async def get_proxy(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                if response.status == 200:
                    content = await response.json()
                    return content
                elif response.status in self.error_list:
                    raise HTTPException(status_code=response.status)

    async def post_proxy(self, req):
        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, data=req) as response:
                if response.status == 200:
                    content = await response.json()
                    return content
                elif response.status in self.error_list:
                    raise HTTPException(status_code=response.status)
