import threading

def Small(stri):
    Count = 0
    for i in stri:
        if i.islower():
            Count = Count + 1
    print("Thread ID:",threading.get_ident())
    print("Thread Name:",threading.current_thread().name)
    print("Number of Lowercase characters:",Count)

def Capital(stri):
    Count = 0
    for i in stri:
        if i.isupper():
            Count = Count + 1
    print("Thread ID:",threading.get_ident())  # get_ident() displays Thread ID
    print("Thread Name:",threading.current_thread().name)  # current_thread displays Thread Name
    print("Number of Uppercase characters:",Count)

def Digit(stri):
    Count = 0
    for i in stri:
        if i.isdigit():
            Count = Count + 1
    print("Thread ID:",threading.get_ident())    
    print("Thread Name:",threading.current_thread().name)
    print("Number of numeric digits:",Count)

def main():
    stri = input("Enter a String:")

    t1 = threading.Thread(target=Small,args=[stri,],name="Small Thread")
    t2 = threading.Thread(target=Capital,args=[stri,],name="Capital Thread")
    t3 = threading.Thread(target=Digit,args=[stri,],name="Digits Thread")
    
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()

    #t1.join()
    #t2.join()
    #t3.join()

if __name__ == "__main__":
    main()