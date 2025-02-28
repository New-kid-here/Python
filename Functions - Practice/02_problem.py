"""
Write a python program using function to convert Celsius to Fahrenheit.
"""

def temp(Celsius):
#    Celsius = float(input("Enter temperature in celsius: "))
    Fahrenheit = (9*Celsius)/5 + 32
    print(round(Fahrenheit, 2))

temp(36)
temp(45)
temp(113)