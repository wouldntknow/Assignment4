numbers : list[int] = [3,4,5,2,9,8]
newNumbers : list[int] = []
print("Old list ", numbers)
for number in numbers:
    newNumbers.append(number * 2)
print("New list ", newNumbers)
