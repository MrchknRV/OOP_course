import json

from config import BASIC_PATH_JSON
from src.task import Product, Category


def load_json_data(path: str) -> list:
    try:
        with open(path, "r", encoding="UTF-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def create_object(data: list):
    try:
        categories = []
        for category in data:
            products = []
            for product in category["products"]:
                products.append(Product(**product))
            category["products"] = products
            categories.append(Category(**category))
        return categories
    except Exception:
        return []


if __name__ == "__main__":
    data = load_json_data(BASIC_PATH_JSON)
    print(data)
    res = create_object(data)
    print(res)

