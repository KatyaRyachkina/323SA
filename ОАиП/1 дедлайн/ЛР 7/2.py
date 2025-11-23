password = input("Придумайте свой пароль: ")
confirm = input("Подтвердите пароль: ")
if password == confirm:
    print ("Пароль сохранен")
else:
     print ("Пароли не совпадают")
exit()
login = input("Введите пароль: ")
if login == password:
     print("Access")
else:
     print("Denied")
