import aiohttp
from starlette.exceptions import HTTPException

from src.config import ERROR_HANDLER_LIST


class StudentClient:

    def __init__(self):
        self.error_list = ERROR_HANDLER_LIST

    async def get_student_id(self, student_id):
        url = f'https://script.google.com/macros/s/AKfycbyNkOFyzajb5yC4tGK5KPv6nHD5QpKaZmQhZs_PtDJ6_9YINwvIkb8-vy3nAhU6RmJC/exec?query=/students/{student_id}'

        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, ssl=False) as response:
                if response.status == 200:
                    content = await response.json()
                    return content
                elif response.status in self.error_list:
                    raise HTTPException(status_code=response.status)