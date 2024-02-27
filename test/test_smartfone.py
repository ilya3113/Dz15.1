from scr.smartphone import Smartphone


def test_init_smartphone(test_smartphone):
    assert test_smartphone.name == "Samsung Galaxy"
    assert test_smartphone.description == "Хорошая камера"
    assert test_smartphone.price == 180_000.0
    assert test_smartphone.quantity == 5
    assert test_smartphone.performance == 2.5
    assert test_smartphone.model == "C23 Ultra"
    assert test_smartphone.memory == 6
    assert test_smartphone.color == "Серый цвет"


def test_creates_product_smartphone(test_smartphone):
    assert Smartphone.creates_product({
        "name": "Samsung Galaxy",
        "description": "Хорошая камера",
        "price": 180_000.0,
        "quantity": 5,
        "performance": 2.5,
        "model": "C23 Ultra",
        "memory": 6,
        "color": "Серый цвет"
    })


def test_repr_smartphone(test_smartphone):
    assert test_smartphone.__repr__() == ("Smartphone(dict_items([('name', 'Samsung Galaxy'),"
                                          " ('description', 'Хорошая камера'),"
                                          " ('price', 180000.0),"
                                          " ('quantity', 5),"
                                          " ('color', 'Серый цвет'),"
                                          " ('performance', 2.5),"
                                          " ('model', 'C23 Ultra'),"
                                          " ('memory', 6)]))")
