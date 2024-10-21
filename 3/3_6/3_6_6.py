import sys

class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = list(map(str.strip, sys.stdin.readlines()))
shop_items = {}

for el in lst_in:
    name, values = el.split(": ")
    weight, price = values.split()
    weight = float(weight)
    price = float(price)
    obj = ShopItem(name, weight, price)
    value = shop_items.get(obj, [])
    if len(value) == 2:
        value[1] += 1
    else:
        shop_items[obj] = [obj, 1]

print(shop_items)