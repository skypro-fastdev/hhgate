import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
from starlette.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from src.handlers.exceptions import validation_exception_handler, custom_http_exception_handler
from src.routers import auth, photo, resume, vacancy, llm, student, proxy

app = FastAPI()
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.include_router(auth.router)
app.include_router(photo.router)
app.include_router(resume.router)
app.include_router(vacancy.router)
app.include_router(llm.router)
app.include_router(student.router)
app.include_router(proxy.router)

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, custom_http_exception_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", log_level="info")
