from random import randint

class FruitStallCRM:
    def __init__(self, name):
        self.name = name
        self.counter = {}
        self.store = {}
        self.price = {}
        self.money = 1000
        self.day = 0
        self.daily_money = 0
        
    def add_fruit(self, fruit, counter_max, store_max, sale_price, purchase_price):
        self.counter[fruit] = {'max': counter_max, 'current': 0}
        self.store[fruit] = {'max': store_max, 'current': 0}
        self.price[fruit] = {'sale_price': sale_price, 'purchase price': purchase_price}
        
    def move_to_counter(self, fruit, amount):
        if fruit not in self.store:
            return False
        if amount > self.store[fruit]['current']:
            amount = self.store[fruit]['current']
        if self.counter[fruit]['current'] + amount > self.counter[fruit]['max']:
            amount = self.counter[fruit]['max'] - self.counter[fruit]['current']
        self.store[fruit]['current'] -= amount
        self.counter[fruit]['current'] += amount
        return True
        
    def sell_fruit(self):
        for fruit in self.counter:
            if self.counter[fruit]['current'] > 0 and randint(1, 100) <= 30:
                sold = randint(1, self.counter[fruit]['current'])
                self.counter[fruit]['current'] -= sold
                self.daily_money += sold * self.price[fruit]['sale_price']
                
    def update_prices(self):
        for fruit in self.price:
            change = randint(-5, 5)
            self.price[fruit]['sale_price'] = max(1, self.price[fruit]['sale_price'] + change)
            self.price[fruit]['purchase price'] = max(1, self.price[fruit]['purchase price'] + change)
            
    def ashot_steal(self):
        if randint(1, 100) <= 20:
            for fruit in self.counter:
                if self.counter[fruit]['current'] > 0:
                    steal_percent = randint(50, 100) / 100
                    stolen = int(self.counter[fruit]['current'] * steal_percent)
                    self.counter[fruit]['current'] -= stolen
                    
    def next_day(self):
        self.day += 1
        self.daily_money = 0
        
        self.update_prices()
        self.sell_fruit()
        self.ashot_steal()
        self.money += self.daily_money
        if self.money <= 0:
            print("Банкрот!")
            return False
        if self.day >= 10:
            print("Победа!")
            return False
        return True
    
    def buy_fruit(self, fruit, amount):
        if fruit not in self.price:
            return False
        
        cost = amount * self.price[fruit]['purchase price']
        if cost > self.money:
            return False
        
        if self.store[fruit]['current'] + amount > self.store[fruit]['max']:
            return False
        
        self.money -= cost
        self.store[fruit]['current'] += amount
        return True
    
    def status(self):
        print(f"День: {self.day}, Деньги: {self.money}")
        print("Прилавок:", self.counter)
        print("Склад:", self.store)
        print("Цены:", self.price)

stall = FruitStallCRM("Фруктовый рай")
stall.add_fruit("яблоко", 10, 50, 10, 5)
stall.add_fruit("банан", 8, 40, 15, 8)

stall.buy_fruit("яблоко", 20)
stall.buy_fruit("банан", 15)

stall.move_to_counter("яблоко", 5)
stall.move_to_counter("банан", 4)

for _ in range(10):
    if not stall.next_day():
        break
    stall.status()
