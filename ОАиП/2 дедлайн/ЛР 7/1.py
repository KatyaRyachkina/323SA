def sum_numbers(*args: float | int) -> float | int:
    """Принимает произвольное количество числовых аргументов и возвращает их сумму.
  Args:
    *args: Произвольное количество числовых аргументов.
Returns:
float | int: Сумма всех переданных аргументов."""
    return sum(args)
print(sum_numbers(1, 2, 3, 4, 5))
