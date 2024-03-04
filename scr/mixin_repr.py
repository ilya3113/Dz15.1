class MixinRepr:

    def __init__(self, *args):
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
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v},'
        return f"создан объект со свойствами {object_attributes})"
