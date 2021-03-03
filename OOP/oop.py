from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, driver: str, max_speed: int):
        self.driver = driver
        self.max_speed = max_speed
        self._status = False

    @abstractmethod
    def deliver_goods(self):
        pass

    @property
    def miles(self):
        return self.max_speed / 1.6

    @property
    def status(self):
        options = {True: 'Is working',
                   False: 'Is not working'}
        return options[self._status]

    @status.setter
    def status(self, value: bool):
        self._status = value

    def __str__(self):
        return f'{self.__class__.__name__} with driver - {self.driver}'


class Car(Transport):
    def __init__(self, driver: str, max_speed: int, car_type: str):
        super().__init__(driver, max_speed)
        self.car_type = car_type

    def deliver_goods(self):
        print(f'Delivered by {self.driver}')

    def deliver_person(self, person: str):
        print(f'{person} has been delivered by {self.driver} on {self.car_type}')


class Truck(Transport):
    def __init__(self, driver: str, max_speed: int, payload: int):
        super().__init__(driver, max_speed)
        self.payload = payload

    def deliver_goods(self):
        print(f'Delivered by truck with payload {self.payload}')


if __name__ == '__main__':
    transport1 = Car('driver1', 60, 'sedan')
    transport2 = Truck('driver2', 35, 100)
    print(transport1.status)
    transport1.status = True
    print(transport1.status)
    transport2.status = True
    transport2.deliver_goods()
    print(transport1)
