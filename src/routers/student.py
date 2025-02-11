from fastapi import APIRouter
from starlette.requests import Request

from src.classes.StudentClient import StudentClient

router = APIRouter(tags=['Студент'])

@router.get("/students/{student_id}")
async def get_student_id(request: Request, student_id):
    student_client = StudentClient()
    response = await student_client.get_student_id(student_id)
    return response