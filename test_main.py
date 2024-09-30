import pytest

from main import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def product() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product_init(product: Product) -> None:
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


@pytest.fixture
def category() -> Category:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


def test_category_init(category: Category) -> None:
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category.products.split("\n")) == 3
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_add_product() -> None:
    category = Category("Electronics", "Various electronic products")
    product = Product("Laptop", "A gaming laptop", 80000, 10)
    category.add_product(product)
    assert len(category.products.split("\n")) == 1


def test_price_setter() -> None:
    product = Product("Laptop", "A gaming laptop", 80000, 10)
    product.price = 90000
    assert product.price == 90000
    product.price = -1000
    assert product.price == 90000


def test_new_product(product: Product) -> None:
    product_data = {"name": "Laptop", "description": "A gaming laptop", "price": 85000, "quantity": 5}
    product = Product.new_product(product_data)
    assert product.name == "Laptop"
    assert product.price == 85000
    assert product.quantity == 5


def test_product_str() -> None:
    product = Product("Laptop", "A gaming laptop", 80000, 10)
    assert str(product) == "Laptop, 80000 руб. Остаток: 10 шт."


def test_category_str(category: Category) -> None:
    assert str(category) == "Смартфоны, количество продуктов: 27 шт."


def test_product_addition() -> None:
    product1 = Product("Laptop", "A gaming laptop", 80000, 10)
    product2 = Product("Phone", "A smartphone", 20000, 5)
    assert product1 + product2 == 900000


if __name__ == "__main__":
    pytest.main()


def test_smartphone_creation() -> None:
    smartphone = Smartphone("iPhone 15", "Последняя модель", 200000, 10, "Высокая", "15 Pro", "512GB", "Серый")
    assert smartphone.name == "iPhone 15"
    assert smartphone.model == "15 Pro"
    assert smartphone.price == 200000
    assert smartphone.quantity == 10
    assert smartphone.memory == "512GB"
    assert smartphone.color == "Серый"


def test_lawngrass_creation() -> None:
    grass = LawnGrass("Газонная трава", "Лучший выбор для газонов", 1000, 50, "Россия", 7, "Зеленый")
    assert grass.name == "Газонная трава"
    assert grass.price == 1000
    assert grass.quantity == 50
    assert grass.country == "Россия"
    assert grass.germination_period == 7
    assert grass.color == "Зеленый"


def test_product_addition_type_error() -> None:
    smartphone = Smartphone("iPhone 15", "Последняя модель", 200000, 10, "Высокая", "15 Pro", "512GB", "Серый")
    grass = LawnGrass("Газонная трава", "Лучший выбор для газонов", 1000, 50, "Россия", 7, "Зеленый")
    with pytest.raises(TypeError):
        smartphone + grass


def test_add_product_type_error() -> None:
    category = Category("Техника", "Категория для техники")
    invalid_product = "Не продукт"
    with pytest.raises(TypeError):
        category.add_product(invalid_product)  # type: ignore[arg-type]
