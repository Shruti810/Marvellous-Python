def RevNumbers(No):
    Result = []
    for i in range(1,No+1):
        Result.append(i)
    Result.reverse()              # reverse outside for loop
    return Result

num = int(input("Enter a number:"))

def main():
    print(RevNumbers(num))

if __name__ == "__main__":
    main()