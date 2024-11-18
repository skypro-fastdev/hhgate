import requests

from src.config import HH_CLIENT_ID, HH_CLIENT_SECRET


class HHAuth:

    def __init__(self, client_id: str, client_secret: str) -> None:
        self.auth_code = self.primary_auth()
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
    client_id=HH_CLIENT_ID,
    client_secret=HH_CLIENT_SECRET
)

hh.connect()
