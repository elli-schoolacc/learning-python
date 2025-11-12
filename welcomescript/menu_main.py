import helper
import sqlconn as sql
import commandrunner as g


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
    while True:
        helper.clearlines()
        print(f"""
Welcome, {user['dname']}!
Please choose an option:""")
        for key, value in g.menu_options.items():
            print(f"[{key}] {value}")
        choice = helper.promptinput("Select an option:", False)
        returnhandle = menu_choice(choice)
        if returnhandle != "":
            print(returnhandle)
            helper.promptinput("Press Enter to continue...", False)
            
    

def menu_choice(choice: str) -> str:
    """Menu Choice Handler
    Args:
        choice (str): Menu choice input.
    Returns:
        str: Error message if invalid choice, else empty string
    """
    try:
        g.menu_options[choice]
    except KeyError:
        return "Invalid choice, please try again."



