

import login
import helper

def main():
    helper.clearlines()
    print("UUT starting up... \n Welcome!")
    uname = helper.promptinput("Enter your username:")
    print("Password:")
    hpwd = login.pwdin()
    login.attemptLogin(uname,hpwd)


if __name__ == "__main__":
    main()