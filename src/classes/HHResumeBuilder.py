from utils.search_areas_service import search_areas
from utils.search_education_level_service import search_education_level


class HHResumeBuilder:
    def __init__(self):
        self.body_fields = {
            "birth_date": None,
            "first_name": None,
            "last_name": None,
            # "gender": {},
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
            "contact": []
        }

    def build(self):
        inst = self.body_fields
        return inst

    def set_profession(self, title, professional_roles, schedules=None, travel_time=None):
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
            self.body_fields["professional_roles"].append(p_role)

    def add_education(self, education):
        secondary_education_list = ["secondary", "special_secondary"]
        higher_education_list = ["unfinished_higher", "higher", "bachelor", "master", "candidate", "doctor"]
        if education["level"].lower() in secondary_education_list:
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
        elif education["level"].lower() in higher_education_list:
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
                        "organization": education.get('education_faculty'),
                        "organization_id": None,
                        "result": education['education_industry'],
                        "result_id": None,
                        "year": education['education_to']
                    }]
            }

    def add_experience(self, recent_job, previous_job):
        self.body_fields["experience"].append(
            {
                "area": {
                    "id": "113"
                },
                "company": previous_job['recent_job_organisation'],
                "company_id": None,
                "company_url": None,
                "position": previous_job['recent_job_position'],
                "description": previous_job['recent_job_experience'],
                "employer": None,
                "start": previous_job['recent_job_from'],
                "end": previous_job['recent_job_to'],
            })
        self.body_fields["experience"].append(
            {
                "area": {
                    "id": "113"
                },
                "company": recent_job['recent_job_organisation'],
                "company_id": None,
                "company_url": None,
                "position": recent_job['recent_job_position'],
                "description": recent_job['recent_job_experience'],
                "employer": None,
                "start": recent_job['recent_job_from'],
                "end": recent_job['recent_job_to'],
            })

    def add_contact(self, phone_number, email):
        self.body_fields["contact"].append(
            {
                "preferred": False,
                "type": {
                    "id": "email",
                    "name": "Эл. почта"
                },
                "value": email
            })

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
                    "city": None,
                    "country": None,
                    "formatted": phone_number,
                    "number": None
                },
                "verified": False
            })

    def add_skill(self, skills_list):
        for skill in skills_list:
            self.body_fields["skill_set"].append(skill)

    def set_about_info(self, about):
        self.body_fields["skills"] = about

    def add_photo(self, photo):
        for k, v in photo:
            self.body_fields["photo"][k] = v

    def set_location(self, area, citizenship=None, work_ticket=None, relocation=None, business_trip_readiness=None):
        if citizenship is None:
            citizenship = [{"id": "113"}]
        if work_ticket is None:
            work_ticket = [{"id": "113"}]
        if relocation is None:
            relocation = {"type": {"id": "no_relocation"}}
        if business_trip_readiness is None:
            business_trip_readiness = [{"id": "never"}]

        self.body_fields["area"] = {"id": search_areas(area)}
        self.body_fields["citizenship"] = citizenship
        self.body_fields["work_ticket"] = work_ticket
        self.body_fields["relocation"] = relocation
        self.body_fields["business_trip_readiness"] = business_trip_readiness

    def set_personal_data(self, birth_date, first_name, last_name):
        self.body_fields["birth_date"] = birth_date
        self.body_fields["first_name"] = first_name
        self.body_fields["last_name"] = last_name
