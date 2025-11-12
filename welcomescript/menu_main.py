import helper
import sqlconn as sql


def startmenu(user_uuid : str) -> None:
    """
    Start Menu after login
    Args: 
    user (str): Logged in user as UUID
    Returns: None
    UUID to be used to fetch user data from SQL database
    """
    impdata = sql.find_item(sql.create_connection("./usrdata"), "*", "uuid", user_uuid)[0]
    user = {
        'id': impdata[0],
        'uname': impdata[1],
        'dname': impdata[2],
        'usettings': impdata[3],
        'password': impdata[4],
        'uuid': impdata[5]
    }
    helper.clearlines()
    print(f"Welcome, {user['dname']}!")