"""
The composite design pattern allows us to create tree structures that contain single objects and collections of objects
the same way, i.e., using the same API.

The composite design pattern is a structural pattern that allows you to compose objects into tree structures to
represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly.

Key Points:
1 - Hierarchical Tree Structure: The pattern is useful for creating a structure where individual objects (leaves) and
    groups of objects (composites) are treated the same way.
2 - Uniform Interface: Both individual objects and composites implement a common interface, allowing clients to interact
    with them in a uniform manner.
3 - Recursive Composition: Composites can contain other composites or individual objects, enabling the creation of
    complex structures from simple components.

https://refactoring.guru/design-patterns/composite
"""

from abc import abstractmethod
from typing import Protocol


class Node(Protocol):

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class Leaf(Node):

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class Branch(Node):

    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, child: Node):
        self.children.append(child)

    def __str__(self):
        output = [self.name]
        output.extend(["*" + str(child).replace("\n", "\n*") for child in self.children])
        return "\n".join(output)


if __name__ == "__main__":
    leaf1 = Leaf("One")
    leaf2 = Leaf("Two")
    print("Printing a leaf:")
    print(leaf1, end="\n\n")

    branch1 = Branch("Branch_1")
    branch1.add(leaf1)
    branch1.add(leaf2)
    print("Printing a branch:")
    print(branch1, end="\n\n")

    leaf3 = Leaf("Three")
    leaf4 = Leaf("Four")
    branch2 = Branch("Branch_2")
    branch2.add(leaf3)
    branch2.add(leaf4)
    branch_master = Branch("Master")
    branch_master.add(branch1)
    branch_master.add(branch2)
    print("Printing a branch with two other branches:")
    print(branch_master)
