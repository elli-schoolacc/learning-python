import os
import sys

def inEKI(prompt: str) -> str:
    print(prompt)
    try:
        input("> ")
    except KeyboardInterrupt as e:
        print("exit...")
        print(e)
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
    

def splitRGB(rgbin): return rgbin.split(",")

def sep(): print("---------------------")

def menu(target: list, available: list = []):
    #clear
    print("Color Calculator")
    sep()
    hd = "--- Target Color ---"
    print(hd)
    clstr = f"{target[0]}, {target[1]}, {target[2]}"
    print(f"> " + clstr)
    sep()
    
    
    print("--- Closest Match ---")
    
    sep()
    
    
    print("--- Available ---")
    
    sep()
    inpu = inEKI("Add Color or remove with rm(n):")
    if inpu.startswith("rm"):
        #remove shit
        return
    else:
        available.append()


def main():
    tcol = inEKI("Enter the Target Color in RGB Seperated by ',':")
    tcol = splitRGB(tcol)
    menu(tcol)


    ##
    #
    ##
    

    
if __name__ == "__main__":
    main()