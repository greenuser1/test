# calculator.py
# Author: ChatGPT (You can modify this as necessary)
# A simple calculator with basic and extra functionalities

import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base, exponent):
        return base ** exponent

    def sqrt(self, number):
        if number < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(number)
