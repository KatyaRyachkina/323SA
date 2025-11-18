fruits ={'яблоки': 5,
    'бананы': 3,
    'апельсины': 3,
    'арбузы': 33}
print("Начальное количество фруктов:")
for fruit, count in fruits.items():
    print(f"За прилавком есть {count} {fruit}")

fruits["яблоки"] -= 2
print("После продажи 2 яблок:")

print("\nИтог:")
for fruit, count in fruits.items():
    print(f"За прилавком осталось {count} {fruit}")

fruits["арбузы"] = 0
print("После визита Ашота арбузов:")

print("\nИтог:")
for fruit, count in fruits.items():
    print(f"За прилавком осталось {count} {fruit}")
