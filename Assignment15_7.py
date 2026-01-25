def main():
    Data = ["Carrot","Watermelon","Apple","Kiwi","Pear"]
    print("Actual Data is:",Data)

    FData = list(filter(lambda stri: len(stri)>5, Data))
    print("Name of elements having length greater than 5:",FData)

if __name__ == "__main__":
    main()