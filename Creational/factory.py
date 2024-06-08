from abc import abstractmethod
from typing import Protocol

"""
The factory pattern takes out the responsibility of instantiating a object from the class to a Factory class.

The factory design pattern is a creational pattern used in object-oriented programming to create objects without
specifying the exact class of object that will be created. Instead of calling a constructor directly, a factory method
is used to create and return instances of objects. This pattern promotes loose coupling by decoupling the client code
from the specific classes it needs to instantiate.

Key Points:
1 - Encapsulation of Object Creation: The factory method handles the instantiation of objects,
    centralizing the creation logic.
2 - Flexibility and Extensibility: By using factory methods, it becomes easier to introduce new classes
    without modifying the client code, facilitating the Open/Closed Principle.
3 - Decoupling: The client code interacts with interfaces or abstract classes rather than concrete classes,
    enhancing code maintainability and scalability

The main difference between the Factory and Builder patterns is that the Factory method takes care of wholesale
creation as opposed to piece wise creation in the Builder case.

For this example, imagine two databases containing names of people from possibly different nationalities should be 
merged. For the Gamma database, the first and last names are in order. However, for the Ixi databased, last names come
before first names and should be corrected for when merged. Furthermore, Gamma member are to be assigned IDs starting
at 0, while Ixi members are to be assigned IDs starting at 6000. Instead of having all this logic in the Person class
initializer, we shift the responsibility to Factory classes, which keep track of the issued IDs as well as correct
for the naming scheme when needed.
"""


class Person:
    def __init__(self, id_number: int, first_name: str, last_name: str) -> None:
        self.id = id_number
        self.first_name = first_name
        self.last_name = last_name


class IPersonFactory(Protocol):

    @abstractmethod
    def create_person(self, first_name: str, last_name: str) -> Person:
        raise NotImplementedError


class GammaPersonFactory(IPersonFactory):

    def __init__(self):
        self.curr_id = 0

    def create_person(self, first_name: str, last_name: str) -> Person:
        operson = Person(self.curr_id, first_name, last_name)
        self.curr_id += 1
        return operson


class IxiPersonFactory(IPersonFactory):

    def __init__(self):
        self.curr_id = 6000

    def create_person(self, first_name: str, last_name: str) -> Person:
        operson = Person(self.curr_id, last_name, first_name)
        self.curr_id += 1
        return operson
