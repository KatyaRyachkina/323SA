input_values = input("Введите три целых числа через пробел: ").split()
a, b, c = map(int, input_values)
ab = a * b
bc = b * c
ca = c * a
print("\n Результаты умножения:")
print("a * b =", a, "*", b, "=", ab)
print("b * c =", b, "*", c, "=", bc)
print("c * a =", c, "*", a, "=", ca)
