from typing import Annotated

from fastapi import APIRouter, Form
from starlette.requests import Request

from src.classes.HHVacanciesClient import HHVacanciesClient
from utils.decorators.check_headers_decorator import check_access_token

router = APIRouter(tags=['Вакансии'])

@router.post("/applications/")
@check_access_token
async def post_application(request: Request, message: Annotated[str, Form()], resume_id: Annotated[str, Form()], vacancy_id: Annotated[str, Form()]):
    hh_access_token = request.headers['hh_access_token']
    hh_app_client = HHVacanciesClient(access_token=hh_access_token)
    response = await hh_app_client.post_application(message, resume_id, vacancy_id)
    return response

@router.get("/vacancies/{hh_vacancy_id}/")
@check_access_token
async def get_vacancy(request: Request, hh_vacancy_id):
    hh_access_token = request.headers['hh_access_token']
    hh_app_client = HHVacanciesClient(access_token=hh_access_token)
    response = await hh_app_client.get_vacancy(hh_vacancy_id)
    return response
