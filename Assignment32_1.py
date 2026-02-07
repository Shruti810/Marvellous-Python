import hashlib
import os

def CalculateChecksum(Filename):
    fobj = open(Filename,"rb")    # here b after r denotes binary data 

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

        fobj.close()

        return hobj.hexdigest()   # calculate Checksum of file

def DirectoryWatcher(DirectoryName):

    if not os.path.exists(DirectoryName):
        print("There is no such Directory")
        return
    
    if not os.path.isdir(DirectoryName):
        print("It is not a Directory")
        return
    
    for FolderName, SubFolderName, Filename in os.walk(DirectoryName):
        for Fname in Filename:
            Fname = os.path.join(FolderName,Fname)
            Checksum = CalculateChecksum(Fname)

            print(f"File name: {Fname} Checksum: {Checksum}")

def main():
    DirectoryName = input("Enter the name of Directory:")
    DirectoryWatcher(DirectoryName)

    fobj = open("Marvellous.log","w")
    fobj.write("Checksum value of file")
    fobj.close()
    
if __name__ == "__main__":
    main()