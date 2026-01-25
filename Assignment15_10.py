def main():
    Data = [2,3,4,5,6,7,8,9,10]
    print("Actual Data is:",Data)

    FData = len(list(filter(lambda No: No % 2 == 0, Data)))
    print("Count of even numbers is:",FData)

if __name__ == "__main__":
    main()