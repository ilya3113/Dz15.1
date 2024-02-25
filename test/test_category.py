def test_init_category(test_category):
    assert test_category.name == "Смартфоны"
    assert test_category.description == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    assert test_category.count_product == 3
    assert test_category.count_category == 1


def test_add_product_in_category(test_category, test_product):
    test_category.add_product(test_product)


def test_product_category(test_category):
    assert test_category.product == ["Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.", "Iphone 15, 210000.0 руб. Остаток: 8 шт.", "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."]


def test_str_category(test_category):
    assert test_category.__str__() == "Смартфоны, количество продуктов: 3 шт."
