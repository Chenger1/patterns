from abc import ABC, abstractmethod


class MenuComposite(ABC):
    def __init__(self, value: str):
        self.value = value

    @abstractmethod
    def show(self, indent: int = 1):
        pass

    def add(self, child):
        pass

    def remove(self):
        pass


class MenuItem(MenuComposite):
    def show(self, indent: int = 1):
        print(f'{" "*indent} -{self.value}')


class MenuList(MenuComposite):
    def __init__(self, value: str):
        super().__init__(value)
        self._children = []

    def add(self, child: MenuComposite):
        self._children.append(child)

    def remove(self):
        self._children.pop()

    def show(self, indent: int = 1):
        print(f'{" " * indent} -*{self.value}')
        for child in self._children:
            child.show(indent+3)


def client(composite: MenuComposite):
    composite.show()


if __name__ == '__main__':
    main_list = MenuList('Main List')
    list1 = MenuList('List-1')
    list2 = MenuList('List-2')
    list3 = MenuList('List-3')
    list4 = MenuList('List - 4')

    elem1 = MenuItem('Elem-1')
    elem2 = MenuItem('Elem-2')
    elem3 = MenuItem('Elem-3')
    elem4 = MenuItem('Elem-4')
    elem5 = MenuItem('Elem-5')
    elem6 = MenuItem('Elem-6')
    elem7 = MenuItem('Elem-7')
    elem8 = MenuItem('Elem-8')
    elem9 = MenuItem('Elem-9')
    elem10 = MenuItem('Elem-10')

# Lists
    main_list.add(list1)
    main_list.add(list2)

    list2.add(list3)
    list2.add(list4)


# Elem

    list1.add(elem1)

    list2.add(elem2)
    list2.add(elem3)

    list3.add(elem4)
    list3.add(elem5)
    list3.add(elem6)
    list3.add(elem7)

    list4.add(elem9)
    list4.add(elem10)

    main_list.add(elem8)

    client(main_list)
