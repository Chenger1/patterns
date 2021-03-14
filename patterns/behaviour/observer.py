import random
from typing import Union


class Subscriber1:
    def notify(self, state_info: int):
        print(f'{state_info*2} - info')


class Subscriber2:
    _value = 2

    def notify(self, state_info: int):
        print(f'{state_info+self._value} + value info')


class System:
    def __init__(self):
        self._subscribers = []
        self._value = 0

    def add_subscriber(self, subscriber: Union[Subscriber1, Subscriber2]):
        self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: Union[Subscriber1, Subscriber2]):
        self._subscribers.remove(subscriber)

    def update(self):
        for sub in self._subscribers:
            sub.notify(self._value)

    def change_value(self):
        self._value = random.randint(1, 100)
        self.update()


if __name__ == '__main__':
    sys = System()
    sub1 = Subscriber1()
    sub2 = Subscriber2()
    sys.add_subscriber(sub1)
    sys.add_subscriber(sub2)

    sys.change_value()
