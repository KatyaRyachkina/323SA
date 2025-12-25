import time
import random

def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates

arr1 = [random.randint(0, 1000) for _ in range(5000)]

start_time = time.time()
result1 = find_duplicates(arr1)
time1 = time.time() - start_time
print(f"Время для 5000 элементов: {time1:.4f} сек")

arr2 = [random.randint(0, 1000) for _ in range(10000)]

start_time = time.time()
result2 = find_duplicates(arr2)
time2 = time.time() - start_time
print(f"Время для 10000 элементов: {time2:.4f} сек")

growth_ratio = time2 / time1
print(f"Рост времени: в {growth_ratio:.1f} раза при увеличении данных в 2 раза")

# Ответ:
# При увеличении данных в 2 раза, время выполнения выросло примерно в 3-4 раза,
# что соответствует квадратичной сложности O(n²).
