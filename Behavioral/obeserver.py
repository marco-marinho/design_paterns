"""
In the observer design pattern, objects can subscribe to be notified of certain events. This is mostly done with
callbacks.

The observer design pattern is a behavioral pattern that defines a one-to-many dependency between objects so that when
one object changes state, all its dependents are notified and updated automatically. This pattern is particularly useful
for implementing distributed event-handling systems.

Key Points:
1 - One-to-Many Dependency: Allows one object (the subject) to notify multiple dependent objects (observers) about state
    changes.
2 - Decoupling: The subject and observers are loosely coupled; the subject doesn't need to know details about the
    observers.
3 - Automatic Updates: Observers are automatically notified and updated when the subject's state changes.
4 - Event Handling: Commonly used for implementing event-driven systems and ensuring that changes in state are
    propagated to interested parties.

https://refactoring.guru/design-patterns/observer
"""

from typing import Callable


class Observer:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber: Callable):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber: Callable):
        self.subscribers.remove(subscriber)

    def emit(self, *args, **kwargs):
        for subscriber in self.subscribers:
            subscriber(*args, **kwargs)


class DataReceiver:

    def __init__(self):
        self.data_signal = Observer()

    def receive(self, data: bytes):
        self.data_signal.emit(data)


if __name__ == "__main__":
    receiver = DataReceiver()
    receiver.data_signal.subscribe(print)
    for i in range(10):
        receiver.receive(bytes(i))
