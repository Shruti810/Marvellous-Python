def Reverse(No):
    rev = 0
    while No > 0:
        digit = No % 10
        rev = rev * 10 + digit
        No = No // 10
    return rev

num = int(input("Enter a number:"))
print("Reverse is:",Reverse(num))