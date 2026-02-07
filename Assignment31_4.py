import os
import shutil

def CopyFileExtension(Dirname1,Extension):

    Dirname2 = "Temp"

    if not os.path.exists(Dirname1):
        print("First directory does not exist")
        return

    # Create destination directory at runtime
    if not os.path.exists(Dirname2):
        os.mkdir(Dirname2)
        print("Second Directory created at runtime")

    for file in os.listdir(Dirname1):
        if file.endswith(Extension):
            old_path = os.path.join(Dirname1, file) # old_path = Demo/Marvellous.exe
            new_path = os.path.join(Dirname2, file) # new_path = Temp/Marvellous.exe

            if os.path.isfile(old_path): # check is this is a path of file not folder
                shutil.copy(old_path, new_path)

    print("All files copied successfully")

def main():
    Dirname1 = input("Enter the name of Directory:")
    Extension = input("Enter the extension:")

    fobj = open("Marvellous2.log","w")
    fobj.write("Copy all files with the specified extension from first Directory to the second Directory")
    fobj.close()

    CopyFileExtension(Dirname1,Extension)

if __name__ == "__main__":
    main()