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
