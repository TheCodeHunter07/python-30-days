# ASSIGNMENT
# 2 bank_account.py — deposit(), withdraw() (block overdrafts) and balance()


class BankAccount:

    def __init__(self,account_holder,balance,):

        self.account_holder = account_holder
        self._balance = balance
        self.transactions = []

    def deposit(self,amount):

       if amount <= 0:
          return "Amount must be greater than zero"

       deposit = self._balance + amount

       self._balance = deposit

       self.transactions.append(f"Deposited: {amount}")

       return deposit

    def withdraw(self,amount):

        if amount <= 0:
           return "Amount must be greater than zero"

        if amount <= self._balance:

            withdraw = self._balance - amount

            self._balance = withdraw

            self.transactions.append(f"Withdrawn: {amount}")

            return withdraw

        else:
            return "Insufficient Balance"

    def balance(self):

        return self._balance

    def transaction_history(self):

        for transaction in self.transactions:
          print(transaction)



    

        






user1 = BankAccount("Sumit", 5000)

print(user1.deposit(1000))
print(user1.withdraw(2000))
print(user1.balance())

print(user1.deposit(-500))
print(user1.withdraw(-100))
print(user1.withdraw(10000))
print(user1.deposit(0))
print(user1.balance())


print("\nTransaction History:")
user1.transaction_history()
