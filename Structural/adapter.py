"""
The adapter pattern is used when a certain class needs to conform to an API different from its own. To avoid rewriting
the class, an adapter can be implemented to provide a conformant API for the class.

The adapter design pattern is a structural pattern used to enable objects with incompatible interfaces to work together.
It acts as a bridge between two incompatible interfaces, allowing classes to collaborate without changing their existing
code.

Key Points:
1 - Interface Compatibility: The adapter makes two incompatible interfaces compatible, allowing classes that otherwise
    couldn't work together to interact seamlessly.
2 - Wrapper Class: The adapter pattern typically involves creating a wrapper class that translates the interface of one
    class into an interface that another class expects.
3 - Reuse and Flexibility: This pattern promotes reuse of existing functionality and increases flexibility by allowing
    new and legacy code to work together.

https://refactoring.guru/design-patterns/adapter

In this example, let's assume we have two different classes that represent IMUs from different vendors, with different
APIs.
"""

from typing import Protocol
from random import randint, random
from math import sqrt
from abc import abstractmethod


class LSBImu(Protocol):

    @abstractmethod
    def read_acc(self) -> list[int]:
        raise NotImplementedError


class IMUAlpha(LSBImu):

    def read_acc(self):
        return [randint(0, 255), randint(0, 255), randint(0, 255)]


class IMUBeta:

    def read_acc(self):
        return [random() * 9.8 * 20, random() * 9.8 * 20, random() * 9.8 * 20]


class IMUBetaToAlphaAdapter(LSBImu):

    def __init__(self, beta: IMUBeta):
        self.beta = beta

    def read_acc(self):
        return [int((entry / (9.8 * 20)) * 255) for entry in self.beta.read_acc()]


def print_lsb(imu: LSBImu):
    print(" ".join(map(str, imu.read_acc())))


if __name__ == "__main__":
    alpha = IMUAlpha()
    beta = IMUBeta()
    beta_adapter = IMUBetaToAlphaAdapter(beta)
    print_lsb(alpha)
    print_lsb(beta_adapter)
