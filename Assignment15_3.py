def main():
    Data = [22,23,24,25,26,27,28,29]
    print("Actual data is:",Data)

    FData = list(filter((lambda No:(No % 2 != 0)),Data))
    print("Odd number from the above list is:",FData)

if __name__ == "__main__":
    main()

