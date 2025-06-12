import pytest

from src.task import Product, Category


@pytest.fixture
def sample_product_1():
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=6
    )


@pytest.fixture
def sample_product_2():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )


@pytest.fixture
def sample_category(sample_product_1, sample_product_2):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации",
        products=[sample_product_1, sample_product_2]
    )


@pytest.fixture
def sample_product():
    return [{
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        "products": [
            {
                "name": "55\" QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000.0,
                "quantity": 7
            }
        ]
    }]


@pytest.fixture
def valid_input_data():
    return [
        {
            "name": "Электроника",
            "description": "Гаджеты и устройства",
            "products": [
                {"name": "Смартфон", "description": "", "price": 999.99, "quantity": 10},
                {"name": "Ноутбук", "description": "", "price": 1499.99, "quantity": 5}
            ]
        },
        {
            "name": "Одежда",
            "description": "Мужская и женская одежда",
            "products": [
                {"name": "Футболка", "description": "", "price": 19.99, "quantity": 50},
                {"name": "Джинсы", "description": "", "price": 59.99, "quantity": 30}
            ]
        }
    ]


@pytest.fixture
def invalid_input_data():
    return [
        {
            "name": "Электроника",
            "description": "Гаджеты и устройства",
            "products": [
                {"name": "Смартфон", "description": "", "price": "invalid_price"},  # Неправильный тип цены
                {"name": "Ноутбук", "description": "", "price": 1499.99, "quantity": 5}
            ]
        }
    ]
