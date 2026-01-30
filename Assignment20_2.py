import threading

def EvenFactors(No):
    result = 0
    for i in range(2,No+1,2):
        if No % i == 0:
            result = result + i
    print("Sum of Even Factors is:",result)
    
def OddFactors(No):
    result = 0
    for i in range(1,No+1,2):
        if No % i == 0:
            result = result + i
    print("Sum of Odd Factors is:",result)
        
def main():
    
    t1 = threading.Thread(target=EvenFactors,args=[12,])
    t1.start()

    t2 = threading.Thread(target=OddFactors,args=[12,])
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")
    
if __name__ == "__main__":
    main()