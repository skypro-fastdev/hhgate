import requests

from src.config import HH_CLIENT_ID, HH_CLIENT_SECRET, HH_AUTH_CODE


class HHAuth:

    def __init__(self, auth_code: str, client_id: str, client_secret: str) -> None:
        self.auth_code = auth_code
        self.client_id = client_id
        self.client_secret = client_secret

    def connect(self):
        url = "https://hh.ru/oauth/token"
        body = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': self.auth_code,
        }

        response = requests.post(url, data=body)

        tokens = response.json()
        print(tokens)

    def primary_auth(self) -> str:
        url = f"https://hh.ru/oauth/authorize?response_type=code&client_id={HH_CLIENT_ID}"

        response = requests.get(url)
        return response.text

hh = HHAuth(
    auth_code=HH_AUTH_CODE,
    client_id=HH_CLIENT_ID,
    client_secret=HH_CLIENT_SECRET
)

hh.connect()
