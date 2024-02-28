import json
from src.category import Category
from src.product import Product


def creates_instance_class() -> tuple:
    """
    Функция считывает json файл и отдает кортеж со значениями

    :return (tuple) значения ключей файла json
    """
    with open("../files/products.json") as f:
        f = json.load(f)
        instance_category = []
        instance_product = []
        instance_product_phone = []
        instance_product_tv = []
        for elem in f:
            if elem["name"] == "Смартфоны":
                for el in elem["products"]:
                    instance_product_phone.append(Product(el["name"], el["description"], el["price"], el["quantity"]))
                instance_category.append(Category(elem["name"], elem["description"], instance_product_phone))

            if elem["name"] == "Телевизоры":
                for el in elem["products"]:
                    instance_product_tv.append(Product(el["name"], el["description"], el["price"], el["quantity"]))
                instance_category.append(Category(elem["name"], elem["description"], instance_product_tv))

            for el in elem["products"]:
                instance_product.append(Product(el["name"], el["description"], el["price"], el["quantity"]))

        return instance_category, instance_product
