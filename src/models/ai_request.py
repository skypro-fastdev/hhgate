from pydantic import BaseModel, Field


class AIAboutGen(BaseModel):
    student_id: int
    student_gender: str = Field(description='Пол студента', examples=['Мужской'])
    skill_set: list[str] = Field(description='Список навыков', examples=['Python', 'JavaScript'])
    student_qualities: list[str] = Field(description='Список личных качеств', examples=['Ответственность, Пунктуальность'])

    previous_job_position: str = Field(description='Предыдущая специальность', examples=['Инженер по АСУТП'])
    previous_job_industry: str = Field(description='Индустрия предыдущей специальности', examples=['Производство материалов'])

    education_organisation: str = Field(description='Название учебного заведения', examples=['Казанский гос. энергоуниверситет (КГЭУ)'])
    education_industry: str = Field(description='Факультет', examples=['Производство материалов'])

    prompt: str
