import pytest

from src.category_iterator import CategoryIterator


def test_success_iteration(sample_iterator):
    assert sample_iterator.index == 0
    assert next(sample_iterator) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 6 шт."
    assert next(sample_iterator) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    with pytest.raises(StopIteration):
        next(sample_iterator)


def test_invalid_data():
    with pytest.raises(ValueError):
        iterator = CategoryIterator([])
        for prod in iterator:
            assert prod == "Неверный формат данных"
