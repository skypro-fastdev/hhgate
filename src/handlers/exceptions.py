from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.handlers.translations_ref.errors_messages import errors_translations
from src.handlers.translations_ref.fields import fields_translations


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Кастомный обработчик ошибки RequestValidationError status_code 422.
    Срабатывает при передаче некорректного типа данных в поля моделей.
    """
    error_messages = []
    for error in exc.errors():
        field = error["loc"][-1]
        message = error["msg"]

        translate_field = ''
        translate_message = ''

        for key, value in fields_translations.items():
            if key == field:
                translate_field = value
        if not translate_field:
            translate_field = field

        for key, value in errors_translations.items():
            if key == message:
                translate_message = value
        if not translate_message:
            translate_message = message

        error_messages.append(f"{translate_field}: {translate_message}")

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": ".\n".join(error_messages),
        }
    )


async def custom_http_exception_handler(request: Request, exc: HTTPException):
    """
    Кастомный обработчик ошибок HTTPExceptions.
    Взаимодействует с ошибками HTTPExceptions из словаря.
    Отдает статус код и детали необработанных ошибок.
    """
    errors_dict = {
        400: exc.detail,
        403: "Доступ запрещен",
        404: "Кажется, запрашиваемого ресурса не существует",
        408: "Ошибка, долгое ожидание запроса",
        410: "Кажется, запрашиваемый ресурс был удален",
        504: "Ошибка, сервер не отвечает",
        500: "Сервер устал или у нас что то сломалось"
    }
    for status_code, message in errors_dict.items():
        if status_code == exc.status_code:
            return JSONResponse(status_code=status_code, content={"error": message})

    return JSONResponse(status_code=exc.status_code, content=exc.detail)
