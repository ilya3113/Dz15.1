from scr.product import Product


class LawnGrass(Product):
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
    def __init__(self, name: str, description: str, price: float, quantity: int, manufacturer: str, germination_period: float, color: str):
        super().__init__(name, description, price, quantity, color)
        self.manufacturer = manufacturer
        self.germination_period = germination_period