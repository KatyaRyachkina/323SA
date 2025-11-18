numbers = [24, 18, 12, 90, 56, 78, 67, 71, 31, 50]
chetno = []  
for num in numbers:
    if num % 2 == 0:  
        chetno.append(num)  
large = [] 
for num in numbers:
    if num > 50: 
        large.append(num)  
print("Исходный список чисел:", numbers)
print("Четные числа:", chetno)
print("Числа больше 50:", large)
