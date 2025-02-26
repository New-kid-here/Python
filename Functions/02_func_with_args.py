# Function to take arguments and great them "Good day"



def gd(name, ending):
    
    print("Good day", name)
    print(ending)


gd("Itu", "Bonjour Mon Amor")
print("")

# A function also has "RETURN" value 

def gd(name, ending):
    
    print("Good day", name)
    print(ending)



a = gd("Itu", "Bonjour Mon Amor")
print(a)  # Here a would return None kyuki function kuchh value usko return karne de hi nahi rha to wapas aapko milega kya???
print("")

# Ab yaha dekho

def gd(name, ending):
    
    print("Good day", name)
    print(ending)
    return "Program completed"



a = gd("Itu", "Bonjour Mon Amor")
print(a) # Ab isme "a" kuchh value return karega jo humne likha hai 

# Its like "gd" function jo hota hai wo end mein apne andar konsi value rakhega, wo hum return waale function se batate hai