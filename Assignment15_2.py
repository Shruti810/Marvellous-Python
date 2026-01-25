# Note: Lambda Function is use in Filter map reduce

from functools import reduce

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is :",Data)
    
    FData = list(filter((lambda No : (No % 2 == 0)), Data))   # Filter is used when the function gives boolean value means like True or False
    print("Even number from above list is :",FData)

if __name__ == "__main__":
    main()