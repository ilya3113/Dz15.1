import pytest
from scr.product_iterator import ProductIterator
from pars_json import creates_instance_class
from scr.lawn_grass import LawnGrass
from scr.smartphone import Smartphone


@pytest.fixture
def test_category():
    instance_category, instance_product = creates_instance_class()
    return instance_category[0]


@pytest.fixture
def test_product():
    instance_category, instance_product = creates_instance_class()
    return instance_product[0]


@pytest.fixture
def test_pars_json():
    return creates_instance_class()


@pytest.fixture
def test_iterator():
    instance_category, instance_product = creates_instance_class()
    return ProductIterator(instance_category[0].product)


@pytest.fixture
def test_smartphone():
    return Smartphone("Samsung Galaxy", "Хорошая камера", 180_000.0, 5, 2.5, "C23 Ultra", 6, "Серый цвет")


@pytest.fixture
def test_lawn_grass():
    return LawnGrass("Газон", "Густая красивая трава", 150.0, 200, "Китай", 3.5, "Зеленый цвет")
