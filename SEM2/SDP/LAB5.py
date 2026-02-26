print("Decorator Pattern")

from abc import ABC, abstractmethod

# Base class
class Coffee(ABC):

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


# Simple Coffee (Original Object)
class SimpleCoffee(Coffee):

    def get_cost(self):
        return 50

    def get_description(self):
        return "Simple Coffee"


# Decorator Base Class
class CoffeeDecorator(Coffee):

    def __init__(self, coffee):
        self.coffee = coffee


# Add Milk
class Milk(CoffeeDecorator):

    def get_cost(self):
        return self.coffee.get_cost() + 20

    def get_description(self):
        return self.coffee.get_description() + " + Milk"


# Add Sugar
class Sugar(CoffeeDecorator):

    def get_cost(self):
        return self.coffee.get_cost() + 10

    def get_description(self):
        return self.coffee.get_description() + " + Sugar"


# Main program
coffee = SimpleCoffee()
coffee = Milk(coffee)
coffee = Sugar(coffee)

print("Order:", coffee.get_description())
print("Total Cost:", coffee.get_cost())

#-----------------------------------------------------
print("Proxy Design Pattern")

from abc import ABC, abstractmethod

# Common interface
class BankAccount(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass


# Real object
class RealBankAccount(BankAccount):

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful. Remaining balance:", self.balance)
        else:
            print("Insufficient balance")


# Proxy class
class BankAccountProxy(BankAccount):

    def __init__(self, balance):
        self.real_account = RealBankAccount(balance)

    def withdraw(self, amount):
        if amount > 10000:
            print("Proxy: Withdrawal limit exceeded (Max 10000)")
        else:
            self.real_account.withdraw(amount)


# Main program
account = BankAccountProxy(20000)

account.withdraw(5000)
account.withdraw(15000)
