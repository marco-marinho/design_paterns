"""
A memento is an object that stores a state of operation and can be used to roll back or forward states of the system.

The memento design pattern is a behavioral pattern that allows an object to capture and save its current state so it
can be restored later without violating encapsulation. This pattern is particularly useful for implementing undo
mechanisms.

Key Points:
1 - State Capture: The pattern captures the internal state of an object without exposing its internal structure.
2 - Encapsulation: Ensures that the object's encapsulation is maintained, as the memento only exposes the necessary
    state to the originator.
3 - Restore Capability: Provides a mechanism to restore the object's state to a previous state using the memento.

https://refactoring.guru/design-patterns/memento
"""
from dataclasses import dataclass
from copy import copy


@dataclass
class State:
    r1: int
    r2: int


class Computer:

    def __init__(self):
        self.state = State(0, 0)
        self.memento = [copy(self.state)]
        self.idx = 0

    @property
    def r1(self):
        return self.state.r1

    @r1.setter
    def r1(self, r1):
        self.state.r1 = r1
        self.memento.append(copy(self.state))
        self.idx += 1

    @property
    def r2(self):
        return self.state.r2

    @r2.setter
    def r2(self, r2):
        self.state.r2 = r2
        self.memento.append(copy(self.state))
        self.idx += 1

    def undo(self):
        if self.idx >= 1:
            self.state = self.memento[self.idx - 1]
            self.idx -= 1

    def redo(self):
        if self.idx < len(self.memento) - 1:
            self.state = self.memento[self.idx + 1]
            self.idx += 1

    def __str__(self):
        return f"Computer: r1: {self.state.r1}, r2: {self.state.r2}"


if __name__ == "__main__":
    computer = Computer()
    computer.r1 = 1
    print(computer)
    computer.undo()
    print(computer)
    computer.redo()
    print(computer)
