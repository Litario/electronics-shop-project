from src.item import Item

obj = Item("telephone", 12.4, 2)


def test__item_init():
    assert obj.name == "telephone"
    assert obj.price == 12.4
    assert obj.quantity == 2


def test__item_calculate_total_price():
    assert obj.calculate_total_price() == 24.8


def test__item_apply_discount():
    obj.pay_rate = 0.5
    obj.apply_discount()
    assert obj.price == 6.2


def test__item_apply_discount():
    obj.pay_rate = 3
    obj.apply_discount()
    assert obj.price == 37.2


def test__item_all():
    pass
