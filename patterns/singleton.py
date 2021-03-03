class DataBase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def connect(self):
        print('Connected')


if __name__ == '__main__':
    db = DataBase()
    db.connect()
    db1 = DataBase()
    print(db is db1)