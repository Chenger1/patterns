from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self):
        self._context = None

    @property
    def context(self) -> 'Context':
        return self._context

    @context.setter
    def context(self, value: 'Context'):
        self._context = value

    @abstractmethod
    def function(self, value: int):
        pass


class FirstState(State):
    def function(self, value: int) -> str:
        return f'State: {self.__class__.__name__} + value: {value * 2}'


class SecondState(State):
    def function(self, value: int) -> str:
        return f'State: {self.__class__.__name__} + value: {value * 4}'


class ThirdState(State):
    def function(self, value: int) -> str:
        return f'State: {self.__class__.__name__} + value: {value * 6}'


class Context:
    def __init__(self, state: State):
        self._state = state

    @property
    def state(self) -> State:
        return self._state

    @state.setter
    def state(self, value: State):
        print(f'Now state is {value}')
        self._state = value

    def function(self, value: int):
        return self._state.function(value)


if __name__ == '__main__':
    state1 = FirstState()
    state2 = SecondState()
    state3 = ThirdState()
    context = Context(state1)

    print(context.function(5))

    context.state = state3

    print(context.function(6))

    context.state = state2

    print(context.function(7))
