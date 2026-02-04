import os

def main():
    FileName = input("Enter the name of File:")

    Ret = os.path.exists(FileName)

    if Ret == True:
        fobj = open(FileName,"r")
        print("File gets executed")
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()