# ASSIGNMENT

# Stretch: Group the products by category into a dictionary of lists.

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
products_by_category = {}


for product in products:
    category = product["category"]
    name = product["name"]

    if category not in products_by_category:
        products_by_category[category] = []
        products_by_category[category].append(name)

    else:
        products_by_category[category].append(name)

print(products_by_category)