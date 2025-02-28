"""
Write a recursive function to calculate the sum of first n natural numbers.
"""

def sum(n):
    if (n==1):
        return 1
    elif (n==0):
        return 0
    return n + sum(n-1)

n = int(input("Enter number: "))
print(f"The sum is {sum(n)}")