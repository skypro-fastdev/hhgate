from fastapi import APIRouter

from src.classes.AIClient import AIClient
from src.models.ai_about import AIAboutGen
from src.models.ai_experience import AIExpGen
from src.models.ai_legend import AILegendGen

router = APIRouter(tags=['Генерация текста'])

@router.post("/ai/about/")
async def about_ai_gen(student_data: AIAboutGen):
    ai_about_gen = AIClient()
    about_dict = student_data.model_dump()
    response = await ai_about_gen.post_ai_about(about_dict)
    return response

@router.post("/ai/legend/")
async def legend_ai_gen(student_data: AILegendGen):
    ai_legend_gen = AIClient()
    legend_dict = student_data.model_dump()
    response = await ai_legend_gen.post_ai_legend(legend_dict)
    return response

@router.post("/ai/experience/")
async def experience_ai_gen(student_data: AIExpGen):
    ai_exp_gen = AIClient()
    exp_dict = student_data.model_dump()
    response = await ai_exp_gen.post_ai_experience(exp_dict)
    return response
