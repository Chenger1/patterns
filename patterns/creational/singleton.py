class DataBase:
    # _instance = None
    #
    # def __new__(cls, *args, **kwargs):
    #     if not cls._instance:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance

    def connect(self):
        print('Connected')


class Singleton:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = DataBase()
        return cls._instance


if __name__ == '__main__':
    # db = DataBase()
    # db.connect()
    # db1 = DataBase()
    db = Singleton.get_instance()
    db.connect()
    db1 = Singleton.get_instance()
    print(db is db1)
    print(id(db))
    print(id(db1))
