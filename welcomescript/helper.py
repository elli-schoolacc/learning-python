import os


def promptinput(prompt: str, cllear: bool = True) -> str:
    if cllear:
        clearlines()
    print(prompt)
    try:
        return input("> ").strip()
    except KeyboardInterrupt:
        exit(0)

def debug_line(input_str : str):
    dev = False
    if dev:
        print(f"[DEBUG] {input_str}")

def clearlines():
    if os.name == 'nt': os.system('cls') 
    else: os.system('clear')

def exitprogram():
    print("Exiting program...")
    exit(0)

def exiterror(code : int):
    print(f"Exiting program with error code {code}...")
    exit(code)

class UsernameError(Exception):
    pass
