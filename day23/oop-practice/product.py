# ASSIGNMENT
# 1 Build a mini online shop: Product (name, price, stock), Cart (add, remove, total), Customer (owns a cart), and
# # a checkout that reduces stock and blocks out-of-stock purchases


class Product:

    def __init__(self,name, price, stock):

        self.name = name
        self.price = price
        self.stock = stock

    def display_info(self):

        return f"Product: {self.name} , Price: {self.price} , Stock: {self.stock}"

    def is_available(self,quantity):

        if quantity <= self.stock:
            return True
        else:
            return False

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["price"],
            data["stock"]
            )

laptop = Product("Laptop", 50000, 5)

print(laptop.display_info())

print(laptop.is_available(3))  # True
print(laptop.is_available(7))  # False

print(laptop.to_dict())

product_data = {
    "name": "Laptop",
    "price": 50000,
    "stock": 5
}

laptop = Product.from_dict(product_data)

print(laptop.display_info())