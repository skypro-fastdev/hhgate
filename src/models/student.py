from datetime import date
from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationError


class Student(BaseModel):
    student_id: int
    student_gender: str = Field(description='Пол')
    student_first_name: str = Field(description='Имя')
    student_last_name: str = Field(description='Фамилия')
    student_birth_date: date = Field(description='Дата рождения в формате ГГГГ-ММ-ДД')
    student_english_level: date = Field(description='Уровень владения английским языком, например A1')

    profession: date = Field(description='Профессия')
    profession_pretty: str = Field(description='Название профессии')
    about: str = Field(description='О себе')
    skill_set: str = Field(description='Список навыков')

    student_mail: EmailStr = Field(description='Электронная почта')
    student_phone: str = Field(description='Номер телефона в международном формате, например 7955-555-5555')
    student_tg: str = Field(description='Имя профиля в телеграмм, например @my_telegram')

    student_age: str = Field(description='Возраст')
    student_location: str = Field(description='Город проживания')
    student_motivation: str = Field(description='Мотивация для смены работы')

    recent_job_type: str = Field(description='Тип истории')
    recent_job_organisation: str = Field(description='Название')
    recent_job_position: str = Field(description='Должность')
    recent_job_industry: str = Field(description='Индустрия')
    recent_job_from: str = Field(description='Даты работы')
    recent_job_to: str = Field(description='Настройка к промпту')
    recent_job_experience: str = Field(description='Достижения')
    recent_job_prompt: str = Field(description='Промпт')

    previous_job_type: str = Field(description='Тип истории')
    previous_job_organisation: str = Field(description='Название')
    previous_job_position: str = Field(description='Должность')
    previous_job_industry: str = Field(description='Индустрия')
    previous_job_from: str = Field(description='Даты работы')
    previous_job_to: str = Field(description='Настройка к промпту')
    previous_job_experience: str = Field(description='Достижения')
    previous_job_prompt: str = Field(description='Промпт')

    education_organisation: str = Field(description='Название учебного заведения')
    education_from: str = Field(description='Начало обучения')
    education_to: str = Field(description='Конец обучения')
    education_industry: str = Field(description='Отрасль / Специальность')

    vacancy_link: str = Field(description='Ссылка на вакансию')
    cover: str = Field(description='Сопроводительное письмо')

    # photo: str = Field(description='Фото')

    hh_id: str = Field(description='id пользователя на HH')
    hh_token: str = Field(description='Токен HH')
    hh_photo_id: str = Field(description='ID фото на HH')
    hh_portfolio_id: str = Field(description='ID портфолио на HH')
    hh_vacancy_url: str = Field(description='URL вакансии')
    hh_vacancy_id: str = Field(description='ID вакансии')
    checklist: str = Field(description='Чеклист с проверкой')

    # TODO create birth_date validator