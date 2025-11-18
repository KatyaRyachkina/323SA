import random
def generate_random_letter():
    return random.choice('abcdefghijklmnopqrstuvwxyz')
message = input("Введите сообщение: ")
n = int(input("Введите количество подстановочных символов: "))
encoded_message = ""
for char in message:
  encoded_message += char
  for _ in range(n):
  encoded_message += generate_random_letter()
print("Закодированное сообщение:", encoded_message)
