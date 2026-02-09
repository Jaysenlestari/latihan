class Calculator:
    def subtract(self, a, b):
        return a - b


if __name__ == "__main__":
    calculator = Calculator()
    
    print("Subtraction: ", calculator.subtract(10, 5))  