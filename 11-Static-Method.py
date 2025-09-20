class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print("Addition:", Calculator.add(10, 5))
print("Multiplication:", Calculator.multiply(4, 3))

calc = Calculator()
print("Addition (using object):", calc.add(7, 2))
