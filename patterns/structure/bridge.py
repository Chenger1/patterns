from abc import ABC, abstractmethod


class Implementation(ABC):
    @abstractmethod
    def create_modal(self):
        pass

    @abstractmethod
    def create_dialog(self):
        pass

    def show_system_message(self):
        print(f'{self.__doc__}\n*id -- {id(self)}')

    def close(self):
        print(f'Close window - {self.__class__.__name__}')


class WindowsImplementation(Implementation):
    """Windows System OS 11"""
    def create_modal(self):
        print('Windows modal')

    def create_dialog(self):
        print('Windows dialog')


class AndroidImplementation(Implementation):
    """Android system OS 12"""
    def create_modal(self):
        print('Android modal')

    def create_dialog(self):
        print('Android dialog')


class Abstraction:
    def __init__(self, implementation: Implementation):
        self.implementation = implementation

    def create_ui(self):
        self.implementation.create_modal()
        self.implementation.create_dialog()
        self.implementation.close()


class ExtendedAbstraction(Abstraction):
    def create_system_info_message(self):
        print('System information: ')
        self.implementation.show_system_message()


def client(os: str):
    if os == 'Windows':
        implementation = WindowsImplementation()
    elif os == 'Android':
        implementation = AndroidImplementation()
    else:
        raise ValueError('Wrong OS')
    abstraction = Abstraction(implementation)
    abstraction.create_ui()
    advanced = ExtendedAbstraction(implementation)
    advanced.create_system_info_message()


if __name__ == '__main__':
    user_input = input('Choose os: ')
    client(user_input)
