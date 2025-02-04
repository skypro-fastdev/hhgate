from pydantic import BaseModel, Field


class Student(BaseModel):
    student_id: int
    student_gender: str = Field(description='Пол', examples=['male'])
    student_first_name: str = Field(description='Имя', examples=['Василий'])
    student_last_name: str = Field(description='Фамилия', examples=['Теркин'])
    student_birth_date: str = Field(description='Дата рождения в формате ГГГГ-ММ-ДД', examples=['2000-05-05'])
    student_english_level: str = Field(description='Уровень владения английским языком, например A1', examples=['B1'])

    profession: str = Field(description='Профессия', examples=['Аналитик данных'])
    profession_pretty: str = Field(description='Название профессии', examples=['Аналитик'])
    professional_roles: list[str] = Field(description='Профессиональные роли', examples=['165'])
    about: str = Field(description='О себе', examples=['Я ответственный и квалифицированный работник'])
    skill_set: list[str] = Field(description='Список навыков', default_factory=list, examples=['Python'])

    student_mail: str = Field(description='Электронная почта', examples=['my_email@example.com'])
    student_phone: str = Field(description='Номер телефона в международном формате, например 7955-555-5555', examples=['7955-555-5555'])
    student_tg: str = Field(description='Имя профиля в телеграмм, например @my_telegram', examples=['@my_telegram'])

    student_age: str = Field(description='Возраст', examples=['24'])
    student_location: str = Field(description='Город проживания', examples=['Москва'])
    student_motivation: str = Field(description='Мотивация для смены работы', examples=['Желание достичь новых вершин'])

    recent_job_type: str = Field(description='Тип истории', examples=['Настоящая'])
    recent_job_organisation: str = Field(description='Название', examples=['AlmostGgle'])
    recent_job_position: str = Field(description='Должность', examples=['Аналитик данных'])
    recent_job_industry: str = Field(description='Индустрия', examples=['Информационные технологии'])
    recent_job_from: str = Field(description='Дата начала работы', examples=['2022-01-01'])
    recent_job_to: str = Field(description='Дата завершения работы', examples=['2022-10-10'])
    recent_job_experience: str = Field(description='Достижения', examples=['Самый первый сдаю работу'])
    recent_job_prompt: str = Field(description='Промпт', examples=['Промпт'])

    previous_job_type: str = Field(description='Тип истории', examples=['Настящая'])
    previous_job_organisation: str = Field(description='Название', examples=['CompService'])
    previous_job_position: str = Field(description='Должность', examples=['Младший ремонтник'])
    previous_job_industry: str = Field(description='Индустрия', examples=['Сервис'])
    previous_job_from: str = Field(description='Дата начала работы', examples=['2020-01-01'])
    previous_job_to: str = Field(description='Дата завершения работы', examples=['2022-01-01'])
    previous_job_experience: str = Field(description='Достижения', examples=['Починил кучу техники'])
    previous_job_prompt: str = Field(description='Промпт', examples=['Промпт'])

    education_organisation: str = Field(description='Название учебного заведения', examples=['Московский физтех институт'])
    education_from: str = Field(description='Год начала обучения', examples=['2015'])
    education_to: str = Field(description='Год конца обучения', examples=['2020'])
    education_industry: str = Field(description='Отрасль / Специальность', examples=['Инженер'])
    education_level: str = Field(description='Уровень образования', examples=['higher'])

    # photo: str = Field(description='Фото')

    # hh_id: str = Field(description='id пользователя на HH')
    hh_code: str = Field(description='Токен HH', examples=['UED57880JHG4212KLDFKGK2JH5KJHKJFLHKDJJKVCLKJHGLHJKEWOI4090943832IOP2'])
    hh_portfolio_id: str = Field(description='ID портфолио на HH', examples=['k34is345dop3950fkd93pwdif903elkc9f'])
    hh_photo_id: str | None = Field(description='ID фото на HH', default=None, examples=['123'])
    education_faculty: str = Field(description='Факультет', default=None, examples=['Физико-технологический'])
    # hh_vacancy_url: str = Field(description='URL вакансии')
    # hh_vacancy_id: str = Field(description='ID вакансии')

    # checklist: str = Field(description='Чеклист с проверкой')

    hh_access_token: str | None = Field(default=None, examples=['USER173484RKF89F0FVBMERJK3K3IF87VG8RLOFD9VFIFRJKR'])
