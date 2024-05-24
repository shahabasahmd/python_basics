class Calculator:
    def __init__(self):
        pass

    def add(self, *args):
        return sum(args)

    def subtract(self, a, b):
        return a - b

    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b



calculator = Calculator()
print("Addition:", calculator.add(5, 3, 2))
print("Subtraction:", calculator.subtract(10, 4))
print("Multiplication:", calculator.multiply(2, 3, 4))
print("Division:", calculator.divide(10, 2))