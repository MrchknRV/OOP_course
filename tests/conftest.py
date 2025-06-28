import pytest

from src.category_iterator import CategoryIterator
from src.product_heirs import LawnGrass, Smartphone
from src.task import Category, Product


@pytest.fixture
def sample_product_1():
    return Product(
        name="Samsung Galaxy C23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=6
    )


@pytest.fixture
def sample_product_2():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def sample_category(sample_product_1, sample_product_2):
    Category.product_count = 0
    Category.category_count = 0
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации",
        products=[sample_product_1, sample_product_2],
    )


@pytest.fixture
def sample_product():
    return [
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        }
    ]


@pytest.fixture
def valid_input_data():
    return [
        {
            "name": "Электроника",
            "description": "Гаджеты и устройства",
            "products": [
                {"name": "Смартфон", "description": "", "price": 999.99, "quantity": 10},
                {"name": "Ноутбук", "description": "", "price": 1499.99, "quantity": 5},
            ],
        },
        {
            "name": "Одежда",
            "description": "Мужская и женская одежда",
            "products": [
                {"name": "Футболка", "description": "", "price": 19.99, "quantity": 50},
                {"name": "Джинсы", "description": "", "price": 59.99, "quantity": 30},
            ],
        },
    ]


@pytest.fixture
def invalid_input_data():
    return [
        {
            "name": "Электроника",
            "description": "Гаджеты и устройства",
            "products": [
                {"name": "Смартфон", "description": "", "price": "invalid_price"},  # Неправильный тип цены
                {"name": "Ноутбук", "description": "", "price": 1499.99, "quantity": 5},
            ],
        }
    ]


@pytest.fixture
def sample_iterator(sample_category):
    return CategoryIterator(sample_category)


@pytest.fixture
def sample_smartphone_product1():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def sample_smartphone_product2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def sample_category_smartphones(sample_smartphone_product1, sample_smartphone_product2):
    Category.product_count = 0
    Category.category_count = 0
    return Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [sample_smartphone_product1, sample_smartphone_product2]
    )


@pytest.fixture
def sample_grass_product1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def sample_grass_product2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def sample_category_grasses(sample_grass_product1, sample_grass_product2):
    Category.product_count = 0
    Category.category_count = 0
    return Category("Газонная трава", "Различные виды газонной травы", [sample_grass_product1, sample_grass_product2])
