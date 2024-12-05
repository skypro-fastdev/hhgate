from utils.search_areas_service import search_areas
from utils.search_education_level_service import search_education_level
from utils.search_language_level_service import search_language_level


class TestSearchersServices:
    """
    Тест класс для поисковых функций
    """

    def test_search_areas_spb(self):
        assert search_areas('Санкт-Петербург') == '2', 'Ошибка для Санкт-Петербург, внешний слой'

    def test_search_areas_ekb(self):
        assert search_areas('Екатеринбург') == '3', 'Ошибка для Екатеринбург, внутренний слой'

    def test_search_education_level_secondary(self):
        assert search_education_level('secondary') == {'id': 'secondary', 'name': 'Среднее'}, 'Ошибка для среднего образования'

    def test_search_education_level_special_secondary(self):
        assert search_education_level('special_secondary') == {'id': 'special_secondary', 'name': 'Среднее специальное'}, \
            'Ошибка для среднего специального образования'

    def test_search_education_level_unfinished_higher(self):
        assert search_education_level('unfinished_higher') == {'id': 'unfinished_higher', 'name': 'Неоконченное высшее'}, \
            'Ошибка для неоконченного высшего образования'

    def test_search_education_level_higher(self):
        assert search_education_level('higher') == {'id': 'higher', 'name': 'Высшее'}, 'Ошибка для высшего образования'

    def test_search_education_level_bachelor(self):
        assert search_education_level('bachelor') == {'id': 'bachelor', 'name': 'Бакалавр'}, 'Ошибка для бакалавра'

    def test_search_education_level_master(self):
        assert search_education_level('master') == {'id': 'master', 'name': 'Магистр'}, 'Ошибка для магистра'

    def test_search_education_level_candidate(self):
        assert search_education_level('candidate') == {'id': 'candidate', 'name': 'Кандидат наук'}, 'Ошибка для кандидата наук'

    def test_search_language_level_a1(self):
        assert search_language_level('A1') == {'id': 'a1', 'name': 'A1 — Начальный'}, 'Ошибка для уровня а1'

    def test_search_language_level_a2(self):
        assert search_language_level('A2') == {'id': 'a2', 'name': 'A2 — Элементарный'}, 'Ошибка для уровня а2'

    def test_search_language_level_b1(self):
        assert search_language_level('B1') == {'id': 'b1', 'name': 'B1 — Средний'}, 'Ошибка для уровня b1'

    def test_search_language_level_b2(self):
        assert search_language_level('B2') == {'id': 'b2', 'name': 'B2 — Средне-продвинутый'}, 'Ошибка для уровня b1'

    def test_search_language_level_c1(self):
        assert search_language_level('C1') == {'id': 'c1', 'name': 'C1 — Продвинутый'}, 'Ошибка для уровня c1'

    def test_search_language_level_c2(self):
        assert search_language_level('C2') == {'id': 'c2', 'name': 'C2 — В совершенстве'}, 'Ошибка для уровня c2'

    def test_search_language_level_l2(self):
        assert search_language_level('L1') == {'id': 'l1', 'name': 'Родной'}, 'Ошибка для уровня l1'
