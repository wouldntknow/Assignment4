import math
print("This program calculates hypotenuse of a right angled tiangle using pyhtagorea's theorem")
length1: float = float(input("Enter the length of AB: "))
length2: float = float(input("Enter the length of AC: "))

hypotenuse: float = math.sqrt(length1**2 + length2**2)
print(f"Hypotenuse length (BC) of a right angled triangle is {hypotenuse}")


