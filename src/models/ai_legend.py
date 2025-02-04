from pydantic import BaseModel, Field


class AILegendGen(BaseModel):

    student_id: int
    legend_type: str = Field(description='Тип легенды: стажировка, фриланс или работа в компании', examples=['INTERNSHIP'])
    student_gender: str = Field(description='Пол студента', examples=['Мужской'])
    skill_set: list[str] = Field(description='Список навыков', examples=[['Python', 'JavaScript']])

    previous_job_organisation: str = Field(description='Организация', examples=['SkyPro'])
    previous_job_position: str = Field(description='Предыдущая специальность', examples=['Веб разработчик'])

    student_projects: list = Field(description='Проекты студента', examples=[['Дешифровальная машина', 'Зверенаклонитель', 'Стабилизатор стресса']], default=None)
    student_cases: list = Field(description='Достижения студента', examples=[['Познал дзен программирования', 'Научился пользоваться f строкой']], default=None)
    previous_job_industry: str = Field(description='Индустрия предыдущей специальности', examples=['Разработка программного обеспечения'], default=None)
    student_location: str = Field(description='Локация студента', examples=['Москва'], default=None)
    prompt: str = Field(description='Промпт, который будет обязательно использован при генерации текста', examples=['Напиши, что люблю цветочки'], default=None)