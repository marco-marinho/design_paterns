"""
The singleton pattern is a pattern where only a single instance of an object exists.

The singleton design pattern is a creational pattern that ensures a class has only one instance and provides a global
point of access to that instance. This pattern is used when exactly one object is needed to coordinate actions across
the system.

While singletons can be useful in certain cases, they often introduce several issues that can make code harder to
maintain, test, and scale. Modern design practices generally favor more flexible and testable approaches like
dependency injection.

Key Points:
1 - Single Instance: Ensures that a class has only one instance throughout the application's lifecycle.
2 - Global Access: Provides a global point of access to the instance, making it easy to access from different parts of
    the application.
3 - Controlled Instantiation: Prevents the instantiation of the class by external code, typically by making the
    constructor private.

https://refactoring.guru/design-patterns/singleton

Three different ways of achieving this pattern in python are exemplified.
"""


def singleton(cls):
    _instances = {}

    def get_instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return get_instance


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Monostate(type):
    _shared_state = {}

    def __call__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__call__(*args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


# As an example of a singleton, we show an allocator class that returns memory from a buffer as requested. This is only
# a toy example and not terribly useful or reasonable in most cases.

class Allocator(metaclass=Singleton):

    def __init__(self):
        self.buffer = [0] * 10
        self.ptr = 0

    def allocate(self, size):
        if size + self.ptr >= len(self.buffer):
            raise MemoryError("Out of memory.")
        output = self.buffer[self.ptr: self.ptr + size]
        # Having a thread switch here could lead to some hard to debug behavior.
        self.ptr = self.ptr + size
        return output


if __name__ == '__main__':
    alloc = Allocator()
    buf1 = alloc.allocate(3)

    alloc2 = Allocator()
    buf2 = alloc2.allocate(3)

    print(alloc.buffer == alloc2.buffer)
