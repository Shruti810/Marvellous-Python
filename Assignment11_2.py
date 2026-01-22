def Count(No):
    count = len(str((No)))
    return count

num = int(input("Enter a number:"))

def main():
    print("Count of digit is:", Count(num))

if __name__ == "__main__":
    main()