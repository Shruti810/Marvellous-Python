from functools import reduce

def main():
    Data = list(map(int, input("Input List: ").split(",")))  # map(int, ....) -> convert each list element into int
    print("Actual Data is :",Data)
    
    FData = list(filter((lambda No : (No >= 70 and No <= 90)), Data))   # Filter is used when the function gives boolean value means like True or False
    print("Data after Filter is :",FData)

    MData = list(map((lambda No : (No + 10)), FData))
    print("Data After Map is:", MData)

    RData = reduce((lambda a,b : a*b), MData)
    print("Data after reduce is:", RData)

if __name__ == "__main__":
    main()



    



