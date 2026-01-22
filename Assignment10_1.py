def MultiplicationTable(No):
    Result = []
    for i in range(1,10):
        Ans = No * i
        Result.append(Ans)
    return Result
   
def main():
    print(MultiplicationTable(4))

if __name__ == "__main__":
    main()