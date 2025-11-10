import sqlite3
from sqlite3 import Error
import uuid

def create_connection(path):
    conection = None
    try:
        connection = sqlite3.connect(path)
        initalize_table(connection)
    except Error as e:
        print(f"Fatal Exception: {e}")
    return connection

def initalize_table(connection):

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
    execute_query(connection,createtable)

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

def find_user(connection, username):
    fetch_usr_pwd = f"""
    SELECT password FROM users WHERE uname='{username}' """
    try:
        hashpwd= execute_query(connection, fetch_usr_pwd, True)
        return hashpwd[0][0]
    except Error as e:
        print(f"Exception: {e}")
    return None

def find_item(connection, column, where, what):
    fetch_: f"SELECT {column} FROM users WHERE {where}='{what}'"
    try:
        fin_return = execute_query(connection, fetch_, True)
        return fin_return
    except Error as e:
        print(f"Exception: {e}")
    return None

def fetch_table(connection):
    fetch_req = f"""
    SELECT * FROM users """
    try:
        fetch = execute_query(connection, fetch_req, True)
        return fetch
    except Error as e:
        print(f"Exception: {e}")
    return None