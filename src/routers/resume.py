from fastapi import APIRouter, HTTPException
from starlette.requests import Request

from src.classes.HHResumeClient import HHResumeClient
from src.models.student import Student
from utils.decorators.check_headers_decorator import check_access_token

router = APIRouter(tags=['Резюме'])

@router.get("/resumes/")
@check_access_token
async def get_all_resumes(request: Request):
    hh_access_token = request.headers['hh_access_token']
    hh_res_client = HHResumeClient(access_token=hh_access_token)
    response = await hh_res_client.get_resumes()
    return response

@router.get("/resumes/{hh_resume_id}")
@check_access_token
async def get_resume(request: Request, hh_resume_id: str):
    hh_access_token = request.headers['hh_access_token']
    hh_res_client = HHResumeClient(access_token=hh_access_token)
    response = await hh_res_client.get_current_resume(hh_resume_id)
    return response

@router.get("/my_vacancies/{hh_resume_id}/")
@check_access_token
async def get_similar_vacancies(request: Request, hh_resume_id: str):
    hh_access_token = request.headers['hh_access_token']
    hh_res_client = HHResumeClient(access_token=hh_access_token)
    response = await hh_res_client.get_similar_vacancies(hh_resume_id)
    return response

@router.post("/resume/")
async def post_resume(student: Student):

    if student.hh_access_token is not None:
        hh_access_token = student.hh_access_token
    else:
        raise HTTPException(status_code=403)

    hh_res_client = HHResumeClient(access_token=hh_access_token)
    student_dict = student.model_dump()
    response = await hh_res_client.post_resume(student_dict)
    return response
