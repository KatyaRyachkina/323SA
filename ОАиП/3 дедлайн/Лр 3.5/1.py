# 1. Функция поиска
def task_1(arr):
    for i in arr:
        if i == 100:
            return True
    return False
# Сложность: O(...) - пояснение

# 2. Функция доступа
def task_2(arr):
    return arr[0] + arr[-1]
# Сложность: O(...) - пояснение

# 3. Функция пар
def task_3(arr):
    count = 0
    for i in arr:
        for j in arr:
            if i == j:
                count += 1
    return count
# Сложность: O(...) - пояснение
