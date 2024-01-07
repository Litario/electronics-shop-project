from src.item import Item


class Phone(Item):
    """
    Класс для представления телефона.
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса Phone.
        :param number_of_sim: кол-во симок в телефоне
        """
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    # @property
    # def n_sim(self):
    #     return self.number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self._number_of_sim = value
