from fastapi import APIRouter
from starlette.requests import Request

from src.classes.ProxyClient import ProxyClient

router = APIRouter(tags=['Прокси'])

@router.get("/proxy/")
async def get_proxy(request: Request):
    proxy_client = ProxyClient()
    response = await proxy_client.get_proxy()
    return response

@router.post("/proxy/")
async def post_proxy(request: Request):
    proxy_client = ProxyClient()
    req_body = await request.body()
    response = await proxy_client.post_proxy(req_body)
    return response
