import hashlib
import getpass
import sqlconn
import uuid
import helper as h 

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
    

def checkavailability(username: str, connection=sqlconn.create_connection("./usrdata")) -> bool:
    existing_usr = sqlconn.find_item(connection, "uname", "uname", username)
    if existing_usr == None:
        return True
    return False

def checkcomponents(username: str) -> bool:
    if len(username) < 3:
        return False
    if any(not c.isalnum for c in username):
        return False
    return True

def createuser(uname: str, password: str, displayname: str = "", connection=sqlconn.create_connection("./usrdata")):
    c_result = []
    c_username: str = uname
    c_displayname: str = displayname
    c_settings: str
    c_password: str = password



    while True:
        c_uuid: str = str(uuid.uuid4())
        existing_uuid = sqlconn.find_item(connection, "uuid", "uuid", c_uuid)
        if existing_uuid is None:
            break

    #validity check
    if len(c_username) < 3:
        raise h.UsernameError("Username too short")
    if any(not c.isalnum for c in c_username):
        raise h.UsernameError("Username contains invalid characters")
    
    existing_usr = sqlconn.find_item(connection, "uname", "uname", c_username)
    if existing_usr is None:
        raise h.UsernameError("Username already exists")

    if displayname == "":
        c_displayname = uname
    
    c_settings = "default-settings"
    
    cuserstr = f"""
        INSERT INTO
        users ('uname', 'dname', 'usettings', 'password', 'uuid')
        VALUES ('{c_username}', '{c_displayname}', '{c_settings}', '{c_password}', '{c_uuid}')"""
    
    sqlconn.execute_query(connection, cuserstr)