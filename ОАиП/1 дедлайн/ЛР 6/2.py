text = input("Введите текст: ")
oldstr, newstr = input("Какое слово заменить, и на какое: ").split()
print(text.replace(oldstr, newstr))
