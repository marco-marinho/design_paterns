"""
The decorator design pattern makes it possible to add functionality to an existing class without offending the
open-closed principle.

The decorator design pattern is a structural pattern that allows you to dynamically add behaviors and responsibilities
to objects without modifying their code. This pattern uses composition instead of inheritance to extend functionality.

Key Points:
1 - Dynamic Behavior Addition: Allows for adding new functionalities to objects dynamically and transparently.
2 - Wrapper Classes: Involves creating wrapper classes that "decorate" the original object by adding new behaviors
    before or after delegating tasks to the original object.
3 - Single Responsibility Principle: Promotes the Single Responsibility Principle by allowing functionality to be
    divided between classes with unique areas of concern.

https://refactoring.guru/design-patterns/decorator
"""

from abc import abstractmethod
from typing import Protocol


class IReadWrite(Protocol):

    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def write(self, data: str):
        raise NotImplementedError


class SimpleWriter(IReadWrite):
    def read(self):
        return "some data"

    def write(self, data):
        print(f"Writing data: {data}")


class ReadWriteDecorator(IReadWrite):

    def __init__(self, read_writer: IReadWrite):
        self.read_writer = read_writer

    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def write(self, data: str):
        raise NotImplementedError


class CompressionDecorator(ReadWriteDecorator):

    def read(self):
        return f"Compressed: {self.read_writer.read()}"

    def write(self, data: str):
        print(f"Compressed: {data}, before writing")
        return self.read_writer.write(data)


class EncryptionDecorator(ReadWriteDecorator):

    def read(self):
        return f"Encrypted: {self.read_writer.read()}"

    def write(self, data: str):
        print(f"Encrypted: {data}, before writing")
        return self.read_writer.write(data)


if __name__ == "__main__":
    simple_writer = SimpleWriter()
    comp_writer = CompressionDecorator(simple_writer)
    enc_writer = EncryptionDecorator(simple_writer)

    print(comp_writer.read())
    comp_writer.write("Hello")

    print("\n")

    print(enc_writer.read())
    enc_writer.write("Hello")

    print("\n")

    chain_writer = EncryptionDecorator(comp_writer)
    print(chain_writer.read())
    chain_writer.write("Hello")
