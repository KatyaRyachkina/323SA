def find_common_elements(list1: list, list2: list) -> list:
    """Находит общие элементы между двумя списками без дубликатов.
Args:
    list1: Первый список для сравнения.
    list2: Второй список для сравнения.
    Returns:
    list: Список общих элементов без дубликатов."""
    return list(set(list1) & set(list2))
list1 = [1, 2, 3, 4, 5, 5]
list2 = [4, 5, 6, 7, 8, 5]
common = find_common_elements(list1, list2)
print(common)
