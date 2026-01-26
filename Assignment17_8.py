def Sum(No):
    sum = 0
    while No > 0:
        digit = No % 10          # get last digit
        sum = sum + digit        # add that last digit to the sum
        No = No // 10            # remove last digit
    return sum

num = int(input("Enter a number:"))
def main():
    print("sum of digits is",Sum(num))

if __name__ == "__main__":
    main()