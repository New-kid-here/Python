# Write a program to find the greatest of four numbers entered by the user. 
# Using reduce and Lambda function
import functools
L = [1,55,45,9]
a= functools.reduce(lambda x,y: x if x>y else y, L)
print("This the greatest of four numbers:", a)

# Now using elif

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
num4 = int(input("Enter the fourth number:"))

if (num1>num2 and num1>num3 and num1>num4):
    print(num1, "is the greatest number")
elif (num2>num1 and num2>num3 and num2>num4):
    print(num2, "is the greatest number")
elif (num3>num1 and num3>num3 and num3>num4):
    print(num3, "is the greatest number")
else:
    print(num4, "is the greatest number")