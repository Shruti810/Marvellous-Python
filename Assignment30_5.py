def main():
    Filename = input("Enter the filename:")
    String = input("Enter the string to search:")

    try:
        file = open(Filename,"r")
        data = file.read()
        file.close()

        if String in data:
            print(String,"is found in",Filename)

        else:
            print(String,"is not found in",Filename)

    except:
        print("File not found")

if __name__ == "__main__":
    main()