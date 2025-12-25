import sys

def create_list(n):
    return [i**2 for i in range(n)]

def create_gen(n):
    return (i**2 for i in range(n))

n = 1000000
lst = create_list(n)
gen = create_gen(n)

print(f"Размер списка: {sys.getsizeof(lst)} байт")
print(f"Размер генератора: {sys.getsizeof(gen)} байт")

# Список имеет пространственную сложность O(n) - хранит все элементы в памяти.
# Генератор имеет пространственную сложность O(1) - генерирует элементы по одному.
