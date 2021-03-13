from typing import Any, Collection


class NewIterator:
    def __init__(self, iterable: Collection):
        self._iterable = iterable
        self._position = 0

    def __next__(self):
        if self._position < len(self._iterable):
            elem = self._iterable[self._position]
            self._position += 1
            return elem
        else:
            raise StopIteration


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, value: Any):
        self._stack.append(value)

    def pop(self) -> Any:
        return self._stack.pop()

    def __iter__(self):
        return NewIterator(self._stack)

    def __str__(self):
        return f'{self._stack}'


if __name__ == '__main__':
    collection = Stack()
    for elem in range(1, 10):
        collection.push(elem)
    print(collection)

    for elem in collection:
        print(elem)

