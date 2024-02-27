from src.abstract_product import AbstractProduct
from src.product import Product


class LawnGrass(Product, AbstractProduct):
    """
    Класс Трава Газонная

    name: (str) название травы
    description: (str) описание травы
    price: (float) цена травы
    quantity; (int) количество в наличии
    manufacturer (str) страна производитель
    germination_period (float) срок прорастания
    color (str) цвет травы
    """
    def __init__(self, name: str, description: str, price: float, quantity: int, manufacturer: str,
                 germination_period: float, color: str):
        super().__init__(name, description, price, quantity, color)
        self.manufacturer = manufacturer
        self.germination_period = germination_period

    @classmethod
    def creates_product(cls, product: dict) -> object:
        """
        Класс метод который принимает словарь и создает новый объект класса Product

        :product (dict) продукт по которому создаст объект

        :return (object) объект класса Product
        """
        return cls(product["name"], product["description"], product["price"], product["quantity"],
                   product["manufacturer"], product["germination_period"], product["color"])
