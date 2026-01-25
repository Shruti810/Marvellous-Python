Min = lambda a,b : a if a<b else b

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

Result = Min(num1,num2)
print("Minimum number is",Result)