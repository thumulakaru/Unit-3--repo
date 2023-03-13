import sqlite3

haiku = """Code flows like a stream
Algorithms guide its way
In silence, it solves"""

class database_handler:
    def __init__(self, dbname):
        self.connection = sqlite3.connect(dbname)
        self.cursor = self.connection.cursor()

    def run_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def search(self, query):
        result = self.cursor.execute(query).fetchone()
        return result

    def close(self):
        self.connection.close()

    def create_table(self):
        query = f"""CREATE TABLE IF NOT EXISTS words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL,
        length INTEGER NOT NULL)"""
        self.run_query(query)


db = database_handler("Quiz_046.db")
db.create_table()

for word in haiku.split():
    query = f"INSERT INTO words (word, length) VALUES ('{word}', {len(word)})"
    db.run_query(query)

query_2  = f"SELECT avg(length) from words"
length = db.search(query_2)

db.close()
print(f"This is the average obtained using sqlite: {length[0]}")

# Using python
length = []
for word in haiku.split():
    length.append(len(word))

print(f"This is the average obtained using python: {sum(length)/len(length)}")