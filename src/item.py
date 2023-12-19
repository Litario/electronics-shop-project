import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item ({self.name}, {self.price}, {self.quantity})"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name2: str):
        self.__name = name2[0:10]

    def calculate_total_price(self) -> float | int:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, adrs):
        """
        Метод, инициализирующий экземпляры класса данными из файла типа .csv
        """
        cls.all.clear()
        with open(adrs, encoding='windows-1251') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for dct in csv_reader:
                Item(*dct.values())

    @staticmethod
    def string_to_number(string):
        try:
            return int(float(string))
        except ValueError:
            print("Введены некорректные данные")
