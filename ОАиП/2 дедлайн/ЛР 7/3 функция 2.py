def fmt_fio(parts: list[str], capitalize: bool = True) -> str:
    """Форматирует ФИО из списка частей.
    Args:
        parts: Список строк, представляющих фамилию, имя и отчество.
        capitalize: Флаг капитализации.
    Returns:
        str: Отформатированная строка ФИО."""
    fio = " ".join(parts)
    if capitalize:
        return fio.title()
        
    return fio
print(fmt_fio(["петров", "иван", "сергеевич"]))
print(fmt_fio(["сидорова", "анна", "валерьевна"], capitalize=False))
