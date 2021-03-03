from abc import ABCMeta, abstractmethod

class Transport(metaclass=ABCMeta):
    @abstractmethod
    def deliver(self):
        pass


class Car(Transport):
    def deliver(self):
        print('Delivered by car')


class Airplane(Transport):
    def deliver(self):
        print('Delivered by plane')


class TransportFactory(metaclass=ABCMeta):
    @abstractmethod
    def createTransport(self):
        pass


class CarFactory(TransportFactory):
    def createTransport(self) -> Car:
        return Car()


class AirplaneFactory(TransportFactory):
    def createTransport(self) -> Airplane:
        return Airplane()


def logistics(factory: TransportFactory):
    print(f'Created by: {factory.__class__.__name__}')
    transport = factory.createTransport()
    transport.deliver()

if __name__ == '__main__':
    logistics(CarFactory())