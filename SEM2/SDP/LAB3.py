#factory pattern

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")
class Square(Shape):
    def draw(self):
        print("Drawing Square")

class ShapeFactory:

    def get_shape(self, shape_type):
        if shape_type.lower() == "circle":
            return Circle()
        elif shape_type.lower() == "rectangle":
            return Rectangle()
        elif shape_type.lower() == "square":
            return Square()
        else:
            return None

if __name__ == "__main__":
    factory = ShapeFactory()

    shape1 = factory.get_shape("circle")
    shape1.draw()

    shape2 = factory.get_shape("rectangle")
    shape2.draw()

    shape3 = factory.get_shape("square")
    shape3.draw()


#abstract pattern
from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsButton(Button):
    def paint(self):
        print("Rendering Windows Button")

class WindowsCheckbox(Checkbox):
    def paint(self):
        print("Rendering Windows Checkbox")

class MacButton(Button):
    def paint(self):
        print("Rendering Mac Button")

class MacCheckbox(Checkbox):
    def paint(self):
        print("Rendering Mac Checkbox")

class GUIFactory(ABC):

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class WindowsFactory(GUIFactory):

    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory(GUIFactory):

    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()
    
if __name__ == "__main__":

    factory = WindowsFactory()   # Change to MacFactory()

    button = factory.create_button()
    checkbox = factory.create_checkbox()

    button.paint()
    checkbox.paint()
