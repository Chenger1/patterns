from abc import ABC, abstractmethod


class SmartPhone(ABC):
    def call(self, person: str):
        print(f'Calling to {person} using {self.__class__.__name__}')

    def send_message(self, person: str, message: str):
        print(f'{person}: {message} using {self.__class__.__name__}')

    @abstractmethod
    def open_store(self):
        pass


class WindowsPhone(SmartPhone):
    def open_store(self):
        print('Opening Windows Store')


class AndroidPhone(SmartPhone):
    def open_store(self):
        print('Opening Android Store')


class Laptop(ABC):
    def create_file(self, filename: str) -> str:
        return f'{filename}.file on {self.__class__.__name__}'

    @abstractmethod
    def open_browser(self):
        pass


class WindowsLaptop(Laptop):
    def open_browser(self):
        print('Opening Edge')


class AndroidLaptop(Laptop):
    def open_browser(self):
        print('Opening Chrome')


class GadgetFactory(ABC):
    @abstractmethod
    def create_smartphone(self) -> SmartPhone:
        pass

    @abstractmethod
    def create_laptop(self) -> Laptop:
        pass


class WindowsFactory(GadgetFactory):
    def create_smartphone(self) -> SmartPhone:
        return WindowsPhone()

    def create_laptop(self) -> Laptop:
        return WindowsLaptop()


class AndroidFactory(GadgetFactory):
    def create_smartphone(self) -> SmartPhone:
        return AndroidPhone()

    def create_laptop(self) -> Laptop:
        return AndroidLaptop()


def application(factory: GadgetFactory):
    smartphone = factory.create_smartphone()
    laptop = factory.create_laptop()

    smartphone.send_message('Vladislav', 'Hello')
    smartphone.open_store()
    laptop.open_browser()


if __name__ == '__main__':
    user_input = input('Choose OS: ')
    if user_input == 'Windows':
        application(WindowsFactory())
    elif user_input == 'Android':
        application(AndroidFactory())
    else:
        raise ValueError('Wrong OS type')

