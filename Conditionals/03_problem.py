""" A spam comment is defined as a text containing following keywords: 
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
to detect these spams. """

a1 = "Make a lot of money" 
a2 = "buy now"
a3 = "subscribe this"
a4 = "click this"

user = input("Enter text you want to check: ")

if ((a1 in user) or (a2 in user) or (a3 in user) or (a4 in user)):
    print("Scam")
else:
    print("Safe")
