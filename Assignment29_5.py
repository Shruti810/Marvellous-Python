def main():
    Filename = input("Enter the filename:")
    String = input("Enter the string to count:")

    try:
        file = open(Filename,"r")
        data = file.read()
        file.close()

        count = data.count(String)

        print(count)

    except:
        print("File not found")

if __name__ == "__main__":
    main()