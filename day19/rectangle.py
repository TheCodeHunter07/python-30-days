# ASSIGNMENT
# 3 rectangle.py — a Rectangle class with area() and perimeter()

class Rectangle():

    def __init__(self,length,width):

        self.length = length
        self.width = width

    def area(self):

        area = self.length * self.width

        return area

    def perimeter(self):

        perimeter = 2 * (self.length + self.width)

        return perimeter


rectangle1 = Rectangle(25,10)

print(rectangle1.area())
print(rectangle1.perimeter())