from fastapi import APIRouter
from starlette.requests import Request

from src.classes.AIClient import AIClient
from src.models.ai_request import AIAboutGen

router = APIRouter(tags=['Генерация текста "О себе"'])

@router.post("/ai/about/")
async def about_ai_gen(student_data: AIAboutGen):
    ai_about_gen = AIClient()
    about_dict = student_data.model_dump()
    response = await ai_about_gen.post_ai_about(about_dict)
    return response

@router.post("/ai/legend/")
async def legend_ai_gen(request: Request):
    ai_legend_gen = AIClient()
    student_data = await request.json()
    response = await ai_legend_gen.post_ai_legend(student_data)
    return response


