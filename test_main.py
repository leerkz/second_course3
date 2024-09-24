import pytest

from main import Category, Product


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
    assert len(category.products) == 145
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_add_product() -> None:
    category = Category("Electronics", "Various electronic products")
    product = Product("Laptop", "A gaming laptop", 80000, 10)
    category.add_product(product)
    assert len(category.products.split("\n")) == 1


def test_price_setter() -> None:
    product = Product("Laptop",
                      "A gaming laptop",
                      80000,
                      10)
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


if __name__ == "__main__":
    pytest.main()
