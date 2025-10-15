import sqlite3
from sqlite3 import Error
import uuid

def create_connection(path):
    conection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f"Fatal Exception: {e}")
    return connection

def initalize_table(connection):
#
# Create Table for User Data
#
#   |id     |username   |displayname    |user settings  |hashed password    | uuid-4    |
#   |       |           |               |               |                   |           |

    createtable = """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uname TEXT NOT NULL,    
    dname TEXT NOT NULL,
    usettings TEXT NOT NULL,
    password TEXT NOT NULL,
    uuid TEXT NOT NULL
    );
    """

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

def find_user(username, hashed_password):
    return