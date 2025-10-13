import os


def promptinput(prompt: str, cllear: bool = True) -> str:
    if cllear:
        clearlines()
    print(prompt)
    try:
        return input("> ").strip()
    except KeyboardInterrupt:
        exit(0)

def clearlines():
    if os.name == 'nt': os.system('cls') 
    else: os.system('clear')