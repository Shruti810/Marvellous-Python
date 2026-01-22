def Rectangle(a,b):
    Area = print("Area of rectangle is:",a * b)
    return Area

num1 = int(input("Enter Length:"))
num2 = int(input("Enter Breadth:"))

def main():
    Rectangle(num1,num2)

if __name__ == "__main__":
    main()