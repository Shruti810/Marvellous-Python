def Divisible(a):
    if a % 3 == 0 and a % 5 == 0:
        print(a,"Divisible by 3 and 5")
    else:
        print(a,"Not Divisible by 3 and 5")

num = int(input("Enter a number:"))

def main():
    Divisible(num)

if __name__ == "__main__":
    main()