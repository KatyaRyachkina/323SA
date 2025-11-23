def fmt_fio(parts: list[str], capitalize: bool = True) -> str:
    fio = " ".join(parts)
    if capitalize:
        return fio.title()
    return fio

print(fmt_fio(["петров", "иван", "сергеевич"]))
print(fmt_fio(["сидорова", "анна", "валерьевна"], capitalize=False))
