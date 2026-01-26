def Addition(lst):
    total = 0

    for No in lst:
        total = total + No
    return total

num = int(input("number of elements: "))
number = []

for i in range(num):
    n = int(input("Enter element:"))
    number.append(n)

Result = Addition(number)
print("Output:",Result)
