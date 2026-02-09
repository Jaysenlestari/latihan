class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b  
    def multiply(self, a, b):
        return a * b
    
if __name__ == "__main__":
    calculator = Calculator()
    
    print("Subtraction: ", calculator.subtract(10, 5))  
    print("Addition: ", calculator.add(5, 3))
    print("Subtraction: ", calculator.subtract(10, 5))  
    print("Multiplication: ", calculator.multiply(10,5))
