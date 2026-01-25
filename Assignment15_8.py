def main():
    Data = [3,2,15,25,60,30,90,66,75]
    print("Actual data is:",Data)

    FData = list(filter(lambda No: No % 3 == 0 and No % 5 == 0, Data))
    print("Numbers divisible by both 3 and 5 is:",FData)

if __name__ == "__main__":
    main()