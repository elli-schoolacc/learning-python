import hashlib
import getpass

def pwdin() -> str:
    try:
        res = hashlib.sha384(getpass.getpass("> ").encode()).hexdigest()
        return res
    except KeyboardInterrupt:
        exit(0)

def attemptLogin(username, hashed_password):
    un = username
    pwd = hashed_password

    print(un)
    print(pwd)
