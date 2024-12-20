from fastapi import APIRouter
from starlette.requests import Request

from src.classes.HHApplicationsClient import HHApplicationClient

router = APIRouter()

@router.post("/applications/")
async def post_application(request: Request):
    hh_access_token = request.headers['hh_access_token']
    hh_app_client = HHApplicationClient(access_token=hh_access_token)
    response = await hh_app_client.post_application(request.json())
    return response
