class Employee:  # ye class banaya jiske andar sab hota hai
    company = "Google"      # ye class ke attributes yaani usko define karne ke liye terms ki is class ke andar kya hai
    salary ="45k"

Rajesh = Employee()    # Ye banaya object jisse class ke attributes ko Rajesh naam ka object access karega
Rajesh.age = 20        # Ye bana intsance attribute jo sirf Rajesh object ke andar work karega
Rajesh.salary ="50k"   # Yaha humne ek class attribute ki value change ki object ke andar to wo object instance ki value lega aur baaki sab class attribute ki
print(Rajesh.company, Rajesh.salary)


