from typing import Protocol, List
from abc import abstractmethod

"""
The Dependency Inversion Principle states that a high level module should depend on interfaces as opposed to concrete
implementations. 

Lets have three different implementations of a class that stores odd and even numbers separately. As well as a common 
interface that shall be used latter.
"""


class HasEven(Protocol):

    @property
    @abstractmethod
    def even(self) -> List[int]:
        raise NotImplementedError


class DictStorage(HasEven):

    def __init__(self):
        self.storage = {"odd": [], "even": []}

    def store(self, value: int):
        if value % 2 == 0:
            self.storage["even"].append(value)
        else:
            self.storage["odd"].append(value)

    @property
    def even(self):
        return self.storage["even"]


class ListStorage(HasEven):

    def __init__(self):
        self.storage = [[], []]

    def store(self, value: int):
        if value % 2 == 0:
            self.storage[0].append(value)
        else:
            self.storage[1].append(value)

    @property
    def even(self):
        return self.storage[0]


class AttrStorage(HasEven):

    def __init__(self):
        self.even_storage = []
        self.odd_storage = []

    def store(self, value: int):
        if value % 2 == 0:
            self.even_storage.append(value)
        else:
            self.odd_storage.append(value)

    @property
    def even(self):
        return self.even_storage


"""
Now, lets make two functions that sums up the even elements. One relying on a specific implementation detail and another
relying on the protocol.
"""


def sum_even_bad(storage: DictStorage):
    # This functions relies on the implementation details of DictStorage. It is not possible here to replace it with
    # any of the other two implementations.
    return sum(storage.storage["even"])


def sum_even(storage: HasEven):
    # This function will work for any of the implementations and any possible future implementation that implements the
    # specified interface.
    return sum(storage.even)
