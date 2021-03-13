from abc import ABC, abstractmethod


class Template:
    def __init__(self):
        self._product = ''

    def template_method(self):
        self.title()
        self.company_name()
        self.performers()
        self.body()
        self.plans()
        self.links()

        return self._product

    def title(self):
        self._product += 'Report\n'

    def company_name(self):
        self._product += 'First company\n'

    @abstractmethod
    def performers(self):
        pass

    @abstractmethod
    def body(self):
        pass

    def plans(self):
        self._product += 'Be more productive\n'

    def links(self):
        pass


class Finance(Template):
    def performers(self):
        self._product += 'Made by: John Joe\n'

    def body(self):
        self._product += 'Main part of the report\n'

    def plans(self):
        self._product += 'Gain million'


class Marketing(Template):
    def performers(self):
        self._product += 'Created by: Rick Ol\n'

    def body(self):
        self._product += 'Marketing report\n'

    def links(self):
        self._product += 'Contact: rick@mail.com\n'


if __name__ == '__main__':
    report1 = Finance()
    report2 = Marketing()
    print(report1.template_method())
    print('--------------------------------')
    print(report2.template_method())
