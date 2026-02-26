from abc import ABC, abstractmethod


# Visitor Interface
class Visitor(ABC):

    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass


# Concrete Visitor
class AreaCalculator(Visitor):

    def visit_circle(self, circle):
        area = 3.14 * circle.radius * circle.radius
        print("Circle Area:", area)

    def visit_rectangle(self, rectangle):
        area = rectangle.length * rectangle.width
        print("Rectangle Area:", area)


# Element Interface
class Shape(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass


# Concrete Elements
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.visit_circle(self)


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def accept(self, visitor):
        visitor.visit_rectangle(self)


# Main Program
circle = Circle(5)
rectangle = Rectangle(4, 6)

area_calculator = AreaCalculator()

circle.accept(area_calculator)
rectangle.accept(area_calculator)