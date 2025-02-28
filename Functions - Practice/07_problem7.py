"""
Write a python function to print first n lines of the following pattern: 
*** 
**               
*   for n = 3
"""

def aster(n):
    if (n==0):
        return
    print("*"*n)
    aster(n-1)

aster(3)
