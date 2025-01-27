class AIRequestBuilder:
    """
    Класс строитель тела запроса POST для AIClient
    """

    def __init__(self):
        self.body_fields = {
            'student_id': None,
            'student_gender': None,
            'skill_set': [],
            'previous_job_position': None,
            'previous_job_industry': None,
            'education_organisation': None,
            'education_industry': None,
            'prompt': None
        }

    def build(self) -> dict[str, str | list]:
        instance = self.body_fields
        return instance

    def set_personal_data(self, student_id, student_gender) -> None:
        self.body_fields['student_id'] = student_id
        self.body_fields['student_gender'] = student_gender

    def set_skills(self, skills_list) -> None:
        for skill in skills_list:
            self.body_fields["skill_set"].append(skill)

    def set_education(self, education_organisation, education_industry) -> None:
        self.body_fields['education_organisation'] = education_organisation
        self.body_fields['education_industry'] = education_industry

    def set_previous_job(self, previous_job_position, previous_job_industry) -> None:
        self.body_fields['previous_job_position'] = previous_job_position
        self.body_fields['previous_job_industry'] = previous_job_industry

    def set_prompt(self, prompt) -> None:
        self.body_fields['prompt'] = prompt

