class Product:
    total_of_products = 0
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price
        Product.total_of_products += 1

my_product01 = Product("Water", 3)
my_product02 = Product("Pizza", 19.90)
my_product03 = Product("Mosue", 59.90)
my_product04 = Product("Keyboard", 100)
my_product05 = Product("Laptop", 1199.90)
my_product06 = Product("Tablet", 499.90)
my_product07 = Product("PS5", 499.90)

print(f"The total of products is {Product.total_of_products}")