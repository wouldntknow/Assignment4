def add_three_copies(mylist : list[str] , data : str) -> list :
    for i in range(3):
        mylist.append(data)
    return mylist

def main():
    data : str = input("Enter the item to be appended in the list: ")
    mylist: list[str] = []
    print(add_three_copies(mylist, data))




if __name__ == '__main__':
    main()
