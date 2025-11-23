stroka = input("Введите строку: ").lower().replace(" ","")
left = 0
right = len(stroka) - 1
palindrom = True

while left < right:
    if stroka[left] != stroka[right]:
        palindrom = False
        break
    left += 1
    right -= 1 

if palindrom:
    print("Это палиндром")
else:
    print("Это не палиндром")
