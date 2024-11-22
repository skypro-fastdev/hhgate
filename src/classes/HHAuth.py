import requests
from fastapi import HTTPException


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
        if response.status_code in (403, 400):
            error_details = response.json()
            raise HTTPException(status_code=response.status_code, detail=error_details)
        tokens = response.json()
        return tokens
