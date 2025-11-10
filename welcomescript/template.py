
import login
import helper

def main():
    proc : bool = False
    #helper.clearlines()
    while not proc:
        uname = helper.promptinput("Enter your username:", False)
        print("Password:")
        hpwd = login.pwdin()
        if login.attemptLogin(uname,hpwd):
            proc = True
            break
        print("Password or Username incorrect")
    print(f"Welcome back, {uname}!")

def createu():
    print("Create User Menu")
    uname = helper.promptinput("Enter your username:", False).lower()
    dname = helper.promptinput("Enter your displayname (default to username):", False)
    upwd = login.pwdin()
    login.createuser(uname, upwd, dname)


if __name__ == "__main__":
    #createu()
    login.debug_listTable()
    main()