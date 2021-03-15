from abc import ABC, abstractmethod
from typing import List


class System(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def call_visitor(self, visitor: 'Visitor'):
        pass


class SystemOne(System):
    def __init__(self):
        self._data = None

    def get_data(self):
        self._data = f'System {self.__class__.__name__}'

    def call_visitor(self, visitor: 'Visitor'):
        visitor.visit_system_one(self, self._data)


class SystemTwo(System):
    def __init__(self):
        self._data = 'Expected data'

    def get_data(self):
        self._data = f'System {self.__class__.__name__} + {self.__dict__}'

    def call_visitor(self, visitor: 'Visitor'):
        visitor.visit_system_two(self, self._data)


class Visitor:
    def visit_system_one(self, system: SystemOne, data: str):
        print(f'From {system} received {data}')

    def visit_system_two(self, system: SystemTwo, data: str):
        print(f'From {system} received additional {data}')


def client(visitor: Visitor, systems: List[System]):
    for system in systems:
        system.get_data()
        system.call_visitor(visitor)


if __name__ == '__main__':
    systems = [SystemOne(), SystemTwo()]
    visitor = Visitor()
    client(visitor, systems)
