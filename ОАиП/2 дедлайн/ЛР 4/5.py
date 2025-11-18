text = input("Введите текст: ")
words = []
current_word = ""
for char in text:
    if char.isalpha():
        current_word += char.lower()
    else:
        if current_word:
            words.append(current_word)
            current_word = ""
if current_word:
    words.append(current_word)
if not words:
    print("Нет слов для анализа")
else:
    longest = max(words, key=len)
    shortest = min(words, key=len)
    avg_length = sum(len(word) for word in words) / len(words)
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]
    print(f"Самое длинное слово: {longest}")
    print(f"Самое короткое слово: {shortest}")
    print(f"Средняя длина: {avg_length:.1f}")
    print(f"Топ-5 слов: {top_words}")
