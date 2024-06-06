"""
In the proxy pattern, a wrapper object is used to wrap some other object, so that calls to functionalities of the
wrapped object can have some logic executed prior or after it.

The proxy design pattern is a structural pattern that provides a surrogate or placeholder for another object to control
access to it. This pattern is useful for implementing various types of control mechanisms, such as access control, lazy
initialization, logging, and more.

Key Points:
1- Control Access: The proxy controls access to the original object, allowing for additional functionality such as
   access control, caching, logging, or lazy loading.

Types of Proxies:
1 - Virtual Proxy: Delays the creation and initialization of an expensive object until it is needed.
2 - Protection Proxy: Controls access to the original object, often used for security.
3 - Remote Proxy: Provides a local representative for an object that resides in a different address space (e.g., on a
    different machine).
4 - Smart Proxy: Adds additional behavior to the object being proxied, such as reference counting or logging.
5 - Delegation: The proxy typically delegates the requests to the real subject (the object it is representing).

https://refactoring.guru/design-patterns/proxy
"""

from random import randint


class RandomGenerator:

    def random(self):
        return randint(1, 100)


class RandomGeneratorLogger:

    def __init__(self, generator):
        self.generator = generator

    def random(self):
        print("Generating random number")
        res = self.generator.random()
        print(f"Generated {res}")
        return res


class RandomGeneratorLazy:

    def __init__(self):
        self.generator = None

    def random(self):
        if self.generator is None:
            self.generator = RandomGenerator()
        return self.generator.random()
