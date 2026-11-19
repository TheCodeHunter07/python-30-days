class Checkout:

    def process_checkout(self, cart, discount_code=None):

        # Phase 1: Check product availability

        for item in cart.items:

            product = item["product"]
            quantity = item["quantity"]

            if product.is_available(quantity):
                print(product.name, "is available")

            else:
                print(product.name, "is out of stock")
                print("Checkout failed!")
                return

        # Phase 2: Calculate total amount

        total = cart.calculate_total()

        # Phase 3: Apply discount

        final_amount = self.apply_discount(total, discount_code)

        # Phase 4: Reduce product stock

        for item in cart.items:

            product = item["product"]
            quantity = item["quantity"]

            product.stock -= quantity

        # Phase 5: Clear cart after successful checkout

        cart.items.clear()

        # Phase 6: Display final bill

        print("\nCheckout successful!")
        print("Original Amount:", total)
        print("Discount Code:", discount_code)
        print("Final Amount:", final_amount)

    # Discount calculation method

    def apply_discount(self, total, discount_code):

        if discount_code == "SAVE10":

            discount = total * 0.10

        elif discount_code == "SAVE20":

            discount = total * 0.20

        else:

            discount = 0

        final_amount = total - discount

        return final_amount