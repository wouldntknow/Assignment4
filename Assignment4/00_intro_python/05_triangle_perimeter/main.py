from typing import Union

length1 : Union[int, float] = float(input("Enter the length of side 1: "))
length2 : Union[int, float] = float(input("Enter the length of side 2: "))
length3 : Union[int, float] = float(input("Enter the length of side 3: "))

perimeter : Union[int, float] = length1 + length2 + length3
print(f"The perimeter if traingle is {perimeter}")