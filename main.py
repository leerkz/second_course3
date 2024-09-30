class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        return cls(
            name=product_data.get("name", "None"),
            description=product_data.get("description", "None"),
            price=product_data["price"],
            quantity=product_data.get("quantity", 0),
        )

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        return (self.price * self.quantity) + (other.price * other.quantity)


class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list | None = None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.product_count += len(self.__products)
        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        return "\n".join([str(product) for product in self.__products])

    def __str__(self) -> str:
        total_quantity = sum([product.quantity for product in self.__products])
        return f"{self.name}, количество продуктов: {total_quantity} шт."
