import pandas as pd
from src.views import main_page_view
from src.utils import get_card_stats, get_top_transactions, get_currency_rates, get_stock_prices
from unittest.mock import patch
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

def test_get_card_stats():
    """
    Тестирует корректность получения статистики по картам.
    """
    stats = get_card_stats()
    assert stats["total_spent"] == 15000.0
    assert stats["cashback_accumulated"] == 300.0


def test_get_top_transactions():
    """
    Тестирует получение топ-5 транзакций.
    """
    with patch('pandas.read_excel') as mock_read_excel:
        mock_data = {
            'Дата операции': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
            'Сумма операции': [100, 200, 300, 400, 500],
            'Категория': ['Еда', 'Развлечения', 'Транспорт', 'Одежда', 'Техника']
        }
        df_mock = pd.DataFrame(mock_data)
        mock_read_excel.return_value = df_mock

        top_transactions = get_top_transactions()
        assert len(top_transactions) == 5
        assert top_transactions[0]["Сумма операции"] == 500


def test_get_currency_rates():
    """
    Тестирует получение курсов валют.
    """
    rates = get_currency_rates()
    assert rates["USD"] == 74.50
    assert rates["EUR"] == 86.30


def test_get_stock_prices():
    """
    Тестирует получение цен на акции.
    """
    stocks = get_stock_prices()
    assert stocks["AAPL"] == 150.75
    assert stocks["GOOGL"] == 2820.50


def test_main_page_view():
    """
    Тестирует генерацию данных для главной страницы.
    """
    with patch('src.utils.get_card_stats', return_value={"total_spent": 1000.0, "cashback_accumulated": 50.0}), \
         patch('src.utils.get_top_transactions', return_value=[
             {"Дата операции": "2024-01-01", "Сумма операции": 100, "Категория": "Еда"},
             {"Дата операции": "2024-01-02", "Сумма операции": 200, "Категория": "Транспорт"}
         ]), \
         patch('src.utils.get_currency_rates', return_value={"USD": 74.50, "EUR": 86.30}), \
         patch('src.utils.get_stock_prices', return_value={"AAPL": 150.75, "GOOGL": 2820.50}):

        response = main_page_view("2024-01-01 12:00:00")
        data = json.loads(response)

        # Проверяем структуру данных
        assert data["current_time"] == "2024-01-01 12:00:00"
        assert data["card_stats"]["total_spent"] == 15000.0
        assert data["top_transactions"][0]["Сумма операции"] == 190044.51
        assert data["top_transactions"][1]["Сумма операции"] == 177506.03
