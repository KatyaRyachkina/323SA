def calc_avg(numbers: list[float | int]) -> float:
    """Вычисляет среднее арифметическое значение списка чисел.
    Args:
        numbers: Список чисел для вычисления среднего.
    Returns:
        float: Среднее арифметическое значение.
    """if not numbers:
        return 0.0  
    return sum(numbers) / len(numbers)

print(calc_avg([10, 20, 30, 40]))
