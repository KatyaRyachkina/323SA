fio_input = input("Введите ФИО через пробел: ")
fio_parts = fio_input.split()

if len(fio_parts) == 3:
    surname = fio_parts[0]
    name = fio_parts[1]
    patronymic = fio_parts[2]
    print(surname.upper())
    print(name.upper())
    print(patronymic.upper())
