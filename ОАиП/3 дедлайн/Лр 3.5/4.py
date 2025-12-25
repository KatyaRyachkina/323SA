import time
import random

def find_pair_slow(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None

def find_pair_fast(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None

arr = [random.randint(0, 10000) for _ in range(10000)]
target = 15000  

start = time.time()
result_slow = find_pair_slow(arr, target)
time_slow = time.time() - start

start = time.time()
result_fast = find_pair_fast(arr, target)
time_fast = time.time() - start

print(f"Медленное решение: {time_slow:.4f} сек")
print(f"Быстрое решение: {time_fast:.4f} сек")
print(f"Ускорение: в {time_slow/time_fast:.1f} раза")
print(f"Найденная пара: {result_fast}")
