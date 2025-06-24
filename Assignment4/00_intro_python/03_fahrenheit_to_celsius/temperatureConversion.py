from typing import Union
farenheintTemp : Union[int, float] = float(input("Enter the temperature in Farenheit: "))
degrees_celsius : Union[int, float]= (farenheintTemp - 32) * 5.0/9.0
print(f"Temperature in celsius is {degrees_celsius}")