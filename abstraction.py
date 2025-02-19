from abc import ABC, abstractmethod
"""
abstract classes mean that the classes inheriting must implement the method
"""
class vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def brake(self):
        pass

class car(vehicle):
    def __init__(self, make):
        self.make = make
    def move(self):
        return f"{self.make} has moved!"
    def brake(self):
        return f"{self.make} -has stopped!"
    def __str__(self):
        return self.make
car1 = car("Toyota")
print(car1)