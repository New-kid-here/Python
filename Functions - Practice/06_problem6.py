"""
Write a python function to remove a given word from a list ad strip it at the same 
time.
"""

l = ["Harry", "Rajesh", "Itu", "Pintu", "Jitu"]
def rem(word, l):
    l=[item.strip(word) for item in l]
    if word in l:
        l.remove(word)
    return l

c = rem("Itu", l)
print(c)