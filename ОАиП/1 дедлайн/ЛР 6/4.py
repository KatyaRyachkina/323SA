text = input("Введите текст: ")
start, end = map(int, input().split())
print(text[start-1:end])
