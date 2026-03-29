import pandas as pd



def get_card_stats() -> dict:
    """
    Возвращает статистику по картам: общая сумма расходов, накопленный кешбэк.

    Returns:
        dict: Статистика по картам.
    """
    # Пример данных
    stats = {
        "total_spent": 15000.0,
        "cashback_accumulated": 300.0
    }
    return stats


def get_top_transactions() -> list:
    """
    Возвращает список топ-5 транзакций.

    Returns:
        list: Топ-5 транзакций.
    """
    data = pd.read_excel("data/operations.xlsx")
    top_transactions = data.nlargest(5, 'Сумма операции')[['Дата операции', 'Сумма операции', 'Категория']].to_dict(orient='records')
    return top_transactions


def get_currency_rates() -> dict:
    """
    Возвращает текущие курсы валют (пример статических данных).

    Returns:
        dict: Курсы валют.
    """
    return {"USD": 74.50, "EUR": 86.30}


def get_stock_prices() -> dict:
    """
    Возвращает текущие цены акций (пример статических данных).

    Returns:
        dict: Цены акций.
    """
    return {"AAPL": 150.75, "GOOGL": 2820.50}


def get_total_income_expenses():
    """
    Возвращает общую сумму доходов и расходов.
    """
    data = pd.read_excel("data/operations.xlsx")

    total_income = round(data[data['Сумма операции'] > 0]['Сумма операции'].sum(), 2)
    total_expenses = round(data[data['Сумма операции'] < 0]['Сумма операции'].sum(), 2)

    return total_income, abs(total_expenses)  # Возвращаем сумму расходов в положительном виде


def get_category_expenses():
    """
    Возвращает расходы по категориям.
    """
    data = pd.read_excel("data/operations.xlsx")
    expenses_by_category = data[data['Сумма операции'] < 0].groupby('Категория')['Сумма операции'].sum().reset_index()

    return expenses_by_category.to_dict(orient='records')