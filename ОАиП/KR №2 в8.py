def process_orders(stock_list, orders_list):
    revenue = 0
    cancelled_orders = []
    stock = [item.copy() for item in stock_list]
    
    stock_dict = {item["id"]: item for item in stock}
    
    for order in orders_list:
        item = stock_dict.get(order["id"])
        if item and item["qty"] >= order["count"]:
            item["qty"] -= order["count"]
            revenue += item["price"] * order["count"]
        else:
            cancelled_orders.append(order)
    
    return (revenue, stock, cancelled_orders)

stock = [
    {"id": 1, "name": "MacBook Pro", "price": 150000, "qty": 5},
    {"id": 2, "name": "iPhone 15", "price": 90000, "qty": 12},
    {"id": 3, "name": "AirPods", "price": 20000, "qty": 25},
    {"id": 4, "name": "iPad Air", "price": 60000, "qty": 8},
    {"id": 5, "name": "Apple Watch", "price": 35000, "qty": 15}
]

orders = [
    {"id": 1, "count": 2},
    {"id": 2, "count": 3},
    {"id": 3, "count": 30},
    {"id": 4, "count": 5},
    {"id": 6, "count": 1}
]

result = process_orders(stock, orders)
print(f"Выручка: {result[0]} руб.")
print("Обновленный склад:")
for item in result[1]:
    print(f"  {item['name']}: {item['qty']} шт.")
print("Отмененные заказы:")
for order in result[2]:
    item_id = order['id']
    item_name = next((item['name'] for item in stock if item['id'] == item_id), 'Неизвестный товар')
    print(f"  {item_name}: {order['count']} шт.")
