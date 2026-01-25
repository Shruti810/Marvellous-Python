def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is :",Data)

    MData = list(map((lambda No : (No * No)), Data))
    print("Square of Numbers in above list:", MData)

if __name__ == "__main__":
    main()