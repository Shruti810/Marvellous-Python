class Numbers:

    def __init__(self):
        self.Value = int(input("Enter number:"))

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return False
            
        return True
    
    def Factors(self):
        print("Factors are:")
        for i in range(1,self.Value + 1):
            if self.Value % i == 0:
                print(i)

obj1 = Numbers()

if obj1.ChkPrime():
    print("Number is Prime")
else:
    print("Number is Not Prime")
    
obj1.Factors()