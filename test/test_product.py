import pytest

from src.category import Category
from src.product import Product


def test_init_product(test_product):
    assert test_product.name == "Samsung Galaxy C23 Ultra"
    assert test_product.description == "256GB, Серый цвет, 200MP камера"
    assert test_product.price == 180_000.0
    assert test_product.quantity == 5


def test_creates_product(test_product, test_create_product):
    assert Product.creates_product({
        "name": "Xiaomi 14 Pro",
        "description": "Влагозащищенный корпус",
        "price": 190_000.0,
        "quantity": 5
    }, test_create_product)

    assert test_create_product[0].quantity == 5
    assert test_create_product[0].price == 180_000.0

    assert Product.creates_product({
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 190000.0,
        "quantity": 5
      }, test_create_product)

    assert test_create_product[0].quantity == 10
    assert test_create_product[0].price == 190_000.0

    assert Product.creates_product({
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 150000.0,
        "quantity": 5
    }, test_create_product)

    assert test_create_product[0].quantity == 15
    assert test_create_product[0].price == 190_000.0


def test_get_price_product(test_product):
    assert test_product.get_price == 180_000.0
    test_product.get_price = 185_000.0
    assert test_product.get_price == 185_000.0


def test_str_product(test_product):
    assert test_product.__str__() == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_len_product(test_product):
    assert test_product.__len__() == 5


def test_add_product(test_product, test_create_product):
    assert test_product.__add__(Product.creates_product({
        "name": "Xiaomi 14 Pro",
        "description": "Влагозащищенный корпус",
        "price": 190_000.0,
        "quantity": 5
    }, test_create_product)) == 1_850_000.0


def test_repr_product(test_product):
    assert test_product.__repr__() == ("Product(dict_items([('name', 'Samsung Galaxy C23 Ultra'),"
                                       " ('description', '256GB, Серый цвет, 200MP камера'),"
                                       " ('price', 180000.0),"
                                       " ('quantity', 5),"
                                       " ('color', None)]))")


def test_add_raise_product(test_product, test_smartphone):
    with pytest.raises(TypeError):
        assert test_product.__add__(test_smartphone) == 1_800_000.0
