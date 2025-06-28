import pytest

from src.product_heirs import LawnGrass, Smartphone
from src.task import Category, Product


def test_init_smartphone(sample_smartphone_product1):
    assert sample_smartphone_product1.name == "Iphone 15"
    assert sample_smartphone_product1.description == "512GB, Gray space"
    assert sample_smartphone_product1.price == 210000.0
    assert sample_smartphone_product1.quantity == 8
    assert sample_smartphone_product1.efficiency == 98.2
    assert sample_smartphone_product1.model == "15"
    assert sample_smartphone_product1.memory == 512
    assert sample_smartphone_product1.color == "Gray space"
    assert issubclass(Smartphone, Product) is True


def test_init_lawngrass(sample_grass_product1):
    assert sample_grass_product1.name == "Газонная трава"
    assert sample_grass_product1.description == "Элитная трава для газона"
    assert sample_grass_product1.price == 500.0
    assert sample_grass_product1.quantity == 20
    assert sample_grass_product1.country == "Россия"
    assert sample_grass_product1.germination_period == "7 дней"
    assert sample_grass_product1.color == "Зеленый"
    assert issubclass(LawnGrass, Product) is True


def test_equal_type(sample_smartphone_product1, sample_smartphone_product2):
    res = sample_smartphone_product2 + sample_smartphone_product1
    assert res == 2114000.0


def test_unequal_type(sample_smartphone_product1, sample_grass_product1):
    with pytest.raises(TypeError) as exc:
        sample_smartphone_product1 + sample_grass_product1
        assert exc.value == "Возникла ошибка при попытке сложения"


def test_add_equal_type_product(sample_category_smartphones):
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    sample_category_smartphones.add_product(smartphone)
    assert len(sample_category_smartphones.products) == 3
    assert sample_category_smartphones.product_count == 3


def test_add_equal_product1(sample_category_smartphones, sample_grass_product1):
    with pytest.raises(TypeError) as exc:
        sample_category_smartphones.add_product(sample_grass_product1)
        assert exc.value == "Неверный тип продукта для данной категории"


def test_add_equal_product_for_empty_category(sample_smartphone_product1, sample_smartphone_product2):
    Category.category_count = 0
    Category.product_count = 0
    cur_category = Category("Smartphone", "test descr")
    cur_category.add_product(sample_smartphone_product1)
    cur_category.add_product(sample_smartphone_product2)
    assert len(cur_category.products) == 2
    assert cur_category.category_count == 1
    assert cur_category.product_count == 2


def test_add_unequal_product(sample_category_grasses):
    with pytest.raises(TypeError) as exc:
        sample_category_grasses.add_product("Not a product")
        assert exc.value == "Недопустимый тип продукта"
