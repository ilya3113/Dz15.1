from scr.category import Category
from scr.product import Product
from test.pars_json import creates_instance_class


def main():
    instance_category, instance_product = creates_instance_class()
    cat = Category(*instance_category[0])
    cat.add_product(Product.creates_product({
        "name": "Xiaomi 14 Pro",
        "description": "Влагозащищенный корпус",
        "price": 190_000.0,
        "quantity": 5
    }))
    print(cat.product)
    # Smartphone("Samsung Galaxy", "Хорошая камера", 180_000.0, 5, 2.5, "C23 Ultra", 6, "Серый цвет")