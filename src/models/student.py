from pydantic import BaseModel, Field


class Student(BaseModel):
    student_id: int
    student_gender: str = Field(description='Пол')
    student_first_name: str = Field(description='Имя')
    student_last_name: str = Field(description='Фамилия')
    student_birth_date: str = Field(description='Дата рождения в формате ГГГГ-ММ-ДД')
    student_english_level: str = Field(description='Уровень владения английским языком, например A1')

    profession: str = Field(description='Профессия')
    profession_pretty: str = Field(description='Название профессии')
    professional_roles: list[str] = Field(description='Профессиональные роли')
    about: str = Field(description='О себе')
    skill_set: list[str] = Field(description='Список навыков', default_factory=list)

    student_mail: str = Field(description='Электронная почта')
    student_phone: str = Field(description='Номер телефона в международном формате, например 7955-555-5555')
    student_tg: str = Field(description='Имя профиля в телеграмм, например @my_telegram')

    student_age: str = Field(description='Возраст')
    student_location: str = Field(description='Город проживания')
    student_motivation: str = Field(description='Мотивация для смены работы')

    recent_job_type: str = Field(description='Тип истории')
    recent_job_organisation: str = Field(description='Название')
    recent_job_position: str = Field(description='Должность')
    recent_job_industry: str = Field(description='Индустрия')
    recent_job_from: str = Field(description='Дата начала работы')
    recent_job_to: str = Field(description='Дата завершения работы')
    recent_job_experience: str = Field(description='Достижения')
    recent_job_prompt: str = Field(description='Промпт')

    previous_job_type: str = Field(description='Тип истории')
    previous_job_organisation: str = Field(description='Название')
    previous_job_position: str = Field(description='Должность')
    previous_job_industry: str = Field(description='Индустрия')
    previous_job_from: str = Field(description='Дата начала работы')
    previous_job_to: str = Field(description='Дата завершения работы')
    previous_job_experience: str = Field(description='Достижения')
    previous_job_prompt: str = Field(description='Промпт')

    education_organisation: str = Field(description='Название учебного заведения')
    education_from: str = Field(description='Год начала обучения')
    education_to: str = Field(description='Год конца обучения')
    education_industry: str = Field(description='Отрасль / Специальность')
    education_level: str = Field(description='Уровень образования')

    hh_code: str = Field(description='Токен HH')
    hh_portfolio_id: str = Field(description='ID портфолио на HH')
    hh_photo_id: str | None = Field(description='ID фото на HH', default=None)
    education_faculty: str = Field(description='Факультет', default=None)

    legend_on: bool = Field(description='Включена ли легенда')

    hh_access_token: str | None = Field(default=None)

    # TODO create birth_date validator
