from abc import ABC
import random


class Component(ABC):
    def __init__(self):
        self._mediator = None

    @property
    def mediator(self) -> 'Mediator':
        return self._mediator

    @mediator.setter
    def mediator(self, value: 'Mediator'):
        self._mediator = value


class Button(Component):
    def click(self):
        self._mediator.request('Message text', random.choice(['common', 'special']))

    def change_button_text(self, value: str):
        print(f'New Button text: {value}')


class Label(Component):
    def display_common_text(self, text: str):
        print(f'Text: {text}')

    def display_special_text(self, text: str):
        print(f'Special text: {text}')

    def respond(self):
        self._mediator.request('Button TWO', 'button')


class Mediator:
    def __init__(self, elem1: Button, elem2: Label):
        self._button = elem1
        self._label = elem2
        self._button.mediator = self
        self._label.mediator = self

    def request(self, data: str, event: str):
        if event == 'common':
            self._label.display_common_text(data)
        elif event == 'special':
            self._label.display_special_text(data)
        elif event == 'button':
            self._button.change_button_text(data)


if __name__ == '__main__':
    button = Button()
    label = Label()
    mediator = Mediator(button, label)
    button.click()
    label.respond()
