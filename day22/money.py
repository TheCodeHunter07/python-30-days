# ASSIGNMENT
# 2 money.py — a Money class that supports + and ==

class Money:

    def __init__(self,amount):
        self.amount = amount

    def __add__(self, other):

     return Money(self.amount + other.amount )

    def __eq__(self, other):

        return self.amount == other.amount

money1 = Money(500)
money2 = Money(300)
money3 = Money(500)

total = money1 + money2

print(total.amount)
print(money1 == money3)
print(money1 == money2)