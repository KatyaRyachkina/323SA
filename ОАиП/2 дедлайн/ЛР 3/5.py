slovar = {}
print("Вводите текст. Для окончания ввода нажмите Enter на пустой строке:")
while True:
    stroka = input()
    if stroka == "":
        break
    slova = stroka.split()
    for slovo in slova:
        chisto = ""
        for bukva in slovo:
            if bukva.isalpha(): 
                chisto += bukva.lower()  
        if chisto == "":
            continue
        if chisto in slovar:
            slovar[chisto] += 1
        else:
            slovar[chisto] = 1
print("Статистика слов:", slovar)
