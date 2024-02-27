class MixinRepr:

    def __repr__(self) -> str:
        """
        Функция возвращает строковое отображение объекта при его создании

        :return (str) объект и его свойства
        """
        return f"{self.__class__.__name__}({self.__dict__.items()})"
