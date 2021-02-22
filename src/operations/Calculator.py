class Calculator:
    result = 0

    def __add__(self, a, b):
        self.result = addition(a,b)
        return self.result

    def __sub__(self, a, b):
        self.result = subtraction(a,b)
        return self.result

    def multiply(self , a ,b):
        self.result = multiplication(a,b)
        return self.result

    def div(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = square_root(a)
        return self.result

    def _init_(self):
        pass

    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def division(a, b):
        return a / b

    def square(a):
        return a ** 2

    def square_root(a):
        return a ** 0.5



