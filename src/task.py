class Product:
    """Класс представляющий товар"""

    def __init__(self, name, description, price, quantity):
        """Инициализирует новый экземпляр класса Product"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, products, products_list=None):
        """Создает новый товар или обновляет существующий"""
        if products_list:
            for prod in products_list:
                if prod["name"] == products["name"]:
                    if prod["price"] < products["price"]:
                        return cls(
                            products.get("name", ""),
                            products.get("description"),
                            products.get("price", 0),
                            products.get("quantity", 0) + prod["quantity"],
                        )
                    else:
                        return cls(
                            products.get("name", ""),
                            products.get("description"),
                            prod["price"],
                            products.get("quantity", 0) + prod["quantity"],
                        )
        return cls(
            products.get("name", ""),
            products.get("description", ""),
            products.get("price", 0),
            products.get("quantity", 0),
        )

    @property
    def price(self):
        """Возвращает цену товара"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Устанавливает новую цену товара"""
        if isinstance(new_price, str):
            new_price = float(new_price)
        if str(new_price).startswith("-"):
            user_input = input("Подтвердите понижение цены (да/нет)\n> ").lower().strip()
            if user_input != "да":
                pass
            elif user_input == "да" and self.__price + new_price > 0:
                self.__price += new_price
            else:
                print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price += new_price

    def __str__(self):
        """Функция возвращает строковое представление продукта."""
        return f"{self.name.title()}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Функция складывает общую стоимость двух продуктов."""
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        return NotImplemented


class Category:
    """Класс представляющий категорию товаров"""

    product_count = 0
    category_count = 0

    def __init__(self, name, description, products):
        """Инициализирует новый экземпляр класса Category"""
        self.name = name
        self.description = description
        self.__products = products

        self.category_count += 1
        self.product_count += len(self.__products) if self.__products else 0

    def add_product(self, product):
        """Функция добавляет продукт в список продуктов и увеличивает счетчик."""
        self.__products.append(product)
        self.product_count += 1

    def __str__(self):
        """Функция возвращает строковое представление продукта."""
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    @property
    def products(self):
        """Функция возвращает список строковых представлений всех продуктов."""
        products = []
        for product in self.__products:
            products.append(str(product))
        return products
