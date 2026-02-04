def main():
    Filename = input("Enter the name of file:")

    try:
        file = open(Filename,"r")
        count=0

        for line in file:
            words = line.split()
            word = len(words)
            count = count + word
        print("Total number of words in",Filename,"is",count)
        file.close()

    except:
        print("File not found")

if __name__ == "__main__":
    main()