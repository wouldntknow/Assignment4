MAX_LENGTH: int = 5

def shorten(mylist: list[str]):
    popList: list[str] = []
    while len(mylist) > MAX_LENGTH:
        popped: str = mylist.pop()
        popList.append(popped)
        print(popList)

def main():
    mylist: list[str] = ["apple", "tomatoes", "mango", "pineapple", "banana", "grapes", "pear"]
    shorten(mylist)
    print("Shortened list:", mylist)

if __name__ == '__main__':
    main()
