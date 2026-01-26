def Number(No):
    if No > 0:
        print("Positive Number")
    elif No < 0:
        print("Negative Number")
    else:
        print("Zero")

num = int(input("Enter a number:"))
Number(num)