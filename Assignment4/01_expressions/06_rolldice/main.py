import random

totalSides : int = 6
roll1 : int = random.randint(1,totalSides)
roll2 : int = random.randint(1,totalSides)

totalrolls : int = roll1 + roll2

print(f"The first dice roll gives {roll1}")
print(f"The second dice roll gives {roll2}")
print(f"Their total is {totalrolls}")

