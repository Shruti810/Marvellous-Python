def Even(No):
    Result = []
    for i in range(1,No+1,2):
        Result.append(i)
    return Result

num = int(input("Enter a number:"))

def main():
    print(Even(num))

if __name__ == "__main__":
    main()