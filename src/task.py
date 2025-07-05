from src.base_product import BaseProduct
from src.mixins import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс представляющий товар"""

    def __init__(self, name, description, price, quantity):
        """Инициализирует новый экземпляр класса Product"""
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

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
            if type(self) is type(other):
                return self.price * self.quantity + other.price * other.quantity
            raise TypeError("Возникла ошибка при попытке сложения")
        return NotImplemented


class Category:
    """Класс представляющий категорию товаров"""

    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=[]):
        """Инициализирует новый экземпляр класса Category"""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products) if self.__products else 0

    def add_product(self, product):
        """Функция добавляет продукт в список продуктов и увеличивает счетчик."""
        if isinstance(product, Product):
            if len(self.__products) != 0:
                if type(self.__products[0]) is type(product):
                    self.__products.append(product)
                    self.product_count += 1
                else:
                    raise TypeError("Неверный тип продукта для данной категории")
            else:
                self.__products.append(product)
                self.product_count += 1

        else:
            raise TypeError("Недопустимый тип продукта")

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

    def average_price(self):
        """Метод, который подсчитывает средний ценник всех товаров."""
        try:
            summ = 0
            for product in self.__products:
                summ += product.price * product.quantity
            return round(summ / len(self.__products))
        except ZeroDivisionError:
            return 0
