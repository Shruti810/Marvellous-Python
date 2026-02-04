import os

def main():
    Filename = input("Enter a filename:")

    Ret = open(Filename)

    Data = Ret.read()

    print("Data from file is:",Data)
    Ret.close()

if __name__ == "__main__":
    main()