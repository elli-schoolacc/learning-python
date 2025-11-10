import hashlib
import getpass
import sqlconn
import uuid

def pwdin() -> str:
    try:
        res = hashlib.sha384(getpass.getpass("> ").encode()).hexdigest()
        return res
    except KeyboardInterrupt:
        exit(0)

def attemptLogin(username, hashed_password):
    un = username
    pwd = hashed_password
    connection = sqlconn.create_connection("./usrdata")
    dbpwd = sqlconn.find_user(connection,un)
    if dbpwd is None:
        print("Password or Username incorrect")
        return False
    if pwd == dbpwd:
        return True

    


def debug_listTable():
    connection = sqlconn.create_connection("./usrdata")
    print(sqlconn.fetch_table(connection))
    

def createuser(uname: str, password: str, displayname: str = "", connection=sqlconn.create_connection("./usrdata")):
    c_result = []
    c_username: str = uname
    c_displayname: str = displayname
    c_settings: str
    c_password: str = password
    c_uuid: str = str(uuid.uuid4())

    #validity check
    if len(c_username) < 3:
        c_result.append("At least 3 Char")
    if any(not c.isalnum for c in c_username):
        c_result.append("only use alnum")
    
    if displayname == "":
        c_displayname = uname
    
    c_settings = "default-settings"

#   |id     |username   |displayname    |user settings  |hashed password    | uuid-4    |
#   |       |           |               |               |                   |           |

    cuserstr = f"""
        INSERT INTO
        users ('uname', 'dname', 'usettings', 'password', 'uuid')
        VALUES ('{c_username}', '{c_displayname}', '{c_settings}', '{c_password}', '{c_uuid}')"""
    
    sqlconn.execute_query(connection, cuserstr)