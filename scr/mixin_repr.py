class MixinRepr:

    def __init__(self, *args, **kwargs) -> None:
        """
        Функция печатает информацию для разработчика
        какой объект был создан и с какими свойствами

        :return None
        """
        print(repr(self))

    def __repr__(self) -> str:
        """
        Функция возвращает строковое отображение объекта при его создании

        :return (str) объект и его свойства
        """
        return f"{self.__class__.__name__}({self.__dict__.items()})"
