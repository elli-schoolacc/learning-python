
import getpass
import hashlib
import helper

def main():
    helper.clearlines()
    print("UUT starting up... \n Welcome!")
    uname = helper.promptinput("Enter your username:")
    print("Password:")
    hpwd = pwdin()

def pwdin() -> str:
    try:
        res = hashlib.sha384(getpass.getpass("> ").encode()).hexdigest()
        return res
    except KeyboardInterrupt:
        exit(0)

if __name__ == "__main__":
    main()