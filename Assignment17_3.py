def Factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i
    return fact

num = int(input("Enter a number:"))

def main():
    print("Factorial of",num, "is",Factorial(num))

if __name__ == "__main__":
    main()