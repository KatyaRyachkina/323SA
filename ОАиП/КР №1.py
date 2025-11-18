words = input("Введите три слова: ").split()
symbol = input("Введите разделитель: ")

new_words = []
for word in words:
    number = False
    for letter in word:
        if letter in "0123456789":
            number = True
            break
    if number:
        new_words.append("NUMBER")
    else:
        new_words.append(word)
match symbol:
    case "/" | "-" | "#":
        result = symbol.join(new_words)
    case _:
        result = ".".join(new_words)  
print("Результат:", result)
