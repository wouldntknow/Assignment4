def addNumsInList(numbers : list) -> int :
    sum : int = 0
    for number in numbers:
        sum+=number
    return sum
print("Sum of numbers is",addNumsInList([3,4,2,4,6,9]))

# alternative approach
def addNumsInList2(numbers : list) -> int :
    sum : int = sum(numbers)
    
    return sum