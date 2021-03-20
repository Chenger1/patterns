from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, handler: 'Handler'):
        self._handler = handler

    @abstractmethod
    def function1(self):
        pass


class Command1(Command):
    def function1(self, value: str) -> str:
        return self._handler.simple_function(value)


class Command2(Command):
    def __init__(self, name: str, handler: 'Handler'):
        super().__init__(handler)
        self._name = name

    def function1(self) -> str:
        return self._handler.simple_function(self._name)

    def function2(self):
        return self._handler.complex_function(self)


class Handler:
    def simple_function(self, value: str) -> str:
        return f'{self.__class__.__name__} + {value}'

    def complex_function(self, command: Command) -> str:
        return f'Current command id is {id(command)}'


class Interface:
    def __init__(self, com1: Command1, com2: Command2):
        self._com1 = com1
        self._com2 = com2

    def execute_commands(self):
        print(com1.function1('Some value'))
        print(com2.function1())
        print(com2.function2())


if __name__ == '__main__':
    handler = Handler()
    com1 = Command1(handler)
    com2 = Command2('Command name', handler)
    interface = Interface(com1, com2)
    interface.execute_commands()
