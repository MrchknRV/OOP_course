from src.task import Category


class CategoryIterator:
    def __init__(self, obj):
        if isinstance(obj, Category):
            self.obj = obj
            self.index = 0
        else:
            raise ValueError("Неверный формат данных")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.obj.products):
            prod = self.obj.products[self.index]
            self.index += 1
            return prod

        raise StopIteration
