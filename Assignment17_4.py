def Factorsum(No):
    fact = 0
    for i in range(1,No):
        if No % i == 0:
            fact = fact + i
    return fact

num = int(input("Enter a number:"))

def main():
    print("Addition of given number factors is",Factorsum(num))

if __name__ == "__main__":
    main()