text = input("Введите строку: ")
glas = "аеёиоуыэюяaeiouyАЕЁИОУЫЭЮЯAEIOUY"
result = ""
n = 0
while n < len(text):
if text[n] not in glas:
result += text[n]
n += 1 
print("Строка без гласных:", result)
