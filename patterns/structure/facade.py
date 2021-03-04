from typing import List
from adapter import Adapter, DataBase, Analytics


class Facade:
    def __init__(self):
        self._db = DataBase()
        self._analytics = Analytics()
        self._adapter = Adapter(self._analytics)

    def get_data(self) -> List[str]:
        data_from_db = self._db.get_from_db()
        result = self._adapter.analyze_data(data_from_db)
        return result


if __name__ == '__main__':
    facade = Facade()
    data = facade.get_data()
    for elem in data:
        print(elem)
