def Numbers(No):
    Result = []
    for i in range(1,No+1):
        Result.append(i)
    return Result

num = int(input("Enter a number:"))

def main():
    print(Numbers(num))

if __name__ == "__main__":
    main()