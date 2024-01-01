from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    @property
    def n_sim(self):
        return self.number_of_sim

    @n_sim.setter
    def n_sim(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.number_of_sim = value
