"""
A command is an object that contains all the necessary information so that an action can be taken.

The command design pattern is a behavioral pattern that encapsulates a request as an object, thereby allowing for
parameterization of clients with different requests, queuing of requests, and logging of the requests. It also provides
support for undoable operations.

Key Points:
1 - Encapsulation: Encapsulates a request as an object, which contains all the information about the request, such as
    the action to be performed and its parameters.
2 - Decoupling: Decouples the sender (invoker) of a request from its receiver by using command objects.
3 - Support for Undo/Redo: Facilitates the implementation of undoable operations by storing the state required to undo
    the command.
4 - Queuing and Logging: Allows for queuing and logging of requests, providing greater flexibility in handling requests.

https://refactoring.guru/design-patterns/command
"""

from abc import ABC, abstractmethod


class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        self.balance += amount
        return True

    def __str__(self):
        return f'BankAccount balance: {self.balance}'


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class SimpleCommand:
    def __init__(self, account: BankAccount, value: float):
        self.success = False
        self.account = account
        self.value = value


class WithdrawCommand(SimpleCommand, Command):

    def execute(self):
        self.success = self.account.withdraw(self.value)
        return self.success

    def undo(self):
        if self.success:
            self.account.deposit(self.value)


class DepositCommand(SimpleCommand, Command):
    def execute(self):
        self.success = self.account.deposit(self.value)
        return self.success

    def undo(self):
        if self.success:
            self.account.withdraw(self.value)


class CompositeCommand(list, Command):

    def __init__(self, commands=None):
        super(list).__init__()
        if commands is not None:
            self.extend(commands)

    def execute(self):
        success = True
        for idx, command in enumerate(self):
            if success:
                success = command.execute()

    def undo(self):
        for command in self[::-1]:
            if command.success:
                command.undo()


if __name__ == '__main__':
    acc = BankAccount(0)

    deposit = DepositCommand(acc, 1000)
    deposit.execute()
    print(acc)
    deposit.undo()
    print(acc, "\n")

    withdraw = WithdrawCommand(acc, 100)
    withdraw.execute()
    print(acc)
    withdraw.undo()
    print(acc, "\n")

    composite_1 = CompositeCommand([deposit, withdraw])
    composite_1.execute()
    print(acc)
    composite_1.undo()
    print(acc, "\n")

    composite_2 = CompositeCommand([withdraw, deposit])
    composite_2.execute()
    print(acc)
    composite_2.undo()
    print(acc)
