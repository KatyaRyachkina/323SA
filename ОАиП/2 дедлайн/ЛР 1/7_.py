symbol = input("Символ: ")
height = int(input("Высота: "))
width = int(input("Ширина: "))
for i in range(height):
    for j in range(width):
   if i == 0 or i == height - 1 or j == 0 or j == width - 1:
   print(symbol, end="")
     else:
    print(" ", end="")
    print()
