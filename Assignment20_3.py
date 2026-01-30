import threading

def EvenList(lst):
    result = 0
    for i in lst:
        if i % 2 == 0:
            print(i)
            result = result + i
    print("Sum of all even elements from the list:",result)

def OddList(lst):
    result = 0
    for i in lst:
        if i % 2 != 0:
            print(i)
            result = result + i
    print("Sum of all odd elements from the list:",result)

def main():
    lst = list(map(int,input("Enter Elemets:").split(",")))

    t1 = threading.Thread(target=EvenList,args=[lst,])
    t1.start()

    t2 = threading.Thread(target=OddList,args=[lst,])
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
