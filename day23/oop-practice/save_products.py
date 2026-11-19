import json
from product import Product

# Create products
laptop = Product("Laptop", 50000, 5)
mouse = Product("Mouse", 500, 10)
keyboard = Product("Keyboard", 1000, 8)

# Store products in a list
products = [laptop, mouse, keyboard]

# Convert Product objects into dictionaries
product_data = []

for product in products:
    product_data.append(product.to_dict())

# Save dictionaries into JSON file
with open("products.json", "w") as file:
    json.dump(product_data, file, indent=4)

print("Products saved successfully!")