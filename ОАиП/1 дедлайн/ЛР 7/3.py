text = input("Введите текст: ")
word = input("Введите слово, которое хотите найти: ")
if word in text:
count = text.count(word)
print("Слово", word, "найдено в тексте")
print("Сколько раз встречается в тексте: ", count)
else:
print("Слова", word, "нет в тексте")
