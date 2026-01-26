def display(No):
    for i in range(No):         # Rows
        for j in range(No):     # Columns
            print("*",end = " ")
        print()                   # Comes to new line

num = int(input("Enter a number:"))
display(num)