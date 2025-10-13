import sqlite3
from sqlite3 import Error

def create(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("created & connected")
    except Error as e:
        print("error: {e}")
    return connection

connection = create("./test.sqlite")