class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Товар {self.name}, цена {self.price} руб'


item = ItemDiscountReport('Диван', 11000)
print(item.get_parent_data())