import math

data = input("Введите число1, знак и число2: ").split()
num1 = float(data[0])
sign = data[1]
num2 = float(data[2])

if sign == '+':
    result = num1 + num2
elif sign == '-':
    result = num1 - num2
elif sign == '*':
    result = num1 * num2
elif sign == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Деление на 0 невозможно"
elif sign == '%':
    result = num1 % num2
elif sign == '//':
    if num2 != 0:
        result = num1 // num2
    else:
        result = "Деление на 0 невозможно"
elif sign == '**':
    result = num1 ** num2
elif sign == '%%':
    if num1 != 0:  
        result = (num2 / num1) * 100
    else:
        result = "Деление на 0 невозможно"
elif sign == '"':
    result = math.sqrt(num1)
else:
    result = "Неизвестная операция"

print("Результат:", result)
