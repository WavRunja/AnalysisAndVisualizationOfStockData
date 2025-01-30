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


# Notify if there are strong fluctuations
def notify_if_strong_fluctuations(data, threshold):
    """
    Анализирует данные и уведомляет, если цена акций колебалась более чем на заданный процент.

    :param data: DataFrame с колонкой 'Close'.
    :param threshold: Порог колебаний в процентах.
    """
    if data.empty:
        print("Данные отсутствуют, невозможно выполнить анализ колебаний.")
        return

    if 'Close' in data.columns:
        max_price = data['Close'].max()
        min_price = data['Close'].min()
        fluctuation = ((max_price - min_price) / min_price) * 100

        print(f"Максимальная цена: {max_price:.2f}")
        print(f"Минимальная цена: {min_price:.2f}")
        print(f"Колебания составляют {fluctuation:.2f}% за период.")

        if fluctuation > threshold:
            print(f"Внимание: колебания превысили порог в {threshold}% "
                  f"Порог превышен на {fluctuation - threshold:.2f}%!")
        else:
            print(f"Колебания не превышают порог в {threshold}%.")
    else:
        print("Колонка 'Close' отсутствует в данных.")
