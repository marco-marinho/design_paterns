"""
The state design pattern is used to encapsulate the behavior of state machines.

The state design pattern is a behavioral pattern that allows an object to change its behavior when its internal state
changes. This pattern is particularly useful for implementing state machines and managing state-dependent behavior
without using conditional statements.

Key Points:
1 - State Encapsulation: Encapsulates state-specific behavior within state objects.
2 - Context: The context object manages state transitions and delegates behavior to the current state object.
3 - State Transitions: The pattern allows for dynamic changes in behavior based on the object's state, without using
    large conditional statements.
4 - Flexibility and Maintainability: By encapsulating state-specific behavior in separate classes, the pattern enhances
    flexibility and maintainability of the code.

https://refactoring.guru/design-patterns/state
"""

from functools import wraps
from enum import Enum, auto


def consumer(func):
    @wraps(func)
    def wrapper(*args, **kw):
        gen = func(*args, **kw)
        next(gen)
        return gen

    return wrapper


class State(Enum):
    OFF = auto()
    ON = auto()


class Action(Enum):
    TURN_ON = auto()
    TURN_OFF = auto()


@consumer
def switch_state_machine():
    state = State.OFF
    command = yield
    while True:
        match state, command:
            case State.OFF, Action.TURN_OFF:
                command = yield "System is already offline"
            case State.OFF, Action.TURN_ON:
                state = State.ON
                command = yield "System is now online"
            case State.ON, Action.TURN_OFF:
                state = State.OFF
                command = yield "System is now offline"
            case State.ON, Action.TURN_ON:
                command = yield "System is already online"


if __name__ == '__main__':
    switch = switch_state_machine()
    print(switch.send(Action.TURN_OFF))
    print(switch.send(Action.TURN_ON))
    print(switch.send(Action.TURN_ON))
    print(switch.send(Action.TURN_OFF))
