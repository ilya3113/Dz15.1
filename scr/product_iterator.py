class ProductIterator:
    """
    Класс для итерации по списку объектов

    item: (list) Список для итерации
    """
    def __init__(self, item: list) -> None:
        self.item = item

    def __iter__(self) -> object:
        """
        Функция создает итерируемый объект

        :return (object) объект итерации
        """
        self.index = -1
        return self

    def __next__(self) -> iter:
        """
        Функция итерируется по объекту

        :return (iter) содержимое объекта
        """
        if self.index + 1 < len(self.item):
            self.index += 1
            return self.item[self.index]
        else:
            raise StopIteration
