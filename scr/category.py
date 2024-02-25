class Category:
    """
    name: (str) название категории
    description: (str) описание категории
    product: (list) список продуктов
    count_category: (int) количество категорий (default 0)
    count_product: (int) количество продуктов (default 0)
    """
    count_category: int = 0
    count_product: int = 0

    def __init__(self, name: str, description: str, product: list) -> None:
        self.name = name
        self.description = description
        self.__product = product
        self.count_category += 1
        self.count_product += len(product)

    def __str__(self) -> str:
        """
        Функция отображает определенные данные в строковом формате

        :return (str) название категории и количество продуктов
        """
        return f"{self.name}, количество продуктов: {len(self.__product)} шт."

    def add_product(self, value: object) -> None:
        """
        Функция добавляет в список продуктов новый продукт
        """
        self.__product.append(value)

    @property
    def product(self) -> list:
        """
        Функция геттер которая выводит на экран список товаров в специальном формате

        :return (list) список продуктов
        """
        list_products = []
        for product in self.__product:
            list_products.append(f"{product["name"]}, {product["price"]} руб. Остаток: {product["quantity"]} шт.")

        return list_products