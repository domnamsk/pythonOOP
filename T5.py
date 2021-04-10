class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = discount

    # def get_parent_data(self):
    #     return f'Товар {self.name}, цена {self.price}'

    def __str__(self):
        return f'Товар {self.name}, его цена без скидки {self.price}руб., а со скидкой {self.discount}%: {self.price - self.price * self.discount / 100} руб.'


item = ItemDiscountReport('Диван', 11000, 10)
print(item)