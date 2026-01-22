def Circle(No):
    Area = 3.14 * No * No
    return Area

num = int(input("Enter radius of circle:"))

def main():
    print("Area of circle is",Circle(num))

if __name__ == "__main__":
    main()