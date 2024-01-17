import csv
import os
import pathlib
from pathlib import Path

from src.errors import InstantiateCSVError


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

        self.__class__.all.append(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}{tuple(self.__dict__.values())}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise Exception("Складывать нужно ЭК класса.")

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
    def instantiate_from_csv(cls, csv_file_path='src/items.csv'):
        """
        Метод, инициализирующий экземпляры класса данными из файла типа .csv
        """
        BASE_DIR: Path = pathlib.Path(__file__).resolve().parent.parent
        CSV_FILE_DIR: Path = BASE_DIR.joinpath(csv_file_path)

        if not os.path.exists(CSV_FILE_DIR):
            raise FileNotFoundError("Отсутствует файл item.csv")
        else:
            cls.all.clear()
            with open(CSV_FILE_DIR, encoding='windows-1251') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                lst = list(csv_reader)  ## без листа указатель чтения в объекте DictReader останется в конце файла

                ## условие наличия правильного количества столбцов в файле
                attr_number = len(cls.__init__.__code__.co_varnames) - 1
                csv_file.seek(0)
                if len(csv_file.readline()) == attr_number:
                    ## условие наличия всех значений в файле
                    if all(map(lambda d: all(d.values()), lst)):
                    # if all([all(i.values()) for i in lst]):  ## вариант условия через списочное выражение
                        for dct in lst:
                            cls(*dct.values())
                    else:
                        raise InstantiateCSVError()
                else:
                    raise InstantiateCSVError()

    @staticmethod
    def string_to_number(string):
        try:
            return int(float(string))
        except ValueError:
            print("Введены некорректные данные")
