def display(No):
    if No % 5 == 0:
        return True
    else:
        return False
    
num = int(input("Enter a number:"))
print(display(num))