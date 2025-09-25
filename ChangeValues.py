def main():
    var1 = "var 1"
    var2 = "var 2"
    print(var1 + " | " + var2)
    print("change...")
    varsh = var1
    var1 = var2
    var2 = varsh
    print(var1 + " | " + var2)

if __name__ == "__main__":
    main()