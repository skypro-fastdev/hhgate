from fastapi import FastAPI
from src.classes.HHResumeClient import HHResumeClient
from src.config import HH_ACCESS_TOKEN
from src.models.student import Student

app = FastAPI()
hh_res_client = HHResumeClient(access_token=HH_ACCESS_TOKEN)


@app.get("/resumes/")
async def get_all_resumes():
    response = await hh_res_client.get_resumes()
    return response

@app.post("/resume/")
async def post_resume(student: Student):
    student_dict = student.model_dump()
    response = await hh_res_client.post_resume(student_dict)
    return response
