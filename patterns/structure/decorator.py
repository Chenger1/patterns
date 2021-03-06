from abc import ABC, abstractmethod
from typing import Union


class Messenger:
    def __init__(self, user: str):
        self._user = user

    def send_message(self, msg: str) -> str:
        return f'{self._user} -- {msg}'


class Decorator(ABC):
    def __init__(self, decorated: Union[Messenger, 'Decorator']):
        self._decorated = decorated

    @abstractmethod
    def send_message(self, msg: str) -> str:
        return self._decorated.send_message(msg)


class EncryptDecorator(Decorator):
    def send_message(self, msg: str) -> str:
        encrypted = msg[::-1]
        return self._decorated.send_message(encrypted)


class CompressDecorator(Decorator):
    def send_message(self, msg: str) -> str:
        compressed = f'[Compressed] {msg}'
        return self._decorated.send_message(compressed)


if __name__ == '__main__':
    messenger = Messenger('John')
    print(messenger.send_message('First'))
    compr = CompressDecorator(messenger)
    print(compr.send_message('First'))
    enc = EncryptDecorator(compr)
    print(enc.send_message('First'))

