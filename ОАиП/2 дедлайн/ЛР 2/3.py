text = input("Введите текст: ")
letters = 0
digits = 0
punct = 0
spaces = 0

for symbol in text:
    if symbol.isalpha():
        letters += 1
    elif symbol.isdigit():
        digits += 1
    elif symbol in '.,!?:;':
        punct += 1
    elif symbol == ' ':
        spaces += 1
        
print("Букв =", letters)
print("Цифр =", digits)
print("Знаков препинания =", punct)
print("Пробелов =", spaces)
