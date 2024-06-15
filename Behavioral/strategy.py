"""
The strategy design pattern is a behavioral pattern that defines a family of algorithms, encapsulates each one, and
makes them interchangeable. This pattern allows the algorithm to vary independently from clients that use it.

Key Points:
1 - Encapsulation of Algorithms: Encapsulates different algorithms (strategies) in separate classes.
2 - Interchangeability: Strategies can be swapped out dynamically at runtime.
3 - Context: A context object uses a strategy to execute the algorithm, allowing it to change behavior by changing
    its strategy.
4 - Elimination of Conditional Statements: Promotes cleaner code by removing the need for multiple conditional
    statements to select an algorithm.

https://refactoring.guru/design-patterns/strategy
"""


def filter_odd(data: list):
    return [element for element in data if element % 2 == 0]


def filter_even(data: list):
    return [element for element in data if element % 2 != 0]


class DataFilter:

    def __init__(self):
        self.strategy = filter_odd

    def filter(self, data):
        return self.strategy(data)


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    filter = DataFilter()
    filter.strategy = filter_odd
    print(filter.filter(data))
    filter.strategy = filter_even
    print(filter.filter(data))
