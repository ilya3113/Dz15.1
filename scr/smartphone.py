from scr.product import Product


class Smartphone(Product):
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
    def __init__(self, name: str, description: str, price: float, quantity: int, performance: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity, color)
        self.performance = performance
        self.model = model
        self.memory = memory