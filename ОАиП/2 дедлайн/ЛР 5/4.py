text = input("Введите текст: ")
words = text.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').split()
unique_words = set(words)
print(f"Уникальные слова: {len(unique_words)}")
long_words = {word for word in unique_words if len(word) > 5}
print(f"Длинные слова: {long_words}")
has_python = "python" in unique_words
has_programming = "programming" in unique_words
has_keywords = has_python or has_programming
print(f"Найдены ключевые слова: {has_keywords}")
if has_python:
    print("- Слово 'python' найдено")
if has_programming:
    print("- Слово 'programming' найдено")
