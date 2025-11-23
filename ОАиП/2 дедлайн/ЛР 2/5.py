n = int(input("Сколько чисел вы хотите ввести? "))
numbers = []

for i in range(1, n + 1):
    num = int(input(f"Введите число {i}: "))
    numbers.append(num)

max_num = max(numbers)
min_num = min(numbers)
average = sum(numbers) / len(numbers)
count = 0

for num in numbers:
    if num > average:
        count += 1

print("\nРезультаты:")
print(f"Максимальное: {max_num}")
print(f"Минимальное: {min_num}")
print(f"Среднее: {average}")
print(f"Чисел больше среднего: {count}")
