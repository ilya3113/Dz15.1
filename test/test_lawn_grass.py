from scr.lawn_grass import LawnGrass


def test_init_lawn_grass(test_lawn_grass):
    assert test_lawn_grass.name == "Газон"
    assert test_lawn_grass.description == "Густая красивая трава"
    assert test_lawn_grass.price == 150.0
    assert test_lawn_grass.quantity == 200
    assert test_lawn_grass.manufacturer == "Китай"
    assert test_lawn_grass.germination_period == 3.5
    assert test_lawn_grass.color == "Зеленый цвет"


def test_creates_product_smartphone(test_smartphone):
    assert LawnGrass.creates_product({
        "name": "Газон",
        "description": "Густая красивая трава",
        "price": 150.0,
        "quantity": 200,
        "manufacturer": "Китай",
        "germination_period": 3.5,
        "color": "Зеленый цвет"
    })


def test_repr_lawn_grass(test_lawn_grass):
    assert test_lawn_grass.__repr__() == ("LawnGrass(dict_items([('name', 'Газон'),"
                                          " ('description', 'Густая красивая трава'),"
                                          " ('price', 150.0), ('quantity', 200),"
                                          " ('color', 'Зеленый цвет'),"
                                          " ('manufacturer', 'Китай'),"
                                          " ('germination_period', 3.5)]))")
