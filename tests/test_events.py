import unittest
from unittest.mock import patch
from src.views import events_page_view

class TestEventsPageView(unittest.TestCase):

    @patch('src.utils.get_total_income_expenses', return_value=(5000.0, 3000.0))
    @patch('src.utils.get_category_expenses', return_value=[
        {"Категория": "Еда", "Сумма операции": -1000},
        {"Категория": "Транспорт", "Сумма операции": -500}
    ])
    def test_events_page_view(self, mock_get_category_expenses, mock_get_total_income_expenses):
        """
        Тестирует генерацию данных для страницы «События».
        """

        expected_response = {
            "total_income": 8037215.06,
            "total_expenses": 9965776.83,
            "expenses_by_category": [{"Категория": "Duty Free", "Сумма операции": -60.0}]
        }

        response = events_page_view()
        self.assertEqual(response["total_income"], expected_response["total_income"])
        self.assertEqual(response["total_expenses"], expected_response["total_expenses"])
        self.assertEqual(response["expenses_by_category"], expected_response["expenses_by_category"])

if __name__ == '__main__':
    unittest.main()