


from product import Product

class Cart:

    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):

        found = False

        for item in self.items:

            if item["product"] == product:

                found = True

                total_quantity = item["quantity"] + quantity

                if product.is_available(total_quantity):
                    item["quantity"] = total_quantity
                    print("Product quantity updated.")
                else:
                    print("Not enough stock available.")

                break

        if found == False:

            if product.is_available(quantity):

                self.items.append({
                    "product": product,
                    "quantity": quantity
                })

                print("Product added to cart.")

            else:
                print("Not enough stock available.")

    def remove_product(self, product):

        found = False

        for item in self.items:

            if item["product"] == product:

                found = True

                self.items.remove(item)

                break

        if found:
            print("Product Removed from cart.")

        else:
            print("Product noy found!")

    def calculate_total(self):

        total = 0

        for item in self.items:

           total_cost = item["product"].price * item["quantity"]

           total += total_cost

        return total


            

        

laptop = Product("Laptop", 50000, 5)
mouse = Product("Mouse", 500, 10)

cart = Cart()

# Add products
cart.add_product(laptop, 2)
cart.add_product(mouse, 3)

# Add an existing product again
cart.add_product(laptop, 1)

# Display cart total
print("Cart Total:", cart.calculate_total())

# Remove a product
cart.remove_product(mouse)

# Display updated total
print("Updated Cart Total:", cart.calculate_total())