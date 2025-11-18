call_counter = 0

def increment_counter() -> None:
    """
    Увеличивает глобальную переменную call_counter на 1 при каждом вызове.
    """
    global call_counter
    call_counter += 1

increment_counter()
increment_counter()
increment_counter()
print(call_counter)
