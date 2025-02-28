"""
Create a class “Programmer” for storing information of few programmers 
working at Microsoft. 
"""
class Programmer:
    
    def __init__(self, name, language, salary, company):
        self.name = name
        self.language = language
        self.salary = salary
        self.company = company


Rajesh = Programmer("Rajesh", "Python", "12 lakhs", "Google")
Itu = Programmer("Itu", "React", "12 lakhs", "TCS")

print(f"The name of employee is {Rajesh.name}\n- The name of the company is {Rajesh.company}\n- The salary of the employee is { Rajesh.salary}\n- The language working on {Rajesh.language}")
print("")
print(f"The name of employee is {Itu.name}\n- The name of the company is {Itu.company}\n- The salary of the employee is {Itu.salary}\n- The language working on {Itu.language}")
        
