products = {
    "Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}
max = 0
best = ""
for product, info in products.items():
    if info["sold"] > max:
        max = info["sold"]
        best = product
print("Самый продаваемый товар:", best)

total = 0
for info in products.values():
    revenue = info["price"] * info["sold"]
    total += revenue
print("Общая выручка магазина:", total, "руб.")

max_rev = 0
best_rev = ""
for product, info in products.items():
    product_rev = info["price"] * info["sold"]
    if product_rev > max_rev:
        max_rev = product_rev
        best_rev = product
print("Товар с наибольшей выручкой:", best_rev, max_rev, "руб.")
