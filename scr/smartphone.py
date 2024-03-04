from src.abstract_product import AbstractProduct
from src.product import Product


class Smartphone(Product, AbstractProduct):
    """
    Класс Смартфоны:

    name: (str) название смартфона
    description: (str) описание смартфона
    price: (float) цена смартфона
    quantity (ini) количество в наличии
    performance (float) производительность
    model (str) модель смартфона
    memory (int) объем встроенной памяти
    color (str) цвет смартфона
    """

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 performance: float, model: str, memory: int, color: str):
        self.performance = performance
        self.model = model
        self.memory = memory
        super().__init__(name, description, price, quantity, color)

    @classmethod
    def creates_product(cls, product: dict) -> object:
        """
        Класс метод который принимает словарь и создает новый объект класса Product

        :product (dict) продукт по которому создаст объект

        :return (object) объект класса Product
        """
        return cls(product["name"], product["description"], product["price"], product["quantity"],
                   product["performance"], product["model"], product["memory"], product["color"])
