import aiohttp
from fastapi import APIRouter, HTTPException
from starlette.requests import Request

from src.config import AI_TOKEN

router = APIRouter(tags=['Генерация текста "О себе"'])


@router.post("/ai/about/")
async def about_ai_gen(request: Request):

    student_data =  await request.json()

    prompt =f"""  
      Напиши текст о себе для профессионального резюме, не указывая опыт и грейд. 
      При написании строго выполняй следующие условия:

      <требования>
      - Пиши в дружелюбном стиле.
      - Пиши коротко и простыми предложениями
      - Пиши без воды
      - Не здоровайся
      - Не представляйся 
      - Не подписывайся
      - Используй активный залог в предложениях (сделал, изучил, создал, разобрался)
      - Не используй пассивный залог (позволило, пришлось, сформировало)
      - Используй гендер {student_data['gender']}
       {student_data['user_prompt']}
      <требования>
      
      Включи в текст:

      Навыки  (200 символов, выбери все из списка)

      <навыки>
      ${student_data['skills']}
      </навыки>

      Личные качества (200 символов, выбери 2-3 из списка:)

      <личные качества>
      ${student_data['qualities']}
      </личные качества>

      Как опыт прошлой профессии и образование помогают в работе (300 символов) 

      <прошлая работа>
      ${student_data['position']} 
      ${student_data['industry']}
      </прошлая работа>

      <образование>
      ${student_data['education_organisation']}
      ${student_data['education_industry']}
      </образование>
      
      - готовность развиваться и интерес к новому (140 символов)

      Начни с самопрезентации (без указания имени)
      """

    req = {
        "model": "gpt-4",
        "messages": [{
            "role": "user",
            "content": f"{prompt}"
        }]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + str(AI_TOKEN)
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url='https://api.openai.com/v1/chat/completions', json=req, headers=headers) as response:
            data = await response.json()
            return {'responce': data['choices'][0]['message']['content']}
