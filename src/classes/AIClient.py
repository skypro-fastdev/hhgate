import aiohttp
from src.config import AI_ADDRESS, AI_TOKEN


class AIClient:

    async def post_ai_about(self, student_data):
        url = AI_ADDRESS
        ai_token = AI_TOKEN

        prompt = f"""  
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
              - Используй гендер {student_data['student_gender']}
               {student_data['prompt']}
              <требования>

              Включи в текст:

              Навыки  (200 символов, выбери все из списка)

              <навыки>
              ${student_data['skill_set']}
              </навыки>

              Личные качества (200 символов, выбери 2-3 из списка:)

              <личные качества>
              ${student_data['student_qualities']}
              </личные качества>

              Как опыт прошлой профессии и образование помогают в работе (300 символов) 

              <прошлая работа>
              ${student_data['previous_job_position']} 
              ${student_data['previous_job_industry']}
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
            "Authorization": "Bearer " + str(ai_token)
        }


        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, json=req, ssl=False, headers=headers) as response:
                data = await response.json()
                return {'response': data['choices'][0]['message']['content']}
