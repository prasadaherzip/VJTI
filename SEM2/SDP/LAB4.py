#singleton pattern
print("Singleton Pattern\n")

class Database:

    single_object = None   # stores only one object

    def __new__(cls):
        if cls.single_object is None:
            print("Creating database object...")
            cls.single_object = super(Database, cls).__new__(cls)
        return cls.single_object

    def show_message(self):
        print("Database connected successfully")


# Main program
db1 = Database()
db1.show_message()

db2 = Database()

if db1 is db2:
    print("Both variables point to the same object (Singleton works)\n")


#composite pattern
print("Composite Pattern")
from abc import ABC, abstractmethod


# Common base class
class Person(ABC):

    @abstractmethod
    def show_details(self):
        pass


# Leaf class (single employee)
class Worker(Person):

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def show_details(self):
        print(self.name + " - " + self.job)


# Composite class (manager with workers)
class TeamLeader(Person):

    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.team_members = []

    def add_member(self, member):
        self.team_members.append(member)

    def remove_member(self, member):
        self.team_members.remove(member)

    def show_details(self):
        print("\nTeam Leader:", self.name, "-", self.department)
        for member in self.team_members:
            member.show_details()


# Main program
worker1 = Worker("Rahul", "Frontend Developer")
worker2 = Worker("Sneha", "Backend Developer")

leader = TeamLeader("Amit", "IT Department")

leader.add_member(worker1)
leader.add_member(worker2)

leader.show_details()