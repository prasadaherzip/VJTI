from abc import ABC, abstractmethod


# Iterator Interface
class MyIterator(ABC):

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


# Concrete Iterator
class NameIterator(MyIterator):

    def __init__(self, name_list):
        self.name_list = name_list
        self.position = 0

    def has_next(self):
        return self.position < len(self.name_list)

    def next(self):
        if self.has_next():
            name = self.name_list[self.position]
            self.position += 1
            return name
        return None


# Collection Class
class NameCollection:

    def __init__(self):
        self.names = []

    def add_name(self, name):
        self.names.append(name)

    def get_iterator(self):
        return NameIterator(self.names)


# Main Program
collection = NameCollection()

collection.add_name("Rahul")
collection.add_name("Sneha")
collection.add_name("Amit")

iterator = collection.get_iterator()

while iterator.has_next():
    print(iterator.next())