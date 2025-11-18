year = int(input("Введите год: "))
if year % 400 == 0:
print(year, "високосный")
elif year % 100 == 0:
print(year, "не високосный")
elif year % 4 == 0:
print(year, "високосный")
else:
print(year, "не високосный")
