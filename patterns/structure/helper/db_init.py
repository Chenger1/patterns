import sqlite3

conn = sqlite3.connect('../example.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS 'cars' (
                'car_type' TEXT,
                'color' TEXT,
                'speed' INTEGER)""")

cur.execute("""INSERT INTO 'cars' VALUES
                ('sport_car', 'red', 200),
                ('truck', 'blue', 59),
                ('sedan', 'black', 60),
                ('sport_car', 'red', 150),
                ('sport_car', 'black', 240),
                ('sedan', 'blue', 89),
                ('sport_car', 'black', 130),
                ('truck', 'red', 20)""")
conn.commit()
conn.close()
