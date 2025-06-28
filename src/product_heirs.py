from src.task import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Расширяет инициализатор нового экземпляра класса-наследника Smartphone"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Расширяет инициализатор нового экземпляра класса-наследника LawnGrass"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
