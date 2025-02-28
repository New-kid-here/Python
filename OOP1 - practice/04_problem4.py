"""
Write a class “Calculator” capable of finding square, cube and square root of a 
number. 
"""
import math


class Calculator:
    def __init__(self, n):
        self.n =n

    def Square(self):
            print(f"The square is {self.n*self.n}")

    def Cube(self): 
            print(f"The cube is {self.n*self.n*self.n}")

    def Sqrt(self):
            print(f"The square root is {math.isqrt(self.n)}")

    @staticmethod
    def greet():
          print("Bonjour Madamoseille")

Calci = Calculator(4)
Calci.greet()
Calci.Square()
Calci.Sqrt()
Calci.Cube()
