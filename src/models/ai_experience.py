from pydantic import BaseModel, Field


class AIExpGen(BaseModel):

    student_id: int
    student_gender: str = Field(description='Пол студента', examples=['Мужской'])

    previous_job_organisation: str = Field(description='Организаци(и/я)', examples=['SkyPro'])
    previous_job_position: str = Field(description='Предыдущая специальность', examples=['Веб разработчик'])
    previous_job_industry: str = Field(description='Индустрия предыдущей специальности', examples=['Разработка программного обеспечения'])

    student_location: str = Field(description='Локация студента', examples=['Москва'])
    prompt: str = Field(description='Промпт, который будет обязательно использован при генерации текста', examples=['Напиши, что люблю цветочки'], default=None)