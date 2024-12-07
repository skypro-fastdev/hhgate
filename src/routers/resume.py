from fastapi import APIRouter, HTTPException

from src.classes.HHResumeClient import HHResumeClient
from src.models.student import Student

router = APIRouter()

@router.get("/resumes/")
async def get_all_resumes():
    # response = await hh_res_client.get_resumes()
    # return response
    pass

@router.get("/resume/")
async def post_resume(student: Student):

    if student.hh_access_token is not None:
        hh_access_token = student.hh_access_token
    else:
        raise HTTPException(status_code=403, detail='Wrong HH code')

    hh_res_client = HHResumeClient(access_token=hh_access_token)
    student_dict = student.model_dump()
    response = await hh_res_client.post_resume(student_dict)
    return response
