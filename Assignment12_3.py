def Display(a,b):
    Ans1 = print("Addition is:",a + b)
    Ans2 = print("Subtraction is:",a - b)
    Ans3 = print("Division is:",a % b)
    Ans4 = print("Multiplication is:",a * b)
    return Ans1,Ans2,Ans3,Ans4

num1 = int(input("Enter first number:"))
num2 = int(input("Enter Second number:"))
Display(num1,num2)