import os
import getpass
import hashlib



def main():
    clearlines()
    print("UUT starting up... \n Welcome!")
    uname = promptinput("Enter your username:")
    print("Password:")
    hpwd = pwdin()

def promptinput(prompt: str, cllear: bool = True) -> str:
    if cllear:
        clearlines()
    print(prompt)
    try:
        return input("> ").strip()
    except KeyboardInterrupt:
        exit(0)

def pwdin() -> str:
    try:
        res = hashlib.sha384(getpass.getpass("> ").encode()).hexdigest()
        return res
    except KeyboardInterrupt:
        exit(0)

def clearlines():
    if os.name == 'nt': os.system('cls') 
    else: os.system('clear')

if __name__ == "__main__":
    main()