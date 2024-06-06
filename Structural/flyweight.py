"""
The flyweight design pattern offloads data to data structures outside the object. This way, the same data can be reused
across multiple flyweights.

The flyweight design pattern is a structural pattern that aims to minimize memory usage and improve performance by
sharing as much data as possible with similar objects. This pattern is particularly useful when dealing with a large
number of objects that have some shared state.

Key Points:
1 - Shared State: Flyweight objects share common state to reduce memory footprint. Only the intrinsic (shared) state is
    stored in the flyweight; the extrinsic (unique) state is passed in from outside.
2 - Factory for Flyweights: A factory is often used to manage and reuse flyweight objects. It ensures that shared
    objects are used whenever possible.
3 - Reduced Memory Usage: By sharing common data, the flyweight pattern helps in reducing the overall memory
    consumption, especially in applications that handle many similar objects.

https://refactoring.guru/design-patterns/flyweight
"""

import time
from random import randint


class ComplexThing:

    def __init__(self, args):
        time.sleep(2)
        self.args = args

    def get(self):
        return self.args


class Flyweight:

    def __init__(self, args, complex_thing):
        self.args = args
        self.complex_thing = complex_thing

    def get(self):
        return self.args, self.complex_thing.get()


class FlyweightFactory:

    def __init__(self):
        self._complex_storage = {}

    def get_flyweight(self, unique_state, shared_state):
        if shared_state not in self._complex_storage:
            self._complex_storage[shared_state] = ComplexThing(shared_state)

        return Flyweight(unique_state, self._complex_storage[shared_state])


if __name__ == '__main__':
    states = [randint(1, 10) for _ in range(100)]
    factory = FlyweightFactory()
    for idx, state in enumerate(states):
        flyweight = factory.get_flyweight(idx, state)
        print(flyweight.get())
