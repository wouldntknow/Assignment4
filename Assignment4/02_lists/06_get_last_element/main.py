def get_last_element(mylist: list[str]) -> str:
    for i in range(len(mylist)):
        last_element = mylist[i]
    return last_element

def main():
    mylist : list[str] = ["Apple", "Banana", "Orange"]
    print("Last element:", get_last_element(mylist))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

