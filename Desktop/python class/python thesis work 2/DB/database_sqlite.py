import sqlite3

from Vk_information import get_users_for_date, age_preferences, get_photos




class Customers:
    def __init__(self):
        self.connect = sqlite3.connect('database.db')
        self.cursor = self.connect.cursor()
        self.create_table()

    def create_table(self):
        #self.cursor.execute("""DROP TABLE customers""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS customers(
        id INTEGER, 
        name TEXT
        )""")

    def instert(self, item):
        self.cursor.execute("""INSERT OR IGNORE INTO customers VALUES (?, ?)""", item)
        self.connect.commit()

    def read(self):
        self.cursor.execute("""SELECT * FROM customers""")
        rows = self.cursor.fetchall()
        return rows

#bd = Customers()

#item = (12314124, 'MASha')
#bd.instert(item)


#for item in bd.read():
#   print(item)

class People_to_date:
    def __init__(self):
        self.connect = sqlite3.connect('database.db')
        self.cursor = self.connect.cursor()
        self.create_table()

    def create_table(self):
        #self.cursor.execute("""DROP TABLE People_to_date""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS People_to_date(
        id INTEGER, 
        name TEXT, 
        id_photo INTEGER )
        """)

    def instert(self, item):
        self.cursor.execute("""INSERT OR IGNORE INTO People_to_date VALUES (?, ?, ?)""", item)
        self.connect.commit()

    def read(self):
        self.cursor.execute("""SELECT * FROM People_to_date""")
        rows = self.cursor.fetchall()
        return rows

#bdd = People_to_date()

#item = (123141245, 'MArSha', 5738)
#itemssss = (123143451245, 'margarita', 53425738)
#bdd.instert(itemssss)
#bdd.instert(item)

#for item in bdd.read():
#    print(item)

class people_that_where_shown:
    def __init__(self):
        self.connect = sqlite3.connect('database.db')
        self.cursor = self.connect.cursor()
        self.create_table()

    def create_table(self):
        #self.cursor.execute("""DROP TABLE people_that_where_shown""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS people_that_where_shown(
        id INTEGER, 
        name TEXT, 
        id_photo INTEGER )
        """)

    def instert(self, item):
        self.cursor.execute("""INSERT OR IGNORE INTO people_that_where_shown VALUES (?, ?, ?)""", item)
        self.connect.commit()

    def read(self):
        self.cursor.execute("""SELECT * FROM people_that_where_shown""")
        rows = self.cursor.fetchall()
        return rows

#bdds = people_that_where_shown()

#item = (123143451245, 'margarita', 53425738)
#bdds.instert(item)

#for item in bdds.read():
#    print(item)

connect = sqlite3.connect('database.db')
cursor = connect.cursor()
cursor.execute("""SELECT people_that_where_shown.id, People_to_date.id FROM people_that_where_shown, People_to_date""")
cursor.execute("""SELECT * FROM people_that_where_shown s LEFT JOIN People_to_date d ON""")
s.id = d.id WHERE s.name <> d.name
for id in cursor:
    print(id)

## Tried to use this one
cursor.execute("""SELECT People_to_date.*, people_that_where_shown.*
FROM People_to_date FULL JOIN people_that_where_shown ON
(People_to_date.id = people_that_where_shown.if) 
WHERE People_to_date.id IS NULL OR people_that_where_shown.id IS NULL""")
