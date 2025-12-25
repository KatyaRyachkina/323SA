import time

lst1 = list(range(100000))

start_time = time.time()
for _ in range(1000):
    lst1.pop(0)
end_time = time.time()
time_pop0 = end_time - start_time

lst2 = list(range(100000))

start_time = time.time()
for _ in range(1000):
    lst2.pop()
end_time = time.time()
time_pop_end = end_time - start_time

print(f"Время pop(0): {time_pop0:.4f} секунд")
print(f"Время pop(): {time_pop_end:.4f} секунд")
print(f"Разница: в {time_pop0/time_pop_end:.1f} раза")

# Вывод:
# Операция pop() значительно быстрее pop(0).
# Сложность pop() - O(1) (удаление с конца).
# Сложность pop(0) - O(n) (удаление из начала требует сдвига всех элементов). 
