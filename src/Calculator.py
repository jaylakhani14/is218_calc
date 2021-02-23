from src.operations.addition import addition
from src.operations.subtraction import subtraction
from src.operations.multiplication import multiplication
from src.operations.division import division
from src.operations.square import square
from src.operations.square_root import square_root

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