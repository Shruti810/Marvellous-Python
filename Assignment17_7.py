def display(No):
    for i in range(1,No+1):         # Rows
        for j in range(1,No+1):     # Columns
            print(j,end = " ")
        print()                   # Comes to new line

num = int(input("Enter a number:"))
display(num)