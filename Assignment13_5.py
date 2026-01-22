def Display(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 50:
        print("Second Class")
    else :
        print("Fail")

num = int(input("Enter a number:"))
def main():
    Display(num)

if __name__ == "__main__":
    main()