import threading

def Thread1(No):
    for i in range(1,No+1):
        print("Display numbers from 1 to 50:",i)

def Thread2(No):
    for i in range(No,0,-1):
        print("Display numbers from 50 to 1:",i)

def main():
    
    t1 = threading.Thread(target=Thread1,args=[50,])
    t2 = threading.Thread(target=Thread2,args=[50,])

    t1.start()
    t1.join()
    
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
