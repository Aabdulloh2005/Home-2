import math

class Calculator:
    def __init__(self, son):
        self.son = son
    
    def plus(self, plus=1):
        self.son+=plus
    
    def minus(self, minus=1):
        self.son-=minus
    
    def multiply(self, mult=2):
        self.son*=mult
    
    def divide(self, divident = 2):
        self.son/=divident
        
    def sqrt(self):
        math.sqrt(self.son)
    
    def pow(self, pow=2):
        math.pow(self.son, pow)
    
    def mod(self, mod=2):
        self.son%=mod
        
    def get_answer(self):
         print(f"Answer is {self.son}")
    

n = int(input())

calc = Calculator(n)
calc.plus(5)             # N = 15
calc.plus()	         # N = 16
calc.mod(2)             # N = 0
calc.plus()               # N = 1	
calc.multiply(100)   # N = 100
calc.multiply()         # N = 200
calc.minus(40)        # N = 160
calc.minus()            # N = 159
calc.get_answer()  # N ning qiymati 159.
