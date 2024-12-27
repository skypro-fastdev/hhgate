from typing import Annotated

from fastapi import APIRouter, Form, UploadFile, Request
from fastapi.params import File

from src.classes.HHArtifactsClient import HHArtifactsClient

router = APIRouter(tags=['Артефакты'])


@router.post("/photo/{student_id}")
async def load_photo_till_ready(student_id: int, hh_access_token: Annotated[str, Form()], file: UploadFile = File(...)):

    contents = file.file.read()
    filename = f"uploads/" + str(student_id) + '.' + file.filename.split('.')[-1]
    with open(filename, 'wb') as f:
        f.write(contents)

    client = HHArtifactsClient(hh_access_token)
    upload_result = await client.upload_and_wait_till_ready(filename)
    return upload_result


@router.get("/artifacts/")
async def get_all_artifacts(request: Request):
    request_data = await request.json()
    hh_access_token = request_data.get("hh_access_token")

    client = HHArtifactsClient(hh_access_token)
    all_artifacts = await client.all_photos()
    return all_artifacts
