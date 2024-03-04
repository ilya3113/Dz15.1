class ProductError(Exception):
    """
    Пользовательский класс исключений
    """
    def __init__(self, *args, **kwargs) -> None:
        self.message = args[0] if args else "Ошибка с продуктом."

    def __str__(self):
        return self.message


class ProductQuantityZeroError(ProductError):
    """
    Класс исключений когда в аргументы передается некорректное значение
    """
    def __init__(self, *args):
        self.message = args[0] if args else "ProductQuantityZeroError: Невозможно посчитать количество товара."
