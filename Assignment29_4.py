import sys
import os

def main():
    Filename1 = sys.argv[1]
    Filename2 = sys.argv[2]

    Ret = open(Filename1)
    Ret2 = open(Filename2)

    Data = Ret.read()
    Data2 = Ret2.read()

    if Data == Data2:
        print("Success")
    
    else:
        print("Failure")

if __name__ == "__main__":
    main()
