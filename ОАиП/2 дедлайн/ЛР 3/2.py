text = input("Введите произвольный текст: ")
lower = text.lower()
count = {}
for char in lower:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print(count)
