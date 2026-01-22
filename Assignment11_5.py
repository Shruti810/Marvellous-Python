def Reverse(No):
    original = No
    rev = 0
    while No > 0:
        digit = No % 10
        rev = rev * 10 + digit
        No = No // 10
    
    if original == rev:
        print("palindrome")
    else:
        print("Not palindrome")

num = int(input("Enter a number:"))
Reverse(num)