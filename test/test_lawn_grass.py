def test_init_lawn_grass(test_lawn_grass):
    assert test_lawn_grass.name == "Газон"
    assert test_lawn_grass.description == "Густая красивая трава"
    assert test_lawn_grass.price == 150.0
    assert test_lawn_grass.quantity == 200
    assert test_lawn_grass.manufacturer == "Китай"
    assert test_lawn_grass.germination_period == 3.5
    assert test_lawn_grass.color == "Зеленый цвет"