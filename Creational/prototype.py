from typing import Protocol, Optional, Self
from abc import abstractmethod

from copy import copy, deepcopy

"""
The prototype pattern uses an instance of a certain object as the template from which other similar objects are built.

The prototype design pattern is a creational pattern that enables the creation of new objects by copying an existing 
object, known as the prototype. This pattern is particularly useful when the cost of creating a new object is expensive 
or complex, and it simplifies the object creation process by cloning a prototype instance.

Key Points:
1 - Cloning Objects: Instead of instantiating new objects directly, a prototype instance is cloned to produce 
   new objects.
2 - Avoiding Subclassing: Reduces the need for creating subclasses for each type of object to be created, since the 
    clone method can create copies of the existing object.
3 - Flexibility and Runtime Object Creation: Enables dynamic creation of objects at runtime, which can be useful when 
    the types of objects to be created are determined dynamically.
    
https://refactoring.guru/design-patterns/prototype

For this example lets use a circular singly linked list.
"""


class ListNode:

    def __init__(self, value: int, next_node: Optional[Self] = None):
        self.value = value
        self.next = next_node

    def __deepcopy__(self, memodict: Optional[dict] = None):
        if memodict is None:
            memodict = {}
        new = self.__class__(self.value)
        memodict[id(self)] = new
        new.next = deepcopy(self.next, memodict)
        return new


"""
Lets imagine that a circular singly linked list with three elements is often needed somewhere in our code, instead of
creating this list every time we need it, we can keep a prototype of it and copy whenever it is needed.
"""


class DefaultListFactory:

    def __init__(self):
        first = ListNode(1)
        second = ListNode(2)
        first.next = second
        third = ListNode(3)
        second.next = third
        third.next = first
        self.first = first

    def create(self):
        return deepcopy(self.first)


if __name__ == "__main__":
    list_factory = DefaultListFactory()
    curr_node_1 = list_factory.create()
    curr_node_2 = list_factory.create()
    for _ in range(3):
        print(f"Values are equal {curr_node_1.value} -> {curr_node_2.value}")
        print(f"IDs are not {id(curr_node_1)} -> {id(curr_node_2)} \n")
        curr_node_1 = curr_node_1.next
        curr_node_2 = curr_node_2.next
