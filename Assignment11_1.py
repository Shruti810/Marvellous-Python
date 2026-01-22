def Prime(No):
    if No<=1:
        print("Not a prime number")
    
    for i in range(2,No):
        if No % i == 0:      # for range(2,2) list is empty
            print ("Not a Prime Number")
            break

    else:
        print("Prime number")

num = int(input("Enter a number:"))

def main():
    Prime(num)

if __name__ == "__main__":
    main()