from src.calculator.operations.addition import addition
from src.calculator.operations.subtraction import subtraction
from src.calculator.operations.multiplication import multiplication
from src.calculator.operations.division import division
from src.calculator.operations.square import square
from src.calculator.operations.square_root import square_root

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def sub(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def mult(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divi(self, a, b):
        self.result = division(a, b)
        return self.result

    def squ(self, a):
        self.result = square(a)
        return self.result

    def root(self, a):
        self.result = square_root(a)
        return self.result