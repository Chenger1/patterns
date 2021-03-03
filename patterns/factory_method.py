from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Car(Transport):
    def deliver(self):
        print('Delivered by car')


class Airplane(Transport):
    def deliver(self):
        print('Delivered by plane')


class TransportFactory(ABC):
    @abstractmethod
    def create_transport(self):
        pass


class CarFactory(TransportFactory):
    def create_transport(self) -> Car:
        return Car()


class AirplaneFactory(TransportFactory):
    def create_transport(self) -> Airplane:
        return Airplane()


def logistics(factory: TransportFactory):
    print(f'Created by: {factory.__class__.__name__}')
    transport = factory.create_transport()
    transport.deliver()


if __name__ == '__main__':
    logistics(CarFactory())
