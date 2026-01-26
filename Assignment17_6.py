def display(No):
    i = No
    while i > 0:         # Loop runs until i value becomes 0
        print(" * " * i) 
        i = i - 1                   

num = int(input("Enter a number:"))
display(num)