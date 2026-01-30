import threading

def Even(No):
    for i in range(2,No+1,2):
        print("First 10 Even numbers:",i)

def Odd(No):
    for i in range(1,No+1,2):
        print("First 10 Odd numbers:",i)
    
    
def main():
    
    t1 = threading.Thread(target=Even,args=[20,])
    t1.start()

    t2 = threading.Thread(target=Odd,args=[20,])
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()