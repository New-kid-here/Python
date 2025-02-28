class Employee: 
    company = "Google"      
    salary ="45k"

# @staticmethod   method jo argument na leta ho
    def greet():
        print("Good day")

    def getInfo(self):
        print(f"The company is {self.company} and the salary is {self.salary}")

Rajesh = Employee()  



Rajesh.greet() # Ab isme error aayega ye likhke ki greet() function to koi arguments leta hi nahi hai, tumne Rajesh ko as a argument kaise de diya
               # To us function ko define karte time hum "self" ko argument ki tarah dete hai fir saare attributes ke aage laga dete hai
               # yaha pe jab main Rajesh.getInfo() likhta hu to Rajesh = self aese jaata hai, aur har jagah self ki jagah Rajesh jaake function run hota hai

Rajesh.getInfo()
# Upar waala function can also be written as
Employee.getInfo(Rajesh) # yaha dekha Rajesh as a argument gaya


