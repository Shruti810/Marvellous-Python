def Binary(No):
    rev = 0
    place = 1
    while No>0:
        digit = No % 2         # divided by 2 because the binary number system is base-2
        rev = rev + digit * place
        place = place * 10    # If we reverse the digit(reminder) it is a Binary number
        No = No//2             # Removes the last processed binary digit and move to the next step 
    return rev

num = int(input("Enter a number:"))

def main():
    print("Binary Equivalent of",num,"is",Binary(num))

if __name__ == "__main__":
    main()