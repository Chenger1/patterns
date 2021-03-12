from abc import ABC, abstractmethod
import random


class Report(ABC):
    _next_handler = None

    def set_next(self, handler: 'Report'):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, data):
        if self._next_handler:
            return self._next_handler.handle(data)


class FinancialReport(Report):
    def handle(self, data: str):
        if data == 'Finance':
            return f'Debit: {random.randint(200, 500)}. Credit: {random.randint(400, 500)}'
        return super().handle(data)


class MarketingReport(Report):
    def handle(self, data: str):
        if data == 'Marketing':
            return f'Market research: Most popular-{random.choice(["Tablet", "Phone"])}. \nKey feature: {random.choice(["Internet", "GPS"])}'
        return super().handle(data)


class ResourceReport(Report):
    def handle(self, data: str):
        if data == 'Resource':
            return f'Resource reporting are in process'
        return super().handle(data)


def client(handler: Report):
    user_input = input('Choose report: ')
    print(handler.handle(user_input))


if __name__ == '__main__':
    report = FinancialReport()
    report.set_next(MarketingReport()).set_next(ResourceReport())
    client(report)
