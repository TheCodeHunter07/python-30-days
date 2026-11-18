# ASSIGNMENT
# 1 vehicles.py — Vehicle base class with Car and Bike subclasses overriding describe()

class Vehicle:

    def __init__(self, brand, color):

        self.brand = brand
        self.color = color

    def describe(self):

        print("This is a vehicle")

class Car(Vehicle):

    def describe(self):

        print(f"Brand of car is {self.brand} and Color is {self.color}")


class Bike(Vehicle):
    
    def describe(self):

        print(f"Brand of Bike is {self.brand} and Color is {self.color}")

car1 = Car("Toyota", "Black")
bike1 = Bike("Honda", "Red")

car1.describe()
bike1.describe()