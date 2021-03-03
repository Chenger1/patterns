from abc import ABCMeta, abstractmethod

class SmartPhone(metaclass=ABCMeta):
    def call(self, person: str):
        print(f'Calling to {person}')

    def send_message(self, person: str, message: str):
        print(f'{person}: {message}')

    @abstractmethod
    def open_store(self):
        pass


class WindowsPhone(SmartPhone):
    def open_store(self):
        print('Opening Windows Store')


class AndroidPhone(SmartPhone):
    def open_store(self):
        print('Opening Android Store')


class Laptop(metaclass=ABCMeta):
    def create_file(self, filename: str) -> str:
        return f'{filename}.file'

    @abstractmethod
    def open_browser(self):
        pass


class WindowsLaptop(Laptop):
    def open_browser(self):
        print('Opening Edge')


class AndroidLaptop(Laptop):
    def open_browser(self):
        print('Opening Chrome')


class GadgetFactory(metaclass=ABCMeta):
    @abstractmethod
    def createSmartPhone(self) -> SmartPhone:
        pass

    @abstractmethod
    def createLaptop(self) -> Laptop:
        pass


class WindowsFactory(GadgetFactory):
    def createSmartPhone(self) -> SmartPhone:
        return WindowsPhone()

    def createLaptop(self) -> Laptop:
        return WindowsLaptop()


class AndroidFactory(GadgetFactory):
    def createSmartPhone(self) -> SmartPhone:
        return AndroidPhone()

    def createLaptop(self) -> Laptop:
        return AndroidLaptop()



def application(factory: GadgetFactory):
    smartphone = factory.createSmartPhone()
    laptop = factory.createLaptop()

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

