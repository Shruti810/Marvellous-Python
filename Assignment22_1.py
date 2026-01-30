class Demo:
    # class variable
    Value = 0

    def __init__(self,no1,no2):
        # instance variable
        self.no1 = no1
        self.no2 = no2

    # Instance method
    def Fun(self): 
        print("Value of Instance Variable 1:",self.no1)
        print("Value of Instance Variable 2",self.no2)

    # Instance method
    def Gun(self):
        print("Value of Instance Variable 1:",self.no1)
        print("Value of Instance Variable 2",self.no2)

# Creating two objects of Demo class
obj1 = Demo(11,21)
obj2 = Demo(51,101)

# Calling Instance method in given sequence
obj1.Fun()

obj2.Fun()
obj1.Gun()
obj2.Gun()
