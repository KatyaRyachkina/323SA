tasks = []
while True:
print("\nЧто вы хотите сделать?")
print("1 - Показать все задачи")
print("2 - Добавить задачу")
print("3 - Удалить задачу") 
print("4 - Выйти")
vybor = input("Введите цифру: ")
    if vybor == "1":
    if len(tasks) == 0:
        print("Задач нет!")
    else:
        print("\nВаши задачи:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
    elif vybor == "2":
    novaia_zadacha = input("Введите новую задачу: ")
    tasks.append(novaia_zadacha)
    print("Задача добавлена!")
    elif vybor == "3":
    if len(tasks) == 0:
    print("Нет задач для удаления!")
        else:
            print("\nВаши задачи:")
            for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")
            nomer = input("Какую задачу вы выполнили? Введите номер: ")
    if nomer.isdigit():
        nomer = int(nomer)
        if nomer >= 1 and nomer <= len(tasks):
        udalennaya = tasks[nomer-1]
        del tasks[nomer-1]
        print(f'Задача "{udalennaya}" удалена!')
    else:
        print("Такой задачи нет")
    else:
        print("Введите число!")
    
    elif vybor == "4":
    print("До свидания")
    break
    else:
    print("Введите 1,2,3 или 4")
