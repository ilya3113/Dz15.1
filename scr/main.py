from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator
from utils.pars_json import creates_instance_class


def main():
    instance_category, instance_product = creates_instance_class()
    cat = Category(*instance_category[0])
    list_ = cat.product
    pi = ProductIterator(list_)
    for i in pi:
        print(i)


if __name__ == "__main__":
    main()