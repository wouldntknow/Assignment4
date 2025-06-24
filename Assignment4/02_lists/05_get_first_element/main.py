def get_first_element(mylist : list[str]) -> str:
    for i in range(1):
        first : str = mylist[i]

    return first


def main():
    myLists : list[str] = ["apple", "banana", "orange"]
    print(get_first_element(myLists))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

