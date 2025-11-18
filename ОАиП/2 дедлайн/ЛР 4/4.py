temperatury = [15, 18, 12, 20, 16, 14, 19, 17, 13, 21, 15, 16, 18, 20]
vysokaia = temperatury[0]
for temp in temperatury:
    if temp > vysokaia:
        vysokaia = temp
nizkaia = temperatury[0]
for temp in temperatury:
    if temp < nizkaia:
        nizkaia = temp
summa = 0
for temp in temperatury:
    summa += temp
sred = summa / len(temperatury)
dney_vishe_srednei = 0
for temp in temperatury:
    if temp > sred:
        dney_vishe_srednei += 1
sort = temperatury.copy()  
sort.sort()              
farengeity = []
for temp in temperatury:
    f = temp * 9/5 + 32
    farengeity.append(round(f, 1))
print("Температуры:", temperatury)
print("Самая высокая:", vysokaia, "°C")
print("Самая низкая:", nizkaia, "°C")
print("Средняя температура:", round(sred, 1), "°C")
print("Дней выше средней:", dney_vishe_srednei)
print("Отсортированные:", sort)
print("В Фаренгейтах:", farengeity)
