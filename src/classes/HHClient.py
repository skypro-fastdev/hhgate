import requests
from pprint import pprint

from post_body_tmp import post_body
from src.config import HH_ACCESS_TOKEN


class HHClient:

    def __init__(self, access_token: str):
        self.access_token = access_token

    @property
    def headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.access_token}"}

    def load_photo(self) -> dict[str, str]:
        url = "https://api.hh.ru/artifacts"
        headers = self.headers

        data = {'type': 'photo'}
        files = {'file': open('../photo/test_pic_sparrow.jpg', 'rb')}

        response = requests.post(url, headers=headers, data=data, files=files)
        return response.json()

    def get_resumes(self) -> str | None:
        url = "https://api.hh.ru/resumes/mine"
        headers = self.headers

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            content = response.json()
            return content
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def post_resume(self) -> str | None:
        url = 'https://api.hh.ru/resumes'
        headers = self.headers

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


client = HHClient(access_token=HH_ACCESS_TOKEN)
# new_res = client.post_resume()
# pprint(new_res)
# pprint(client.load_photo())
# result = client.get_resumes()
# print(result)
