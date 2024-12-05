from src.classes.HHResumeBuilder import HHResumeBuilder


class TestHHResumeBuilder:
    """
    Тест класс для Билдера HHResumeBuilder
    """

    resume_builder = HHResumeBuilder()

    def test_build(self):
        self.resume_builder.set_profession(
            title='Аналитик',
            professional_roles=['165']
        )
        self.resume_builder.add_education(education=
        {
            'education_level': 'higher',
            'education_organisation': 'Универ всякой всячины',
            'education_to': '2000',
            'education_faculty': 'Биотехнолог',
            'education_industry': 'Медтехнологии'
        })
        self.resume_builder.add_experience(experience=
        {
            'organisation': 'Мед технологии',
            'position': 'Руководитель отдела',
            'job_experience': 'Руководил отделом',
            'job_from': '2000-01-10',
            'job_to': '2000-10-10'
        })
        self.resume_builder.add_experience(experience=
        {
            'organisation': 'ИТ организация',
            'position': 'Аналитик данных',
            'job_experience': 'Анализировал данные',
            'job_from': '2001-01-01',
            'job_to': '2001-10-10'
        })
        self.resume_builder.add_contact(contact=
        {
            'student_mail': 'mymail@mail.com'
        })
        self.resume_builder.add_contact(contact={
            'student_phone': '7955-855-3522'
        })
        self.resume_builder.add_skill(skills_list=["Python"])
        self.resume_builder.set_about_info(about='Успехи и достижения')
        self.resume_builder.add_photo(photo=
        {
            "id": '1222333444',
            "small": 'url_small',
            "medium": 'url_medium',
        })
        self.resume_builder.set_location(
            area='Санкт-Петербург'
        )
        self.resume_builder.set_personal_data(
            birth_date='1990-05-05',
            first_name='Студент',
            last_name='Студентов',
            gender='male'
        )
        self.resume_builder.add_languages('A1')

        assert self.resume_builder.build() == {
            'birth_date': '1990-05-05',
            'first_name': 'Студент',
            'last_name': 'Студентов',
            'gender': {'id': 'male'},
            'area': {'id': '2'},
            'citizenship': [{'id': '113'}],
            'work_ticket': [{'id': '113'}],
            'relocation': {'type': {'id': 'no_relocation'}},
            'business_trip_readiness': {'id': 'never'},
            'title': 'Аналитик',
            'schedules': [{'id': 'fullDay', 'name': 'Полный день'}, {'id': 'remote', 'name': 'Удаленная работа'}],
            'travel_time': {"id": 'any'},
            'photo': {"id": '1222333444', "small": 'url_small', "medium": 'url_medium'},
            'professional_roles': [{'id': '165'}],
            'experience': [{
                'area': {
                    'id': "113"
                },
                'company': 'Мед технологии',
                'company_id': None,
                'company_url': None,
                'position': 'Руководитель отдела',
                'description': 'Руководил отделом',
                'employer': None,
                'start': '2000-01-10',
                'end': '2000-10-10',
                },
                {
                    'area': {
                        'id': '113'
                    },
                    'company': 'ИТ организация',
                    'company_id': None,
                    'company_url': None,
                    'position': 'Аналитик данных',
                    'description': 'Анализировал данные',
                    'employer': None,
                    'start': '2001-01-01',
                    'end': '2001-10-10',
                }],
            'education': {
                'additional': None,
                'attestation': None,
                'elementary': None,
                'level': {
                    'id': 'higher',
                    'name': 'Высшее'
                },
                'primary': [
                    {
                        'id': None,
                        'name': 'Универ всякой всячины',
                        'name_id': None,
                        'organization': 'Медтехнологии',
                        'organization_id': None,
                        'result': 'Биотехнолог',
                        'result_id': None,
                        'year': '2000'
                    }]
            },
            'skills': 'Успехи и достижения',
            'skill_set': ['Python'],
            'contact': [
                {
                    'preferred': False,
                    'type': {
                        'id': 'email',
                        'name': 'Эл. почта'
                    },
                    'value': 'mymail@mail.com'
                },
                {
                    'comment': None,
                    'need_verification': False,
                    'preferred': True,
                    'type': {
                        'id': 'cell',
                        'name': 'Мобильный телефон'
                    },
                    'value': {
                        'formatted': '7955-855-3522',
                    },
                    'verified': False
                }
            ],
            'language': [
                {
                    'id': 'rus',
                    'name': 'Русский',
                    'level':
                        {
                            'id': 'l1',
                            'name': 'Родной'
                        }
                },
                {
                    'id': 'eng',
                    'name': 'Английский',
                    'level': {
                        'id': 'a1',
                        'name': 'A1 — Начальный'
                    }
                }
            ]
        }