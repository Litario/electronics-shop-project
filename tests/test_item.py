import pytest

from src.errors import InstantiateCSVError
from src.item import Item
from src.phone import Phone


## ________________________________________________________ fixtures
@pytest.fixture
def item_fixture():
    return [
        Item("test_2", 12.4, 2),
        Item("test_3", 50, 3)
    ]


# @pytest.fixture
# def item_fixture2():
#     return Item("test_3", 50, 3)


@pytest.fixture
def phone_fixture():
    return Phone("Astra", 5000, 1, 2)


# obj = Item("test_1", 12.4, 2)


## ____________________________________________________________ tests
def test__item_init(item_fixture):
    assert item_fixture[0].name == "test_2"
    assert item_fixture[0].price == 12.4
    assert item_fixture[0].quantity == 2


def test__item_all(item_fixture):
    start_len = len(Item.all)
    n = 10
    for i in range(n):
        Item(f"obj_{i}", i / 1, i)

    assert len(Item.all) == n + start_len


def test__item_str(item_fixture):
    assert str(item_fixture[0]) == 'test_2'


def test__item_repr(item_fixture):
    assert repr(item_fixture[0]) == "Item('test_2', 12.4, 2)"


def test__item_add(item_fixture, phone_fixture):
    with pytest.raises(Exception, match=r"Складывать нужно ЭК класса."):
        item_fixture[0] + 10
        item_fixture[0] + "проверка"

    assert item_fixture[0] + item_fixture[1] == 5
    assert item_fixture[0] + phone_fixture == 3
    assert item_fixture[1] + phone_fixture == 4
    assert phone_fixture + item_fixture[0] == 3


def test__name(item_fixture):
    item_fixture[0].name = "test2_from_setter"
    assert item_fixture[0].name == "test2_from"


def test__calculate_total_price(item_fixture):
    assert item_fixture[0].calculate_total_price() == 24.8


def test__apply_discount_1(item_fixture):
    item_fixture[0].pay_rate = 0.5
    item_fixture[0].apply_discount()
    assert item_fixture[0].price == 6.2


def test__apply_discount_2(item_fixture):
    item_fixture[0].pay_rate = 3
    item_fixture[0].apply_discount()
    assert item_fixture[0].price == 37.2


def test__instantiate_from_csv(item_fixture):
    with pytest.raises(FileNotFoundError, match=r"Отсутствует файл item.csv"):
        item_fixture[0].__class__.instantiate_from_csv('src/items_absent.csv')

    with pytest.raises(InstantiateCSVError, match=r"Файл item.csv поврежден"):
        item_fixture[0].__class__.instantiate_from_csv('src/items_for_test1.csv')

    with pytest.raises(InstantiateCSVError, match=r"Файл item.csv поврежден"):
        item_fixture[0].__class__.instantiate_from_csv('src/items_for_test2.csv')


def test__string_to_number():
    assert Item.string_to_number(5) == 5
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("a") is None
