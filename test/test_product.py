from scr.product import Product


def test_init_product(test_product):
    assert test_product.name == "Samsung Galaxy C23 Ultra"
    assert test_product.description == "256GB, Серый цвет, 200MP камера"
    assert test_product.price == 180_000.0
    assert test_product.quantity == 5


def test_creates_product(test_product):
    assert Product.creates_product({
        "name": "Xiaomi 14 Pro",
        "description": "Влагозащищенный корпус",
        "price": 190_000.0,
        "quantity": 5
    })


def test_price_product(test_product):
    assert test_product.price == 180_000.0
    test_product.price = 185_000.0
    assert test_product.price == 185_000.0


def test_str_product(test_product):
    assert test_product.__str__() == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_product(test_product):
    assert test_product.__add__(Product.creates_product({
        "name": "Xiaomi 14 Pro",
        "description": "Влагозащищенный корпус",
        "price": 190_000.0,
        "quantity": 5
    })) == 1_850_000.0