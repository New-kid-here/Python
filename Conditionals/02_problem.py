"""Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user. """

Maths = int(input("Enter marks for Maths out of 50:" ))
Sci = int(input("Enter marks for Sci out of 50:" ))
Eng = int(input("Enter marks for Eng out of 50:" ))

Total = (Maths+Sci+Eng)*100
Total_percentage = Total/150
if (Total_percentage>40 and Maths*100/50>33 and Sci*100/50>33 and Eng*100/50>33):
    print("Passed, your percentage is", Total_percentage)
else:
    print("Failed")

