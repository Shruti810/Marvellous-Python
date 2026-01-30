from functools import reduce

def Chkprime(No):
    if No<=1:
        return False
    for i in range(2,No):
        if No % i == 0:
            return False
        
    return True

def Mult(No):
    return No * 2

def Max(a,b):
    return a if a>b else b

def main():
    Data = list(map(int,input("Input List:").split(",")))
    print("Actual Data is:",Data)

    FData = list(filter(Chkprime, Data))
    print("Data after Filter is:",FData)

    MData = list(map(Mult, FData))
    print("Data after Map is:",MData)

    RData = reduce(Max, MData)
    print("Data after Reduce is:",RData)

if __name__ == "__main__":
    main()