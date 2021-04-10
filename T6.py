class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport1(ItemDiscount):
    def get_info(self):
        return self.name


class ItemDiscountReport2(ItemDiscount):
    def get_info(self):
        return self.price


item1 = ItemDiscountReport1('Диван', 11000)
print(item1.get_info())

item2 = ItemDiscountReport2('Кровать', 12000)
print(item2.get_info())

for item in (item1, item2):
    print(item.get_info())

def obj_handler(obj):
    return obj.get_info()

print(obj_handler(item1))
print(obj_handler(item2))