import os
import sys

def main():
    FileName = sys.argv[1]

    try: 
        fobj1 = open(FileName,"r")
        fobj2 = open("Demo.txt","w") # create a Demo.txt file

        data = fobj1.read() 
        data1 = fobj2.write(data)

        fobj1.close()
        fobj2.close()

        print("Create file")

    except:
        print("Unable to open file")

if __name__ == "__main__":
    main()