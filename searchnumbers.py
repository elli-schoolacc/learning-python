def main():
    zahl = int(input("Geben Sie die zu suchende Zahl ein: "))
    numbers = (0, 10, 12, 4, 7, 20, 21, 13)
    for i in numbers:
        if i == zahl:
            return("found at pos " + str(i))
    return("not found. exiting")

if __name__ == "__main__":
    print(main())