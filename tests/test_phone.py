import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone_fixture():
    return Phone("Astra", 5000, 1, 2)


@pytest.fixture
def item_fixture():
    return Item("test_2", 12.4, 2)


def test__item_init(phone_fixture):
    assert phone_fixture.name == "Astra"
    assert phone_fixture.price == 5000
    assert phone_fixture.quantity == 1
    assert phone_fixture.number_of_sim == 2


def test__phone_sim(phone_fixture):
    assert phone_fixture.number_of_sim == 2

    phone_fixture.number_of_sim = 1
    assert phone_fixture.number_of_sim == 1

    for i in (-1, 0, 0.5):
        with pytest.raises(ValueError):
            phone_fixture.number_of_sim = i
