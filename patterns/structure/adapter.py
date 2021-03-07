from typing import List, Tuple, Dict
import sqlite3

import os


class DataBase:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "example.db")

    @classmethod
    def get_from_db(cls) -> List[Tuple[str, str, int]]:
        conn = sqlite3.connect(cls.db_path)
        raw_data = conn.execute('SELECT * FROM cars')
        return raw_data.fetchall()


class Analytics:
    @classmethod
    def analyze_data(cls, data:  Dict[str, Dict[str, List[int]]]) -> List[str]:
        temp = cls._proceed_data(data)
        result = cls._create_list_of_strings(temp)
        return result

    @classmethod
    def _proceed_data(cls, data:  Dict[str, Dict[str, List[int]]]) -> Dict[str, Dict[str, int]]:
        temp = {}
        for key in data.keys():
            count = len(data[key]['speed']) - 1
            speed = sum(data[key]['speed']) // count
            temp[key] = {'count': count, 'average_speed': speed}
        return temp

    @classmethod
    def _create_list_of_strings(cls, data: Dict[str, Dict[str, int]]) -> List[str]:
        result = []
        for key, value in data.items():
            result.append(f'For {key} average speed - {value["average_speed"]}. Total cars: {value["count"]}')
        return sorted(result)


class Adapter:
    def __init__(self, adapted: Analytics):
        self.adapted = adapted

    def analyze_data(self, to_adapt: List[Tuple[str, str, int]]) -> List[str]:
        result = {}
        data_keys = {elem[0] for elem in to_adapt}
        for key in data_keys:
            speeds = [elem[2] for elem in to_adapt if elem[0] == key]
            result[key] = {'speed': speeds}
        return self.adapted.analyze_data(result)


def client():
    data_from_db = DataBase.get_from_db()
    adapter = Adapter(Analytics())
    result = adapter.analyze_data(data_from_db)

    for elem in result:
        print(elem)


if __name__ == '__main__':
    client()
