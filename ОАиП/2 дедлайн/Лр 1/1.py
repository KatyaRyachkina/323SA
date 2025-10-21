num = int(input("Введите целое положительное число: "))
s = 0
while num > 0:
    s += num % 10
    num //= 10 
print(s)
