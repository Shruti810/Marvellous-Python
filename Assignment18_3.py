def Addition(lst):
    for No in lst:
      Ans = min(lst)  
    return Ans

num = int(input("number of elements: "))
number = []

for i in range(num):
    n = int(input("Enter element:"))
    number.append(n)

Result = Addition(number)
print("Output:",Result)