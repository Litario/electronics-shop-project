import pytest

from src.keyboard import Keyboard


@pytest.fixture()
def keyboard_fixture():
    return Keyboard("A4tech", 2000, 3)


def test__keyboard_init(keyboard_fixture):
    assert keyboard_fixture.name == "A4tech"
    assert keyboard_fixture.price == 2000
    assert keyboard_fixture.quantity == 3
    assert keyboard_fixture.language == 'EN'


def test__keyboard_str(keyboard_fixture):
    assert str(keyboard_fixture) == "A4tech"


def test__keyboard_repr(keyboard_fixture):
    assert repr(keyboard_fixture) == "Keyboard('A4tech', 2000, 3, 'EN')"


def test__name(keyboard_fixture):
    keyboard_fixture.name = '12345'
    assert keyboard_fixture.name == '12345'

    keyboard_fixture.name = '12345678910'
    assert keyboard_fixture.name == '1234567891'


def test__calculate_total_price(keyboard_fixture):
    assert keyboard_fixture.calculate_total_price() == 6000


def test__change_lang(keyboard_fixture):
    keyboard_fixture.change_lang()
    assert keyboard_fixture.language == 'RU'

    keyboard_fixture.change_lang()
    assert keyboard_fixture.language == 'EN'

    keyboard_fixture.change_lang()
    assert keyboard_fixture.language == 'RU'
