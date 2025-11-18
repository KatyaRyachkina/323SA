book = {"Андрей": "+7-999-176-44-15",
        "Дарья": "+7-952-711-22-47",
        "Варвара": "+7-925-555-97-09"}
while True:
    print("ТЕЛЕФОННАЯ КНИГА")
    print("="*30)
    print("1 - Показать все контакты")
    print("2 - Добавить контакт")
    print("3 - Удалить контакт")
    print("4 - Выйти")
    print("="*30)
    choice = input("Выберите действие (1-4): ")
    if choice == "1":
        print("\n---ВСЕ КОНТАКТЫ---")
        if book:
            for name, phone in book.items():
                print(f"{name}: {phone}")
        else:
            print("Телефонная книга пуста")
    elif choice == "2":
        print("\n---ДОБАВЛЕНИЕ КОНТАКТА---")
        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ").strip()
        if name in book:
            print("Ошибка: Контакт с таким именем уже существует")
        else:
            book[name] = phone 
            print("Контакт успешно добавлен")
    elif choice == "3":
        print("\n---УДАЛЕНИЕ КОНТАКТА---")
        name = input("Введите имя контакта для удаления: ")
        if name in book:
            del book[name]
            print("Контакт успешно удален")
        else: 
            print("Ошибка: Контакт с таким именем не найден")
    elif choice == "4":
        print("До свидания!")
        exit()
    else:
        print("Ошибка: Введите число от 1 до 4")
