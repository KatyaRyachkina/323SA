n = int(input("Ввод: "))
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    matrix.append(row)

x = n // 2
y = n // 2
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
dir = 0
number = 1
step = 1
changes = 0

while number <= n * n:
    for i in range(step):
        if 0 <= x < n and 0 <= y < n:
            matrix[x][y] = number
            number += 1
        dx, dy = directions[dir]
        x += dx
        y += dy
        if number > n * n:
            break
    dir = (dir + 1) % 4
    changes += 1
    if changes % 2 == 0:
        step += 1

print("Вывод:")
for row in matrix:
    for num in row:
        print(f"{num:3}", end=" ")
    print()
