from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def function(self):
        pass


class CommandOn(Command):
    def function(self):
        return 'Computer is working now'


class CommandOff(Command):
    def function(self):
        return 'Computer is off'


class CommandClean(Command):
    def function(self):
        return 'Clean RAM'


class CommandReboot(Command):
    def function(self):
        return 'Rebooting system...'


class Handler:
    def __init__(self):
        self._commands = []

    def add(self, command: Command):
        self._commands.append(command)

    def execute(self):
        for comm in self._commands:
            print(comm.function())

#включить/выключить, очистить и перезагрузить системы - действия команд


if __name__ == '__main__':
    handler = Handler()
    handler.add(CommandOn())
    handler.add(CommandOff())
    handler.add(CommandReboot())
    handler.add(CommandClean())

    handler.execute()

    print('____________')
    handler.add(CommandOff())
    handler.execute()
