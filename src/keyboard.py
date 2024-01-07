from src.item import Item


class languageMixin:
    """
    Класс миксин для изменения языка.
    """
    languages = {'EN': 'RU', 'RU': 'EN'}

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        self.__language = self.__class__.languages[self.__language]


class Keyboard(Item, languageMixin):
    """
    Класс для представления клавиатуры.
    """

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        languageMixin.__init__(self)
