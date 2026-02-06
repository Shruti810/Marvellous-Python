import os
import shutil

def DirectoryCopy(Dirname1):

    Dirname2 = "Temp"   # runtime directory name

    if not os.path.exists(Dirname1):
        print("First directory does not exist")
        return

    # Create destination directory at runtime
    if not os.path.exists(Dirname2):
        os.mkdir(Dirname2)
        print("Second Directory created at runtime")

    for file in os.listdir(Dirname1):
        Dir1_path = os.path.join(Dirname1, file)
        Dir2_path = os.path.join(Dirname2, file)

        if os.path.isfile(Dir1_path):
            shutil.copy(Dir1_path, Dir2_path)

    print("All files copied successfully")


def main():
    Dirname1 = input("Enter the name of first directory:")
    
    fobj = open("Marvellous1.log","w")
    fobj.write("Copy all files from first directory to second directory")
    fobj.close()

    DirectoryCopy(Dirname1)


if __name__ == "__main__":
    main()