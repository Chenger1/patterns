from abc import ABC, abstractmethod
from typing import Union, List


class MenuComposite(ABC):
    def __init__(self, value: str):
        self.value = value

    @abstractmethod
    def show(self, indent: int = 1):
        pass

    @abstractmethod
    def return_self_value(self):
        pass

    def add(self, child):
        pass

    def remove(self):
        pass


class MenuItem(MenuComposite):
    def show(self, indent: int = 1):
        print(f'{" "*indent} -{self.value}')

    def return_self_value(self):
        print(f'{self.value}')


class MenuList(MenuComposite):
    def __init__(self, value: str):
        super().__init__(value)
        self._children = []

    def add(self, children: Union[MenuComposite, List[MenuComposite]]):
        if isinstance(children, list):
            for child in children:
                self._children.append(child)
        else:
            self._children.append(children)

    def remove(self):
        self._children.pop()

    def show(self, indent: int = 1):
        print(f'{" " * indent} -*{self.value}')
        if self._children:
            for child in self._children:
                child.show(indent+3)
        else:
            print(f'{" " * (indent+3)} -Empty list')

    def return_self_value(self):
        print(f'{self.value}')


def client(composite: MenuComposite):
    composite.show()
    print('-------------------\n')
    composite.return_self_value()
    print('-------------------\n')


if __name__ == '__main__':
    elements = [MenuItem(f'item{elem}') for elem in range(11)]
    lists = [MenuList(f'list{elem}') for elem in range(6)]
    main_list = MenuList('Main List')
    main_list.add(elements[:5])
    lists[3].add(elements[6])
    lists[4].add(elements[6:])
    main_list.add(lists)

    client(main_list)
    client(elements[0])
