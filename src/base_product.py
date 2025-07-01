from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для создания продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs): ...

    @abstractmethod
    def __add__(self, other): ...
