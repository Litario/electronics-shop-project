import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone_fixture1():
    return Phone("Astra", 5000, 1, 2)


@pytest.fixture
def item_fixture1():
    return Item("test_2", 12.4, 2)


def test__item_init(phone_fixture1):
    assert phone_fixture1.name == "Astra"
    assert phone_fixture1.price == 5000
    assert phone_fixture1.quantity == 1
    assert phone_fixture1.number_of_sim == 2


def test__phone_n_sim(phone_fixture1):
    assert phone_fixture1.n_sim == 2

    phone_fixture1.n_sim = 1
    assert phone_fixture1.n_sim == 1

    for i in (-1, 0, 0.5):
        with pytest.raises(ValueError):
            phone_fixture1.n_sim = i
