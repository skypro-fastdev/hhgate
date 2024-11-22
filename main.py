import os
import uuid
from typing import Annotated

import uvicorn

from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.params import Form
from starlette.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from src.routers import auth, photo, resume

app = FastAPI()
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.include_router(auth.router)
app.include_router(photo.router)
app.include_router(resume.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", log_level="info")
