from fastapi import APIRouter, Request

from src.classes.HHAuth import HHAuth
from src.config import HH_CLIENT_ID, HH_CLIENT_SECRET

router = APIRouter(tags=['Аутентификация'])

@router.post("/auth/")
async def get_auth(request: Request):
    request_data = await request.json()
    hh_code = request_data["hh_code"]
    hh_access_token = HHAuth(
        auth_code=hh_code,
        client_id=HH_CLIENT_ID,
        client_secret=HH_CLIENT_SECRET
    ).connect()["access_token"]
    return {"access_token": hh_access_token}

@router.get("/client_id/")
async def get_client_id(request: Request):
    return {"client_id": HH_CLIENT_ID}
