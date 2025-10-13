import sqlite3
from sqlite3 import Error

def create(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("created & connected")
    except Error as e:
        print(f"error: {e}")
    return connection

def execute(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("ex successfull")
    except Error as e:
        print(f"error: {e}")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

connection = create("./test.sqlite")
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
);
"""
insertin = """
INSERT INTO
  users (name, age, gender, nationality)
VALUES
  ('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada');
"""
#execute(connection, create_users_table)
#execute(connection, insertin)

select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)
for user in users:
    print(user)



query = """
SELECT * FROM users where name = 'James'
"""
jj = execute_read_query(connection, query)
print(jj)

