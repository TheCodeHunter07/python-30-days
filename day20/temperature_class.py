# ASSIGNMENT
# 2 temperature_class.py — use @property to block values below absolute zero

class Temperature:

    def __init__(self,temperature):
        self.celsius = temperature

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self,value):
        if value >= -273.15:
            self._celsius = value
        else:
            raise ValueError("Temperature cannot be below absolute zero!")

temp = Temperature(25)

print(temp.celsius)

temp.celsius = 100
print(temp.celsius)

try:
    temp.celsius = -300
except ValueError as e:
    print(e)

print(temp.celsius)