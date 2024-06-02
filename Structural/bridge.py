"""
The bridge design pattern allows us to avoid complexity explosion by splitting a complex implementation in two interface
hierarchies and using composition to achieve the desired behavior.

The bridge design pattern is a structural pattern that separates an object's abstraction from its implementation,
allowing them to vary independently. This pattern is useful for managing complex class hierarchies by decoupling the
interface and implementation classes.

Key Points:
1 - Decoupling: The bridge pattern decouples the abstraction (interface) from the implementation, enabling both to
    evolve independently.
2 - Composition over Inheritance: It favors composition over inheritance, allowing more flexibility in extending and
    modifying implementations.
3 - Independent Variation: Both the abstraction and the implementation can be extended independently without affecting
    each other.

https://refactoring.guru/design-patterns/bridge

In this example, we use a BLE controller and BLE backend abstractions to illustrate how the controller and backend
hierarchies can be split to allow their development to be done independently.
"""

from typing import Protocol, Callable
from abc import abstractmethod
from functools import partial


class BLEController(Protocol):

    @abstractmethod
    def send(self, payload: str):
        raise NotImplementedError


class BLEBackend(Protocol):

    @abstractmethod
    def transmit(self, payload):
        raise NotImplementedError


class StringController(BLEController):

    def __init__(self, backend: BLEBackend):
        self.backend = backend
        self.callbacks = []

    def send(self, payload: str):
        self.backend.transmit(payload + "\n\r")


class BytesController(BLEController):

    def __init__(self, backend: BLEBackend):
        self.backend = backend
        self.callbacks = []

    def send(self, payload: str):
        self.backend.transmit(payload.encode("utf-8"))


class BackendA(BLEBackend):

    def transmit(self, payload):
        print(f"Transmitting {payload} with backend A.")


class BackendB(BLEBackend):

    def transmit(self, payload):
        print(f"Transmitting {payload} with backend B.")


if __name__ == "__main__":
    backenda = BackendA()
    backendb = BackendB()

    str_board = StringController(backenda)
    bytes_board = BytesController(backendb)

    str_board.send("rato")
    bytes_board.send("rato")
