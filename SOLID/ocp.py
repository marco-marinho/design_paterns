"""
Open closed principle.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import IntEnum, auto


class Manufacturer(IntEnum):
    ST = auto()
    NORDIC = auto()
    TI = auto()


class Microcontroller(IntEnum):
    ARM = auto()
    RISCV = auto()
    PIC = auto()


@dataclass
class System:
    name: str
    manufacturer: Manufacturer
    microcontroller: Microcontroller


# This is illustrated here as a class, but it could also be a module or a function
class FilterManager:
    @staticmethod
    def filter_by_manufacturer(manufacturer: Manufacturer, items):
        for item in items:
            if item.manufacturar == manufacturer:
                yield item

    # Adding other filters would result in changing the class, the closed part of the closed principle states that
    # a class, function or similar should be closed to changes. We then need to set up ways so that filters can be
    # added or modified without changing the filtering implementation itself.


# Here SystemFilter is the base class from which all other filters are derived. This allows filters to be created
# without any changes to the base class or the functions which might use it. I also allows us to create composition
# between different filters.

class SystemFilter(ABC):
    @abstractmethod
    def filter(self, item: System):
        ...

    def __and__(self, other):
        return AndFilter([self, other])

    def __or__(self, other):
        return OrFilter([self, other])


class AndFilter(SystemFilter):

    def __init__(self, filters: list[SystemFilter]):
        self.filters = filters

    def filter(self, item: System):
        return all(map(lambda filt: filt.filter(item), self.filters))


class OrFilter(SystemFilter):

    def __init__(self, filters: list[SystemFilter]):
        self.filters = filters

    def filter(self, item: System):
        return any(map(lambda filt: filt.filter(item), self.filters))


class ManufacturerFilter(SystemFilter):

    def __init__(self, manufacturer: Manufacturer):
        self.manufacturer = manufacturer

    def filter(self, item: System):
        return self.manufacturer == item.manufacturer


class MicrocontrollerFilter(SystemFilter):

    def __init__(self, microcontroller: Microcontroller):
        self.microcontroller = microcontroller

    def filter(self, item: System):
        return self.microcontroller == item.microcontroller


if __name__ == "__main__":
    f411 = System("F411", Manufacturer.ST, Microcontroller.ARM)
    n53 = System("N53", Manufacturer.NORDIC, Microcontroller.RISCV)
    n52 = System("N52", Manufacturer.NORDIC, Microcontroller.ARM)

    items = [f411, n52, n53]

    riscv_filter = MicrocontrollerFilter(Microcontroller.RISCV)
    arm_filter = MicrocontrollerFilter(Microcontroller.ARM)
    st_filter = ManufacturerFilter(Manufacturer.ST)
    nordic_filter = ManufacturerFilter(Manufacturer.NORDIC)
    nordic_arm_filter = arm_filter & nordic_filter
    riscv_or_st_filter = riscv_filter | st_filter

    print("RISCV systems:", [item for item in items if riscv_filter.filter(item)])
    print("Nordic and arm systems: ", [item for item in items if nordic_arm_filter.filter(item)])
    print("ST or RISCV systems: ", [item for item in items if riscv_or_st_filter.filter(item)])
