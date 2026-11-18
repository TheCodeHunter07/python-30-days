# ASSIGNMENT
# 4 Rewrite Rectangle as a @dataclass

from dataclasses import dataclass

@dataclass
class Rectangle:
    length: float
    width: float

    def area(self):
       return self.length * self.width



    def perimeter(self):

        return 2 * (self.length + self.width)


rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(10, 5)

print(rectangle1)
print(rectangle1.area())
print(rectangle1.perimeter())
print(rectangle1 == rectangle2)