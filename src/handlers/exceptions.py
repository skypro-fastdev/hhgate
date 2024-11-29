from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


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
