class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Товар {self.__name}, цена {self.__price}' # Будет ошибка
        # return f'Товар {self._ItemDiscount__name}, цена {self._ItemDiscount__price}'


item = ItemDiscountReport('Диван', 11000)
print(item.get_parent_data())