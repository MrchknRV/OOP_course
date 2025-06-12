class Product:
    """Класс представляющий товар"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализирует новый экземпляр класса Product"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс представляющий категорию товаров"""
    name: str
    description: str
    products: list

    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        """Инициализирует новый экземпляр класса Category"""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products) if products else 0
