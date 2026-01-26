def Frequency(lst,no):
    count = 0
    for i in lst:
        if i == no:
            count = count + 1
    return count

num = int(input("Enter number of Elements:"))
lst = []

for i in range(num):
    no = int(input("Enter element:"))
    lst.append(no)

search = int(input("Enter element to search:"))

Result = Frequency(lst,search)
print("Output:",Result)


