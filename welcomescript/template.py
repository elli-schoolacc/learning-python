
import login
import helper

def main():
    helper.clearlines()
    print("UUT starting up... \n Welcome!")
    uname = helper.promptinput("Enter your username:")    
    print("Password:")
    hpwd = login.pwdin()
    login.attemptLogin(uname,hpwd)

def createu():
    print("Create User Menu")
    uname = helper.promptinput("Enter your username:", False)
    dname = helper.promptinput("Enter your displayname (default to username):", False)
    upwd = login.pwdin()
    login.createuser(uname, upwd, dname)



if __name__ == "__main__":
    createu()