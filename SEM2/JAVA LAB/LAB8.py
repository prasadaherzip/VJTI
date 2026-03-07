class Vehicle:
    
    def __init__(self, name):
        self.name = name

    # Method Overloading using default argument
    def start(self, mode=None):
        if mode:
            print(self.name, "starting in", mode, "mode")
        else:
            print(self.name, "starting normally")


# Inheritance
class Car(Vehicle):

    # Method Overriding
    def start(self, mode=None):
        print(self.name, "car engine starting")


class Bike(Vehicle):

    # Method Overriding
    def start(self, mode=None):
        print(self.name, "bike engine starting")


# Creating objects
car1 = Car("Honda")
bike1 = Bike("Yamaha")

# Calling methods
car1.start()
bike1.start()

# Demonstrating method overloading
v = Vehicle("Generic Vehicle")
v.start()
v.start("Eco")