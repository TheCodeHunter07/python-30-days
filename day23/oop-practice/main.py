from product import Product
from customer import Customer
from checkout import Checkout

# Create product
laptop = Product("Laptop", 50000, 5)

# Create two customers
customer1 = Customer("Sumit")
customer2 = Customer("Rahul")

# Create checkout object
checkout = Checkout()

# Customer 1 adds 3 laptops
customer1.cart.add_product(laptop, 3)

# Customer 2 adds 3 laptops
customer2.cart.add_product(laptop, 3)


# Rahul purchases first
print("\nRahul's Checkout:")

checkout.process_checkout(customer2.cart, "SAVE10")

print("Laptop Stock:", laptop.stock)


# Sumit attempts checkout
print("\nSumit's Checkout:")

checkout.process_checkout(customer1.cart, "SAVE20")

print("Laptop Stock:", laptop.stock)
print("Sumit's Cart:", customer1.cart.items)


# Create another customer for discount testing
customer3 = Customer("Amit")

# Add laptop to Amit's cart
customer3.cart.add_product(laptop, 1)

print("\nAmit's Checkout:")

checkout.process_checkout(customer3.cart, "SAVE20")

print("Laptop Stock:", laptop.stock)