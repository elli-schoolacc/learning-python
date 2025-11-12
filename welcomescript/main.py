
import login
import helper
from menu_main import startmenu
from sqlconn import find_item, create_connection

def main():
    #helper.clearlines()
    while True:
        uname = helper.promptinput("Enter your username:", False)
        print("Password:")
        hpwd = login.pwdin()
        if login.attemptLogin(uname,hpwd):
            break
        print("Password or Username incorrect")
    uuid = find_item(create_connection("./usrdata"), "uuid", "uname", uname)[0][0]
    startmenu(uuid)    

def createu():
    print("Create User Menu")
    while True:
        uname = helper.promptinput("Enter your username:", False).lower()
        if not login.checkcomponents(uname):
            print("Username must be at least 3 characters and only contain alphanumeric characters.")
            continue
        if not login.checkavailability(uname):
            print("Username already exists, please choose another.")
            continue
        break

    dname = helper.promptinput("Enter your displayname (default to username):", False)
    while True:
        print("Enter Password:")
        upwd = login.pwdin()
        print("Enter Password again:")
        upwd2 = login.pwdin()
        if upwd == upwd2:
            break
        print("Passwords do not match.")
    try:
        login.createuser(uname, upwd, dname)
    except Exception as e:
        print(f"Error creating user: {e}")
        return


if __name__ == "__main__":
    #createu()
    login.debug_listTable()
    main()
    