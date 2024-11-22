import os
import uuid
from typing import Annotated

import uvicorn

from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.params import Form
from starlette.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from src.classes.HHArtifactsClient import HHArtifactsClient
from src.classes.HHAuth import HHAuth
from src.classes.HHResumeClient import HHResumeClient
from src.config import HH_CLIENT_ID, HH_CLIENT_SECRET
from src.models.student import Student

app = FastAPI()
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/auth/")
async def get_auth(request: Request):
    request_data = await request.json()
    hh_code = request_data["hh_code"]
    hh_access_token = HHAuth(
        auth_code=hh_code,
        client_id=HH_CLIENT_ID,
        client_secret=HH_CLIENT_SECRET
    ).connect()['access_token']
    return {"access_token": hh_access_token}

@app.get("/resumes/")
async def get_all_resumes():
    # response = await hh_res_client.get_resumes()
    # return response
    pass
@app.post("/resume/")
async def post_resume(student: Student):
    if student.hh_access_token is not None:
        hh_access_token = student.hh_access_token
    else:
        try:
            hh_access_token = HHAuth(
                auth_code=student.hh_code,
                client_id=HH_CLIENT_ID,
                client_secret=HH_CLIENT_SECRET
            ).connect()['access_token']
        except Exception as e:
            raise HTTPException(status_code=403, detail='Wrong HH code')

    hh_res_client = HHResumeClient(access_token=hh_access_token)
    student_dict = student.model_dump()
    response = await hh_res_client.post_resume(student_dict)
    return response

@app.post("/photo/{student_id}")
async def load_photo_till_ready(student_id: int, hh_access_token: Annotated[str, Form()], file: UploadFile = File(...)):

    contents = file.file.read()
    filename = f"uploads/" + str(student_id) + '.' + file.filename.split('.')[-1]
    with open(filename, 'wb') as f:
        f.write(contents)

    client = HHArtifactsClient(hh_access_token)
    upload_result = await client.upload_and_wait_till_ready(filename)
    return upload_result


@app.get("/artifacts/")
async def get_all_artifacts(request: Request):
    request_data = await request.json()
    hh_access_token = request_data.get("hh_access_token")

    client = HHArtifactsClient(hh_access_token)
    all_artifacts = await client.all_photos()
    return all_artifacts


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", log_level="info")
