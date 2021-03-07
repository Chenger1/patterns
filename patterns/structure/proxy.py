from typing import Tuple


class User:
    _counter = 0

    def __init__(self, user_name: str, is_admin: bool = False):
        self._user_name = user_name
        self.is_admin = is_admin
        self._increase_counter()

    @property
    def counter(self):
        return f'Total users: {self._counter}'

    @classmethod
    def _increase_counter(cls):
        cls._counter += 1

    def __str__(self):
        options = {True: 'is admin',
                   False: 'is NOT admin'}
        return f'#{self._counter}. {self._user_name} - {options[self.is_admin]}'


class Profile:
    def __init__(self, user: User, profile_info: Tuple[str, str, str]):
        self.user = user
        self._profile_info = profile_info

    @property
    def profile_info(self):
        info = ', '.join(self._profile_info)
        return f'{self.user} -> {info}'

    @profile_info.setter
    def profile_info(self, profile_info: Tuple[str]):
        self._profile_info = profile_info

    def get_user_counter(self) -> str:
        """Admin feature"""
        return self.user.counter


class Proxy(Profile):
    def get_user_counter(self) -> str:
        if not self._check_access():
            return f'{self.user} -> Don`t have access'
        return self.user.counter

    def _check_access(self) -> bool:
        return self.user.is_admin


if __name__ == '__main__':
    user1 = User('John')
    user_admin = User('Jack', is_admin=True)
    profile1 = Proxy(user1, ('men', '21', 'City1'))
    profile2 = Proxy(user_admin, ('men', '43', 'City2'))
    print(profile1.profile_info)
    print(profile1.get_user_counter())

    print(profile2.profile_info)
    print(profile2.get_user_counter())
