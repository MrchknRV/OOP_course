import json
from unittest.mock import mock_open, patch

from src.utils import load_json_data, create_object
from src.task import Category, Product


def test_load_json_data_file_not_found():
    result = load_json_data("test.json")
    assert result == []


def test_load_json_data(sample_product):
    json_content = json.dumps(sample_product)
    with patch("builtins.open", mock_open(read_data=json_content)) as mock_file:
        result = load_json_data("any_path.json")
        assert result == sample_product
        mock_file.assert_called_once_with("any_path.json", "r", encoding="UTF-8")


def test_create_object_success(valid_input_data):
    result = create_object(valid_input_data)
    assert len(result) == 2
    assert isinstance(result[0], Category)
    assert isinstance(result[1], Category)
    assert len(result[0].products) == 2
    assert len(result[1].products) == 2
    assert isinstance(result[0].products[0], Product)
    assert isinstance(result[1].products[1], Product)
    assert result[0].name == "Электроника"
    assert result[0].products[0].name == "Смартфон"
    assert result[0].products[0].price == 999.99


def test_create_object_empty_input():
    result = create_object([])
    assert result == []


def test_create_object_invalid_data(invalid_input_data):
    result = create_object(invalid_input_data)
    assert result == []


def test_create_object_missing_products():
    invalid_data = [{"name": "Категория", "description": "Описание"}]
    result = create_object(invalid_data)
    assert result == []


def test_create_object_partly_valid(valid_input_data):
    corrupted_data = valid_input_data + [{"name": "test", "products": [{"invalid": "data"}]}]
    result = create_object(corrupted_data)
    assert result == []
