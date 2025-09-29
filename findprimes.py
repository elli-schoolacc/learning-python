import sys


def main():
    print("enter number")
    n = inputint()
    q = 1
    field = []
    while q <= n:
        field.append(q)
        q+=1
    x = 2
    while (x*2) <= n:
        
        m = 2
        while m * x <= n:
            print(f"    {x}: {m}  ", end="\r")
            field[(x * m) - 1] = 0
            m+=1
        x+=1
    print("")
    print("cleaning up..")
    i = 0
    y = field.count(0)-1
    while i <= y:
        field.remove(0)
        i+=1
    print(field)
    leng = int(len(field))
    print(f"{leng} Primes, {leng/n*100} Percent")

def inputint():
    try: 
        return int(input("> "))
    except KeyboardInterrupt:
        sys.exit()
    except:
        print("Enter number")
        inputint()
        return

if __name__ == "__main__":
    main()