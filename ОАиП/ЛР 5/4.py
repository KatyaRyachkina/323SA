numbers = []
for i in range(5):num = float(input(f"Введите число {i+1}: "))
numbers.append(num)
min_num = min(numbers)
max_num = max(numbers)
print(f"Минимальное число: {min_num}")
print(f"Максимальное число: {max_num}")
