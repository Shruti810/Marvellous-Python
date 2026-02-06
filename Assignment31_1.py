import os

def Display(Dirname, Extension):
    try:
        for file in os.listdir(Dirname):
            if file.endswith("." + Extension):
                print(file)

    except FileNotFoundError:
        print("Directory not found")


def main():
    Dirname = input("Enter the name of Directory:")
    Extension = input("Enter thr extension:")

    fobj = open("Marvellous.log","w")

    fobj.write("Jay Ganesh\n")
    fobj.write("This is a Log File\n")

    fobj.close()

    Display(Dirname,Extension)

if __name__ == "__main__":
    main()