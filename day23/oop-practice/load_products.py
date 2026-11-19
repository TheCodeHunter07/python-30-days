import json
from product import Product

# Open JSON file
with open("products.json", "r") as file:
    product_data = json.load(file)

# Convert dictionaries into Product objects
products = []

for data in product_data:
    product = Product.from_dict(data)
    products.append(product)

# Display loaded products
for product in products:
    print(product.display_info())