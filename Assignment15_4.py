from functools import reduce

def main():
    Data = [21,12,35,42,55,63,83]
    print("Actual Data is :",Data)
    
    RData = reduce((lambda a,b : a+b), Data)
    print("Data after reduce that is addition of all elements is:", RData)

if __name__ == "__main__":
    main()