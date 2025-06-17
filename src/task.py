class Product:
    """Класс представляющий товар"""

    def __init__(self, name, description, price, quantity):
        """Инициализирует новый экземпляр класса Product"""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

        # self.product_list.append(
        #     {
        #         "name": self.name,
        #         "description": self.description,
        #         "price": self.price,
        #         "quantity": self.quantity
        #     }
        # )

    @classmethod
    def new_product(cls, products, products_list=None):
        if products_list:
            for prod in products_list:
                if prod['name'] == products['name']:
                    if prod['price'] < products['price']:
                        return cls(products.get('name', ''), products.get('description'), products.get('price', 0),
                                   products.get("quantity", 0) + prod['quantity'])
                    else:
                        return cls(products.get('name', ''), products.get('description'), prod['price'],
                                   products.get("quantity", 0) + prod['quantity'])
        return cls(products.get('name', ''), products.get('description', ''), products.get('price', 0),
                   products.get("quantity", 0))

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if str(new_price).startswith("-"):
            user_input = input("Подтвердите понижение цены (да/нет)\n> ").lower().strip()
            if user_input != 'да':
                pass
            elif user_input == 'да' and self._price + new_price > 0:
                self._price += new_price
            else:
                print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price += new_price


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
        self.__products.append(product)
        self.product_count += 1

    @property
    def products(self):
        products = []
        for product in self.__products:
            products.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return products
