"""
In the chain of responsibility design pattern requests are passed along a chain of handlers. Each handler then decides
how to interact with the request.

The chain of responsibility design pattern is a behavioral pattern that allows multiple objects to handle a request
without coupling the sender to a specific receiver. Instead of handling the request directly, each object in the chain
either processes the request or passes it to the next handler in the chain.

Key Points:
1 - Decoupling: The pattern decouples the sender of a request from its receivers by allowing multiple objects to process
    the request.
2 - Chain of Handlers: Handlers are arranged in a chain, where each handler has the opportunity to handle the request
    or pass it along to the next handler.
3 - Flexibility: The chain can be modified dynamically by adding or removing handlers, making the system flexible and
    extensible.

https://refactoring.guru/design-patterns/chain-of-responsibility
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from copy import copy
from typing import List, Callable


class Data:

    def __init__(self, transformer: DataTransformer, data: List[int]):
        self.transformer = transformer
        self.original_data = data

    @property
    def data(self):
        q = Query(self, copy(self.original_data))
        self.transformer.perform_query(q)
        return q.value


class Query:

    def __init__(self, sender: Data, value: List[int]):
        self.sender = sender
        self.value = value


class DataTransformer:
    def __init__(self):
        self._handlers: List[Callable] = []

    def perform_query(self, query: Query):
        for handler in self._handlers:
            handler(query)

    def register(self, handler: Callable):
        self._handlers.append(handler)

    def unregister(self, handler: Callable):
        self._handlers.remove(handler)


class DataModifier(ABC):

    def __init__(self, handler: DataTransformer, data: Data):
        self.handler = handler
        self.data = data
        self.handler.register(self.handle)

    @abstractmethod
    def handle(self, query: Query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.handler.unregister(self.handle)


class DataDoubler(DataModifier):

    def handle(self, query: Query):
        if query.sender == self.data:
            query.value = [entry * 2 for entry in query.value]


class DataHalver(DataModifier):

    def handle(self, query: Query):
        if query.sender == self.data:
            query.value = [entry // 2 for entry in query.value]


if __name__ == '__main__':
    transformer = DataTransformer()
    acc = Data(transformer, [1, 2, 3, 4, 5])
    gyr = Data(transformer, [2, 4, 6, 8, 10])

    with DataDoubler(transformer, acc):
        print("Doubled acc:", acc.data)

    with DataHalver(transformer, gyr):
        print("Halved gyr:", gyr.data)

    print("Original acc:", acc.data)
    print("Original gyr:", gyr.data)
