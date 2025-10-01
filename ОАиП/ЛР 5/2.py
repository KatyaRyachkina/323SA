print("Введите три целых числа через пробел:")
a, b, c = map(int, input().split())
print(f"\n Введенные числа: {a}, {b}, {c}")
mult_ab = a * b
mult_bc = b * c
mult_ca = c * a
print("\n Результаты умножения:")
print(f"{a} * {b} = {mult_ab}")
print(f"{b} * {c} = {mult_bc}")
print(f"{c} * {a} = {mult_ca}")
power_a4 = a ** 4
print("\n Дополнительные операции:")
print(f"{a} в 4 степени = {power_a4}")
print(f"Остаток от деления {b} на {c} = (remainder {b},{c}")
print(f"Целочисленное деление {c} на {a} = (int_division_{c},{a}")
print("\n Сумма результатов из пункта 4:")
if a != 0:
    int_division_ca = c // a
else:
    int_division_ca = "не определено (деление на ноль)"
