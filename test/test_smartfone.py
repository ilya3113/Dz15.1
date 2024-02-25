def test_init_smartphone(test_smartphone):
    assert test_smartphone.name == "Samsung Galaxy"
    assert test_smartphone.description == "Хорошая камера"
    assert test_smartphone.price == 180_000.0
    assert test_smartphone.quantity == 5
    assert test_smartphone.performance == 2.5
    assert test_smartphone.model == "C23 Ultra"
    assert test_smartphone.memory == 6
    assert test_smartphone.color == "Серый цвет"