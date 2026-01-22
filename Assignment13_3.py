def Perfect(No):
    sum = 0
    for i in range(1,No-1):
        if No % i == 0:
            sum = sum + i
    if sum == No:
        print("Perfect number")
    else:
        print("Not a perfect number")

num = int(input("Enter a number:"))

def main():
    Perfect(num)

if __name__ == "__main__":
    main()