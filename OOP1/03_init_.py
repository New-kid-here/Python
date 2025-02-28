class Employee: 
    company = "Google"      
    salary ="45k"

    def __init__(self, name, salary, company):  # dudnder or magical methods also known as "CONSTRUCTORS" JO AUTOMATICALLY deploy hote hai
        self.name = name
        self.company = company
        self.salary = salary
        print("This line is printed without even called")
        

    def getInfo(self):
        print(f"The name is {self.name}")
        print(f"The company is {self.company} and the salary is {self.salary}")

Rajesh = Employee("Rajesh", "55k", "Tesla")
Rajesh.getInfo()




