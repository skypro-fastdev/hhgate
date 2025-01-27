import aiohttp
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from starlette.requests import Request

from src.classes.AIClient import AIClient
from src.config import AI_TOKEN, AI_ADDRESS
from src.models.ai_request import AIAboutGen

router = APIRouter(tags=['Генерация текста "О себе"'])
ai_address = AI_ADDRESS

@router.post("/ai/about/")
async def about_ai_gen(student_data: AIAboutGen):
    ai_about_gen = AIClient()
    about_dict = student_data.model_dump()
    response = await ai_about_gen.post_ai_about(about_dict)
    return response
