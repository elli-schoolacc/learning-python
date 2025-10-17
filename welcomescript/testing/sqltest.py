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

def execute_query(connection, query, read: bool = False):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        if read:
            result = cursor.fetchall()
            return result
        else:  
            connection.commit()
    except Error as e:
        print(f"Fatal Exception: {e}")

connection = create("usrdata.sqlite")
createtable = """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uname TEXT NOT NULL,    
    dname TEXT,
    usettings TEXT,
    password TEXT NOT NULL,
    uuid TEXT
    );
    """
insertin = """
    INSERT INTO
    users (uname, password)
    VALUES
    ('James',  'jjames'),
    ('Leila', 'PASSWORD'),
    ('Brigitte', '1234'),
    ('Mike', 'password'),
    ('Elizabeth', 'hello world');
"""
#execute_query(connection, createtable)
#execute_query(connection, insertin)

query = """
SELECT password FROM users where uname='Kite'
"""

jj = execute_query(connection, query, True)
print(jj)

