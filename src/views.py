from datetime import datetime
from src.utils import get_top_transactions, get_card_stats, get_currency_rates, get_stock_prices
import json
from src.utils import get_total_income_expenses, get_category_expenses


def main_page_view(current_time: str) -> str:
    """
    Генерирует данные для главной страницы с текущим временем, статистикой по картам,
    топ-5 транзакциями, курсами валют и акциями.

    Args:
        current_time (str): Дата и время в формате YYYY-MM-DD HH:MM:SS.

    Returns:
        str: JSON-ответ с данными.
    """
    try:
        current_dt = datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        raise ValueError("Invalid date format. Expected YYYY-MM-DD HH:MM:SS") from e

    card_stats = get_card_stats()
    top_transactions = get_top_transactions()
    currency_rates = get_currency_rates()
    stock_prices = get_stock_prices()

    response_data = {
        "current_time": current_dt.strftime("%Y-%m-%d %H:%M:%S"),
        "card_stats": card_stats,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices
    }

    return json.dumps(response_data, ensure_ascii=False, indent=4)


def events_page_view():
    """
    Генерирует данные для страницы «События», включая общую сумму расходов и поступлений,
    а также разбивку расходов по категориям.
    """
    total_income, total_expenses = get_total_income_expenses()
    expenses_by_category = get_category_expenses()

    response = {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "expenses_by_category": expenses_by_category
    }

    return response
