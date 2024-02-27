from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone
from utils.pars_json import creates_instance_class


def main():
    instance_category, instance_product = creates_instance_class()
    print(repr(Product.creates_product({
        "name": "Xiaomi 14 Pro",
        "description": "Влагозащищенный корпус",
        "price": 190_000.0,
        "quantity": 5
    })))


if __name__ == "__main__":
    main()
