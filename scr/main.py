from exceptions.exceptions import ProductQuantityZeroError
from src.category import Category
from src.order import Order
from src.product import Product


def main():
    cat = Category("Смартфоны", "Лучший дизайн", [
        Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5),
    ])
    print(cat.product)
    Product.creates_product({
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 190_000.0,
        "quantity": 5
    }, cat.copy_product)

    print(cat.product)


if __name__ == "__main__":
    try:
        main()
    except ProductQuantityZeroError as e:
        print(e)
    else:
        print("Товар был успешно добавлен")
    finally:
        print("Обработка добавления товара завершена")
