import os 

def Display(Dirname, Extension1, Extension2):
    try:
        for file in os.listdir(Dirname):
            if file.endswith(Extension1):
                old_path = os.path.join(Dirname, file)
                new_file = file.replace(Extension1,Extension2)
                new_path = os.path.join(Dirname,new_file)

                os.rename(old_path,new_path)
            print(file,"renamed to",new_file)

    except FileNotFoundError:
        print("Directory does not exist")

def main():
    Dirname = input("Enter the name of Directory:")
    Extension1 = input("Enter the extension of first file:")
    Extension2 = input("Enter the extension of second file:")

    fobj = open("Marvellous.log","w")
    fobj.write("Renaming .txt file to .doc file")
    fobj.close()

    Display(Dirname, Extension1, Extension2)

if __name__ == "__main__":
    main()