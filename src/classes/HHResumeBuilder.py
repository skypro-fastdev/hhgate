from typing import Any

from utils.search_areas_service import search_areas
from utils.search_education_level_service import search_education_level
from utils.search_language_level_service import search_language_level


class HHResumeBuilder:
    """
    Класс Строитель тела POST запроса для HHResumeClient
    """

    def __init__(self):
        self.body_fields = {
            "birth_date": None,
            "first_name": None,
            "last_name": None,
            "gender": {},
            "area": {},
            "citizenship": [],
            "work_ticket": [],
            "relocation": {},
            "business_trip_readiness": {},
            "title": None,
            "schedules": [],
            "travel_time": {},
            "photo": {},
            "professional_roles": [],
            "experience": [],
            "education": {},
            "skills": None,
            "skill_set": [],
            "contact": [],
            "language": []
        }

    def build(self) -> dict[str, Any]:
        """
        Метод сборки всех полей, возвращает готовый словарь со всеми полями
        """
        inst = self.body_fields
        return inst

    def set_profession(self,
                       title: str,
                       professional_roles: list[str] | None,
                       schedules: list[dict[str, str]] | None=None,
                       travel_time: dict[str, str] | None=None) -> None:
        """
        Добавляет поля:
            - Название желаемой профессии
            - Желаемую профессиональную роль
            - Желаемый график работы
            - Желаемое время в пути
        """
        if schedules is None:
            schedules = [
                {
                    "id": "fullDay",
                    "name": "Полный день"
                },
                {
                    "id": "remote",
                    "name": "Удаленная работа"
                }]
        if travel_time is None:
            travel_time = {"id": 'any'}

        self.body_fields["title"] = title
        self.body_fields["schedules"] = schedules
        self.body_fields["travel_time"] = travel_time

        for p_role in professional_roles:
            self.body_fields["professional_roles"].append({"id":p_role})

    def add_education(self, education: dict[str, str | int]) -> None:
        """
        Добавляет поля:
            - Информацию об образовании
        """
        secondary_education_list = ["secondary", "special_secondary"]
        higher_education_list = ["unfinished_higher", "higher", "bachelor", "master", "candidate", "doctor"]

        if education["education_level"].lower() in secondary_education_list:
            self.body_fields["education"] = {
                "additional": None,
                "attestation": None,
                "elementary": [
                    {
                    "name": education['education_organisation'],
                    "year": education['education_to']
                }],
                "level": search_education_level(education["education_level"]),
                "primary": None
            }

        elif education["education_level"].lower() in higher_education_list:
            self.body_fields["education"] = {
                "additional": None,
                "attestation": None,
                "elementary": None,
                "level": search_education_level(education["education_level"]),
                "primary": [
                    {
                        "id": None,
                        "name": education['education_organisation'],
                        "name_id": None,
                        "organization": education['education_industry'],
                        "organization_id": None,
                        "result": education['education_faculty'],
                        "result_id": None,
                        "year": education['education_to']
                    }]
            }

    def add_experience(self, experience: dict[str, str]) -> None:
        """
        Добавляет поля:
            - Информацию о работе прошлой/настоящей
        """
        self.body_fields["experience"].append(
            {
                "area": {
                    "id": "113"
                },
                "company": experience['organisation'],
                "company_id": None,
                "company_url": None,
                "position": experience['position'],
                "description": experience['job_experience'],
                "employer": None,
                "start": experience['job_from'],
                "end": experience['job_to'],
            })

    def add_contact(self, contact: dict[str, str]) -> None:
        """
        Добавляет поля:
            - Контакты телефон/эл.почта
        """
        if "student_mail" in contact:
            self.body_fields["contact"].append(
                {
                    "preferred": False,
                    "type": {
                        "id": "email",
                        "name": "Эл. почта"
                    },
                    "value": contact["student_mail"]
                })
        elif "student_phone" in contact:
            self.body_fields["contact"].append(
                {
                    "comment": None,
                    "need_verification": False,
                    "preferred": True,
                    "type": {
                        "id": "cell",
                        "name": "Мобильный телефон"
                    },
                    "value": {
                        "formatted": contact["student_phone"],
                    },
                    "verified": False
                })

    def add_skill(self, skills_list: list[str]) -> None:
        """
        Добавляет поля:
            - Список навыков
        """
        for skill in skills_list:
            self.body_fields["skill_set"].append(skill)

    def set_about_info(self, about: str) -> None:
        """
        Добавляет поля:
            - О себе. Достижения, успехи
        """
        self.body_fields["skills"] = about

    def add_photo(self, photo:dict[str, str]) -> None:
        """
        Добавляет поля:
            - Фотография профиля
        """
        for k, v in photo.items():
            self.body_fields["photo"][k] = v

    def set_location(self,
                     area: str,
                     citizenship: list[dict[str, str]] | None=None,
                     work_ticket: list[dict[str, str]] | None=None,
                     relocation: dict[str, dict[str, str]] | None=None,
                     business_trip_readiness: dict[str, str] | None=None) -> None:
        """
        Добавляет поля:
            - Город проживания
            - Гражданство
            - Разрешение на работу
            - Возможность релокации
            - Готовность к командировкам
        """
        if citizenship is None:
            citizenship = [{"id": "113"}]
        if work_ticket is None:
            work_ticket = [{"id": "113"}]
        if relocation is None:
            relocation = {"type": {"id": "no_relocation"}}
        if business_trip_readiness is None:
            business_trip_readiness = {"id": "never"}

        student_area = search_areas(area)
        if student_area:
            self.body_fields["area"] = {"id": student_area}
        else:
            self.body_fields["area"] = {"id": 1}

        self.body_fields["citizenship"] = citizenship
        self.body_fields["work_ticket"] = work_ticket
        self.body_fields["relocation"] = relocation
        self.body_fields["business_trip_readiness"] = business_trip_readiness

    def set_personal_data(self, birth_date:str, first_name:str, last_name:str, gender:str='male') -> None:
        """
        Добавляет поля:
            - Дата рождения
            - Имя
            - Фамилия
            - Пол
        """
        self.body_fields["birth_date"] = birth_date
        self.body_fields["first_name"] = first_name
        self.body_fields["last_name"] = last_name
        self.body_fields["gender"] = {"id": gender}

    def add_languages(self, eng_level: str, rus_level: str | None=None) -> None:
        """
        Добавляет поля:
            - Владение языками
        """
        if rus_level is None:
            self.body_fields["language"].append(
            {
                "id": "rus",
                "name": "Русский",
                "level":
                    {
                        "id": "l1",
                        "name": "Родной"
                    }
            }
        )
        self.body_fields["language"].append(
            {
                "id": "eng",
                "name": "Английский",
                "level": search_language_level(eng_level)
            }
        )
