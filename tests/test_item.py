import pytest

from src.item import Item


@pytest.fixture
def item_fixture():
    return Item("test_2", 12.4, 2)


# obj = Item("test_1", 12.4, 2)

def test__item_init(item_fixture):
    assert item_fixture.name == "test_2"
    assert item_fixture.price == 12.4
    assert item_fixture.quantity == 2


def test__item_str(item_fixture):
    assert str(item_fixture) == 'test_2'


def test__item_repr(item_fixture):
    assert repr(item_fixture) == "Item('test_2', 12.4, 2)"


def test__name(item_fixture):
    item_fixture.name = "test2_from_setter"
    assert item_fixture.name == "test2_from"


def test__calculate_total_price(item_fixture):
    assert item_fixture.calculate_total_price() == 24.8


def test__apply_discount_1(item_fixture):
    item_fixture.pay_rate = 0.5
    item_fixture.apply_discount()
    assert item_fixture.price == 6.2


def test__apply_discount_2(item_fixture):
    item_fixture.pay_rate = 3
    item_fixture.apply_discount()
    assert item_fixture.price == 37.2


def test__item_all(item_fixture):
    start_len = len(Item.all)
    n = 10
    for i in range(n):
        Item(f"obj_{i}", i / 1, i)

    assert len(Item.all) == n + start_len


def test__string_to_number():
    assert Item.string_to_number(5) == 5
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("a") == None
