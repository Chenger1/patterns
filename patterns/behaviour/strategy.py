from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Strategy(ABC):
    @abstractmethod
    def open_file(self, file):
        pass

    def analyze_data(self, data: dict) -> str:
        result = ''
        for key, value in data['package'].items():
            result += f'{key} - {value}\n'
        return result


class TxtStrategy(Strategy):
    def open_file(self, file) -> dict:
        data = {'package': {}}
        with open(file, 'r') as opened_file:
            for line in opened_file.readlines()[1:]:
                key, value = line.split(':')
                data['package'].update({key: value.strip()})
            data['package'].update({'origin': 'txt'})
        return data


class JsonStrategy(Strategy):
    def open_file(self, file) -> dict:
        with open(file, 'r') as opened_file:
            data = json.load(opened_file)
            data['package'].update({'origin': 'json'})
        return data


class XmlStrategy(Strategy):
    def open_file(self, file) -> dict:
        tree = ET.parse(file)
        root = tree.getroot()
        data = {'package': {}}
        for tag in list(root.iter())[1:]:
            data['package'].update({tag.tag: tag.text})
        data['package'].update({'origin': 'xml'})
        return data


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, value: Strategy):
        self._strategy = value

    def get_data(self, file) -> str:
        raw_data = self._strategy.open_file(file)
        data = self._strategy.analyze_data(raw_data)
        return data


if __name__ == '__main__':
    while True:
        file_type = input('Choose file type: ')
        if file_type == 'json':
            file_name = 'data.json'
            strategy = JsonStrategy()
        elif file_type == 'txt':
            file_name = 'data.txt'
            strategy = TxtStrategy()
        elif file_type == 'xml':
            file_name = 'data.xml'
            strategy = XmlStrategy()
        file_path = os.path.join(BASE_DIR, file_name)
        context = Context(strategy)
        print(context.get_data(file_path))
