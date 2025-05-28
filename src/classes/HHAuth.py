import requests
from fastapi import HTTPException


class HHAuth:
    def __init__(self, client_id, client_secret, auth_code, user_agent):
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_code = auth_code
        self.user_agent = user_agent

    def connect(self):
        headers = {
            "User-Agent": self.user_agent,
            "Content-Type": "application/x-www-form-urlencoded"  # Changed content type
        }
        # Changed from json to data for form-urlencoded
        data = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": self.auth_code
        }
        try:
            # Changed json=data to data=data
            response = requests.post("https://api.hh.ru/token", headers=headers, data=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            error_message = str(e)
            if e.response is not None:
                error_message += f"\nResponse: {e.response.text}"
            raise Exception(f"Token request failed: {error_message}")
