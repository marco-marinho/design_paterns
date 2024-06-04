from abc import abstractmethod
from typing import Protocol

"""
The principle states that a derived subclass should be usable anywhere where the superclass\\interface could be used. 
"""


class HasArea(Protocol):

    @abstractmethod
    def area(self):
        ...


class Square(HasArea):

    def __init__(self, size):
        self.size = size

    def area(self):
        return self.size * self.size


class Circle(HasArea):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * 3.14 * radius


"""
Here Cylinder breaks the area contract by applying extra conditions to the method, throwing an exception that is not 
thrown by the interface. Other violations could include a difference in signature or unexpected side effects.
"""


class Cylinder(HasArea):

    def __init__(self, radius, height):
        self.circle = Circle(radius)
        self.height = height

    def area(self):
        if height <= 0:
            raise ValueError("Height must be greater than zero")
        return self.circle.area() * self.height
