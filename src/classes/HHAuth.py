import requests




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
        print(body)

        response = requests.post(url, data=body)
        print(response.status_code, response.content)

        tokens = response.json()
        return tokens
