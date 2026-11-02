# ASSIGNMENT
# 1 products.py — a list of 8 product dictionaries (name, price, category, stock): print them as a table, filter by
# category, sort by price, list out-of-stock items, and calculate total inventory value


products = [
    {
        "name": "Laptop",
        "price": 55000,
        "category": "Electronics",
        "stock": 10
    },
    {
        "name": "Mouse",
        "price": 500,
        "category": "Electronics",
        "stock": 25
    },
    {
        "name": "Chair",
        "price": 3000,
        "category": "Furniture",
        "stock": 5
    },
    {
        "name": "Keyboard",
        "price": 1500,
        "category": "Electronics",
        "stock": 0
    },
    {
        "name": "Desk",
        "price": 7500,
        "category": "Furniture",
        "stock": 8
    },
    {
        "name": "Notebook",
        "price": 80,
        "category": "Stationery",
        "stock": 50
    },
    {
        "name": "Pen",
        "price": 20,
        "category": "Stationery",
        "stock": 0
    },
    {
        "name": "Monitor",
        "price": 12000,
        "category": "Electronics",
        "stock": 12
    }
]



# Task 1: Print a header containing the four column names.

print(f"{'Product':<15} {'Price':>10} {'Category':<18} {'Stock':>8}")

# Task 2: Print a separator line beneath the header.

print("-" * 55)

# Task 3: Loop through the products and print each product's information in aligned columns.

for product in products:

    print(f"{product['name']:<15} {product['price']:>10} {product['category']:<18} {product['stock']:>8}")


# filtering products by category.

print("\nElectronics Products")
print("-" * 55)

for product in products:
    if product["category"] == "Electronics":
        print(f"{product['name']:<15} {product['price']:>10} {product['category']:<18} {product['stock']:>8}")


print("\nFurniture Products")
print("-" * 55)

for product in products:
    if product["category"] == "Furniture":
        print(f"{product['name']:<15} {product['price']:>10} {product['category']:<18} {product['stock']:>8}")

print("\nStationery Products")
print("-" * 55)

for product in products:
    if product["category"] == "Stationery":
        print(f"{product['name']:<15} {product['price']:>10} {product['category']:<18} {product['stock']:>8}")


# sort products by price

print("\nProducts Sorted by Price")
print("-" * 55)

sorted_products = sorted(products,key=lambda product:product["price"] )


for product in sorted_products:
    print(
        f"{product['name']:<15} "
        f"{product['price']:>10} "
        f"{product['category']:<18} "
        f"{product['stock']:>8}"
    )

# Out-of-Stock Products

print("\nOut-of-Stock Products")
print("-" * 55)

for product in products:
    if product["stock"] == 0:
         print(
                f"{product['name']:<15} "
                f"{product['price']:>10} "
                f"{product['category']:<18} "
                f"{product['stock']:>8}"
            )


# Calculate the total inventory value.

print("\nInventory Value")
print("-" * 55)

total_value = 0

for product in products:
    inventory_value = product["price"] * product["stock"]
    total_value += inventory_value

    print(f"{product['name']:<15} ₹{inventory_value:>10,}")

print("-" * 55)
print(f"{'Total Inventory Value:':<27} ₹{total_value:,}")