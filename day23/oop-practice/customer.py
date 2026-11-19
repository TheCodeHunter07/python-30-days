

from cart import Cart

class Customer:

    def __init__(self, name):
        self.name = name
        self.cart = Cart()

customer1 = Customer("Sumit")
customer2 = Customer("Rahul")

print(customer1.name)
print(customer1.cart.items)

print(customer2.name)
print(customer2.cart.items)