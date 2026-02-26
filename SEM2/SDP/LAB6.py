print("Responsibility Pattern")

from abc import ABC, abstractmethod


# Base Handler
class SupportLevel(ABC):

    def __init__(self):
        self.next_level = None

    def set_next(self, next_handler):
        self.next_level = next_handler

    @abstractmethod
    def handle_request(self, problem_level):
        pass


# Level 1 Support
class Level1Support(SupportLevel):

    def handle_request(self, problem_level):
        if problem_level == 1:
            print("Level 1 Support: Problem solved")
        elif self.next_level:
            self.next_level.handle_request(problem_level)


# Level 2 Support
class Level2Support(SupportLevel):

    def handle_request(self, problem_level):
        if problem_level == 2:
            print("Level 2 Support: Problem solved")
        elif self.next_level:
            self.next_level.handle_request(problem_level)


# Level 3 Support
class Level3Support(SupportLevel):

    def handle_request(self, problem_level):
        if problem_level == 3:
            print("Level 3 Support: Problem solved")
        else:
            print("Problem cannot be solved")


# Main Program
level1 = Level1Support()
level2 = Level2Support()
level3 = Level3Support()

level1.set_next(level2)
level2.set_next(level3)

level1.handle_request(1)
level1.handle_request(2)
level1.handle_request(3)

print("Mediator Pattern")

from abc import ABC, abstractmethod


# Mediator
class ChatRoom:

    def show_message(self, user, message):
        print(user.name + " says: " + message)


# Colleague
class User:

    def __init__(self, name, chat_room):
        self.name = name
        self.chat_room = chat_room

    def send_message(self, message):
        self.chat_room.show_message(self, message)


# Main Program
chat_room = ChatRoom()

user1 = User("Rahul", chat_room)
user2 = User("Sneha", chat_room)

user1.send_message("Hello!")
user2.send_message("Hi Rahul!")
