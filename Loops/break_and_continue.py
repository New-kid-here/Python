for i in range(100):
    if (i==20):
        break #It stops the loop there
    print(i)
print("The numbers are printed before", i)

# Continue 
for i in range(100):
    if (i==20):
        continue #It skips the iteration there and continues after it
    print(i)
print("The number is printed till", i)
