import datetime
import random
from copy import deepcopy


class Document:
    def __init__(self, fonts: str, color: hex, interval: float):
        self._fonts = fonts
        self._color = color
        self._interval = interval

    def save(self):
        return Memento(deepcopy(self))

    def restore(self, memento: 'Memento'):
        state = memento.get_state()
        vars(self).update(vars(state))

    def change_fonts(self):
        self._fonts = random.choice(['Arial', 'Picket', 'Tahoma', 'Georgia', 'Helvetica', 'FontOne'])

    def __str__(self):
        return f'Document: fonts - {self._fonts}, color - {self._color} - interval: {self._interval}'


class Memento:
    def __init__(self, state: Document):
        self._state = state
        self._date = datetime.datetime.now()

    def get_state(self) -> Document:
        return self._state

    def __str__(self):
        return f'Snapshot: {self._date} with {self._state}'


class Organizer:
    def __init__(self, doc: Document):
        self._history = []
        self._document = doc

    def backup(self):
        self._history.append(self._document.save())

    def restore(self):
        if self._history:
            memento = self._history.pop()
            self._document.restore(memento)

    def show_history(self):
        for index, elem in enumerate(self._history):
            print(f'{index}. {elem}')


if __name__ == '__main__':
    document = Document('TimesNewRoman', 0x03fc3d, 1.5)
    organizer = Organizer(document)
    print(document)
    organizer.backup()
    document.change_fonts()

    print(document)
    organizer.backup()

    document.change_fonts()
    print(document)

    organizer.show_history()
    organizer.restore()
    print(document)
