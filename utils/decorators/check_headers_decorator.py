from functools import wraps
from typing import Callable

from fastapi import HTTPException
from starlette.requests import Request

def check_access_token(func: Callable):
    @wraps(func)
    async def _wrapper(*args, **kwargs):
        request: Request = kwargs.get("request")
        if 'hh_access_token' not in request.headers:
            raise HTTPException(status_code=403)
        return await func(*args, **kwargs)
    return _wrapper
