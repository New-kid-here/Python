"""
Create a class with a class attribute a; create an object from it and set ‘a’ 
directly using ‘object.a = 0’. Does this change the class attribute? 
"""

class R:
    a = "How are you"
    
S = R()
S.a = 0

print(S.a)

# Its just that for the object you are calling, it will take its instance attribute if provided, but this doesn't change the class attribute for other objects

I = R()
print(I.a)
print(R.a)