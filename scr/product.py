from src.abstract_product import AbstractProduct
from src.mixin_repr import MixinRepr


class Product(AbstractProduct, MixinRepr):
    """
    name: (str) название продукта
    description: (str) описание продукта
    price: (float) цена товара
    quantity: (int) остаток товара
    color: (str) цвет продукта (default None)
    """

    def __init__(self, name: str, description: str, price: float, quantity: int, color=None) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.color = color
        super().__init__()

    def __str__(self) -> str:
        """
        Функция отображает определенные данные в строковом формате

        :return (str) название продукта, цена, остаток
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        """
        Функция возвращает строковое отображение объекта при его создании

        :return (str) объект и его свойства
        """
        return super().__repr__()

    def __len__(self) -> int:
        """
        Функция считает количество продукта в наличии

        :return (int) количество продуктов в наличии
        """
        return self.quantity

    def __add__(self, other) -> float:
        """
        Функция складывает цену и количество продуктов

        :return (float) общая стоимость продуктов
        """
        if type(other) is not type(self):
            raise TypeError("Складывать можно только объекты из одинаковых категорий")

        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def get_price(self) -> float:
        """
        Геттер для свойства цены

        :return (float) цена продукта
        """
        return self.price

    @get_price.setter
    def get_price(self, value: float) -> None:
        """
        Сеттер для свойства цены, устанавливает новое значение если оно больше 0
        """
        if value <= 0:
            print("цена введена некорректная")
        elif value < self.price:
            while True:
                answer = input("Вы уверены что хотите понизить цену: (y/n)").lower()
                if answer == "y":
                    self.price = value
                    break

                elif answer == "n":
                    self.price = self.price
                    break

        else:
            self.price = value

    @classmethod
    def creates_product(cls, product: dict, list_product: list) -> object:
        """
        Класс метод который принимает словарь и создает новый объект класса Product
        если такого объекта еще нет в списке продуктов

        :product (dict) продукт по которому создаст объект

        :list_product (list) список уже существующих продуктов

        :return (object) объект класса Product
        """
        for elem in list_product:
            if elem.name in product.get("name"):
                elem.quantity += product.get("quantity")
                if elem.price != product.get("price"):
                    elem.price = elem.price if elem.price > product.get("price") else product.get("price")

        return cls(product["name"], product["description"], product["price"], product["quantity"])
