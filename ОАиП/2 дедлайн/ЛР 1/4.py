from random import randint
num = randint(1, 100)
while True:
num1= int(input("Введите число: "))
if num1 < num:
 print("Больше")
elif num1 > num:
print("Меньше")
else:
print("Угадал!")
break
