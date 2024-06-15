"""
The template method design pattern is a behavioral pattern that defines the skeleton of an algorithm in a method,
deferring some steps to subclasses. It allows subclasses to redefine certain steps of the algorithm without changing
its structure.

Key Points:
1 - Algorithm Structure: The pattern defines the structure of an algorithm in a method called the template method.
2 - Defer Implementation: Subclasses can override specific steps of the algorithm without altering its overall
    structure.
3 - Code Reuse: Promotes code reuse by allowing the common parts of the algorithm to be implemented in a base class
    while variations are implemented in subclasses.
4 - Inversion of Control: The base class controls the overall process, while subclasses provide the specifics.

https://refactoring.guru/design-patterns/template-method
"""

from abc import ABC, abstractmethod
from copy import copy


class Filter(ABC):

    def __init__(self, data: list):
        self.data = copy(data)
        self.filter()

    @abstractmethod
    def filter(self):
        pass

    def __repr__(self):
        return f"Filter with buffer: {self.data}"


class OddFilter(Filter):

    def filter(self):
        self.data = [element for element in self.data if element % 2 != 0]

    def __repr__(self):
        return f"OddFilter with buffer: {self.data}"


class EvenFilter(Filter):

    def filter(self):
        self.data = [element for element in self.data if element % 2 == 0]


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even = EvenFilter(data)
    print(even)
    odd = OddFilter(data)
    print(odd)
