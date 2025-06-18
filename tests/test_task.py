from unittest.mock import patch

from src.task import Product


def test_init_category(sample_category):
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Смартфоны, как средство не только коммуникации"
    assert len(sample_category.products) == 2

    assert sample_category.category_count == 1
    assert sample_category.product_count == 2


def test_init_product1(sample_product_1):
    assert sample_product_1.name == "Samsung Galaxy C23 Ultra"
    assert sample_product_1.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product_1.price == 180000.0
    assert sample_product_1.quantity == 6


def test_init_product2(sample_product_2):
    assert sample_product_2.name == "Iphone 15"
    assert sample_product_2.description == "512GB, Gray space"
    assert sample_product_2.price == 210000.0
    assert sample_product_2.quantity == 8


def test_add_new_product():
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_price_change_positive(sample_product_1):
    sample_product_1.price = 800
    assert sample_product_1.price == 180800.0


def test_price_change_negative_success(sample_product_1):
    with patch("builtins.input", return_value="да"):
        sample_product_1.price = -1000

    assert sample_product_1.price == 179000.0


def test_price_change_negative(sample_product_1):
    with patch("builtins.input", return_value="нет"):
        sample_product_1.price = -1000

    assert sample_product_1.price == 180000.0


def test_price_change_negative_err(sample_product_1, capsys):
    with patch("builtins.input", return_value="да"):
        sample_product_1.price = -200000

    captured = capsys.readouterr()
    res = captured.out.split("\n")
    assert res[0] == "Цена не должна быть нулевая или отрицательная"
    assert sample_product_1.price == 180000.0


def test_price_change_with_str_input(sample_product_1):
    sample_product_1.price = "1000"
    assert sample_product_1.price == 181000.0


def test_add_product_in_category(sample_category):
    product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    sample_category.add_product(product)
    assert len(sample_category.products) == 3
    assert sample_category.product_count == 3


def test_category_products(sample_category):
    assert len(sample_category.products) == 2
    assert sample_category.products[0] == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 6 шт."
