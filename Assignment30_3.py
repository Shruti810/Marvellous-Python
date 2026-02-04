def main():
    Filename = input("Enter the name of file:")

    try:
        file = open(Filename,"r")

        for line in file:
            print(line)

    except:
        print("File not found")
        







if __name__ == "__main__":
    main()