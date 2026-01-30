from functools import reduce

def main():
    Data = list(map(int, input("Input List:").split(","))) 
    print("Actual Data:",Data)

    FData = list(filter((lambda No: No % 2 == 0), Data))
    print("Data after Filter:",FData)

    MData = list(map((lambda No: No * No), FData))
    print("Data after Map is:",MData)

    RData = reduce((lambda a,b: a + b),MData)
    print("Data after Reduce:",RData)

if __name__ == "__main__":
    main()
