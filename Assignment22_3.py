class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first number:"))
        self.Value2 = int(input("Enter second number:"))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        return self.Value1 / self.Value2
    
obj1 = Arithmetic()

obj1.Accept()
Ans = obj1.Addition()
print("Addition is:",Ans)

Ans = obj1.Subtraction()
print("Subtraction is:",Ans)

Ans = obj1.Multiplication()
print("Multiplication is:",Ans)

Ans = obj1.Division()
print("Division is:",Ans)



