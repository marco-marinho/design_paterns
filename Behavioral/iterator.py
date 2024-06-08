"""
Iterators are mechanisms for traversing data structures.

An iterator is a fundamental concept in programming, particularly in languages like Python. It allows you to traverse
through all the elements of a collection, such as a list, tuple, or dictionary, without needing to know the underlying
structure of the collection.

Key Concepts of Iterators
Iterable: An object that can return an iterator. Examples include lists, tuples, dictionaries, sets, and strings.
Iterator: An object that represents a stream of data; it returns one element at a time. Iterators implement two
          methods: __iter__() and __next__().
          __iter__() returns the iterator object itself.
          __next__() returns the next element from the container. If there are no more items, it raises the
          StopIteration exception.

https://refactoring.guru/design-patterns/iterator
"""


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)


def in_order_traversal(root):
    if root.left is not None:
        for node in in_order_traversal(root.left):
            yield node
    yield root
    if root.right is not None:
        for node in in_order_traversal(root.right):
            yield node


def pre_order_traversal(root):
    yield root
    if root.left is not None:
        for node in pre_order_traversal(root.left):
            yield node
    if root.right is not None:
        for node in pre_order_traversal(root.right):
            yield node


def post_order_traversal(root):
    if root.left is not None:
        for node in pre_order_traversal(root.left):
            yield node
    if root.right is not None:
        for node in pre_order_traversal(root.right):
            yield node
    yield root


if __name__ == '__main__':
    root = Node(1, Node(2), Node(3))
    print([node for node in in_order_traversal(root)])
    print([node for node in pre_order_traversal(root)])
    print([node for node in post_order_traversal(root)])
