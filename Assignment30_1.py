def main():
    Filename = input("Enter the name of file:")
    
    try:
        file = open(Filename,"r")
        
        count = 0
        for line in file:
            count = count + 1
        print("There are",count,"line in",Filename)

        file.close()


    except:
        print("file not found")

if __name__ == "__main__":
    main()
