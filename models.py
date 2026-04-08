from abc import ABC, abstractmethod

# Abstract Class
class BaseUser(ABC):
    @abstractmethod
    def display(self):
        pass


class User(BaseUser):
    def __init__(self, name):
        self.__name = name   # encapsulation

    def get_name(self):
        return self.__name

    def display(self):
        print(f"User: {self.__name}")


class Expense(User):  # Inheritance
    def __init__(self, name, amount, category):
        super().__init__(name)   # super usage
        self.amount = amount
        self.category = category

    # Method overriding
    def display(self):
        print(f"{self.get_name()} spent {self.amount} on {self.category}")