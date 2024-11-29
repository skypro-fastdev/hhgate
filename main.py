import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError, HTTPException
from starlette import status
from starlette.responses import JSONResponse
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

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_messages = []
    for error in exc.errors():
        field = error["loc"][-1]
        message = error["msg"]
        error_messages.append(f"{field}: {message}")

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": ".\n".join(error_messages),
        }
    )

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    errors_dict = {
        400: exc.detail,
        403: "Доступ запрещен",
        408: "Ошибка, долгое ожидание запроса",
        504: "Ошибка, сервер не отвечает",
        500: "Сервер устал или у нас что то сломалось"
    }
    for status_code, message in errors_dict.items():
        if status_code == exc.status_code:
            return JSONResponse(status_code=status_code, content={"error": message})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", log_level="info")
