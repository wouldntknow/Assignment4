mylist : list[str] =[]
element : str = input("Enter items: ")
while element:
    mylist.append(element)
    element = input("Enter items: ")

print("List: ",mylist)
