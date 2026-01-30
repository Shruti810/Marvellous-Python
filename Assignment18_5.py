import MarvellousNum

def Listprime(lst):
    count = 0
    for num in lst:
        if MarvellousNum.Chkprime(num):
            count = count + num

    return count

n = int(input("Number of Elements:"))
number = []

for i in range(n):
    value = int(input("Input Elements:"))
    number.append(value)

Result = Listprime(number)
print(Result)

