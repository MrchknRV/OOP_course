from src.task import Product
from src.product_heirs import Smartphone, LawnGrass


def test_print_mixin(capsys):
    Product(
        name="Samsung Galaxy C23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=6
    )
    captured = capsys.readouterr()
    assert captured.out == "Product(Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 6)\n"

    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    captured = capsys.readouterr()
    assert captured.out == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)\n"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    captured = capsys.readouterr()
    assert captured.out == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)\n"
