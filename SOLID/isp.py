from abc import abstractmethod
from typing import Protocol

"""
Here the Vehicle interface is too broad. It forces methods on the child which might not always be relevant of make 
sense. For instance, if a Bicycle would inherit from Vehicle, one could consider turn_on and turn_off as getting on 
and off the bike, but one cannot turn the AC on on a bicycle. Therefore, for this purpose, the elements of this 
interface should be split up.
"""


class Vehicle(Protocol):

    @abstractmethod
    def turn_on(self):
        raise NotImplementedError

    @abstractmethod
    def move(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off(self):
        raise NotImplementedError

    @abstractmethod
    def ac_on(self):
        raise NotImplementedError


"""
Here we segregate the individual member of the bloated Vehicle interface into parts that can individually used by
children as needed.
"""


class AC(Protocol):

    @abstractmethod
    def ac_on(self):
        raise NotImplementedError


class Movable(Protocol):

    @abstractmethod
    def move(self):
        raise NotImplementedError


class MotorVehicle(Protocol):

    @abstractmethod
    def start_engine(self):
        raise NotImplementedError

    @abstractmethod
    def stop_engine(self):
        raise NotImplementedError


"""
We can now use the segregated interfaces to construct classes that expose only the relevant and necessary methods.
The complete interface that was originally exposed in Vehicle can be achieved by combining the segregated pieces.
"""


class Bicycle(Movable):

    def move(self):
        pass


class CarWithAC(MotorVehicle, Movable, AC):

    def ac_on(self):
        pass

    def move(self):
        pass

    def start_engine(self):
        pass

    def stop_engine(self):
        pass
