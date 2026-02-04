def main():
    Filename1 = input("Enter the name of first file:")
    Filename2 = input("Enter the name of second file:")

    file1 = open(Filename1,"r")
    data = file1.read()
    file2 = open(Filename2,"w")
    data1 = file2.write(data)

    file1.close()
    file2.close()




if __name__ == "__main__":
    main()