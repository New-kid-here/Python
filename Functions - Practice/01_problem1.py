"""
Write a program using functions to find greatest of three numbers. 
"""

def greater(a, b, c):
    if (a>b and a>c):
        print(f"The greatest number is {a}")
    elif (b>a and b>c):
        print(f"The greatest number is {b}")
    else:
        print(f"The greatest number is {c}")
    return "Done"

greater(10,9,22)
greater(55,56,87)