import math

# Simple Calculator Application

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    # BUG: Addition is written instead of multiplication!
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)

if __name__ == '__main__':
    print('Add 5 + 3:', add(5, 3))
    print('Multiply 5 * 3:', multiply(5, 3))
    print('Sqrt 9:', sqrt(9))
