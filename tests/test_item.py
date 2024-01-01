import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def item_fixture1():
    return Item("test_2", 12.4, 2)


@pytest.fixture
def item_fixture2():
    return Item("test_3", 50, 3)


@pytest.fixture
def phone_fixture1():
    return Phone("Astra", 5000, 1, 2)


# obj = Item("test_1", 12.4, 2)

def test__item_init(item_fixture1):
    assert item_fixture1.name == "test_2"
    assert item_fixture1.price == 12.4
    assert item_fixture1.quantity == 2


def test__item_str(item_fixture1):
    assert str(item_fixture1) == 'test_2'


def test__item_repr(item_fixture1):
    assert repr(item_fixture1) == "Item('test_2', 12.4, 2)"


def test__item_add2(item_fixture1, item_fixture2, phone_fixture1):
    with pytest.raises(Exception, match=r"Складывать нужно ЭК класса."):
        item_fixture1 + 10

    assert item_fixture1 + item_fixture2 == 5
    assert item_fixture1 + phone_fixture1 == 3
    assert item_fixture2 + phone_fixture1 == 4
    assert phone_fixture1 + item_fixture1 == 3


def test__name(item_fixture1):
    item_fixture1.name = "test2_from_setter"
    assert item_fixture1.name == "test2_from"


def test__calculate_total_price(item_fixture1):
    assert item_fixture1.calculate_total_price() == 24.8


def test__apply_discount_1(item_fixture1):
    item_fixture1.pay_rate = 0.5
    item_fixture1.apply_discount()
    assert item_fixture1.price == 6.2


def test__apply_discount_2(item_fixture1):
    item_fixture1.pay_rate = 3
    item_fixture1.apply_discount()
    assert item_fixture1.price == 37.2


def test__item_all(item_fixture1):
    start_len = len(Item.all)
    n = 10
    for i in range(n):
        Item(f"obj_{i}", i / 1, i)

    assert len(Item.all) == n + start_len


def test__string_to_number():
    assert Item.string_to_number(5) == 5
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("a") is None
