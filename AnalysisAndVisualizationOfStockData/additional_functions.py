# Calculating the average price
def calculate_and_display_average_price(data):
    """
    Вычисляет и возвращает, выводит среднюю цену закрытия акций за период.

    :param data: DataFrame с колонкой 'Close'.
    :return: Средняя цена или None, если колонка отсутствует.
    """
    if 'Close' in data.columns:
        average_price = data['Close'].mean()
        print(f"Средняя цена закрытия за период: {average_price:.2f}")
        return average_price
    else:
        print("Колонка 'Close' отсутствует в данных.")
        return None
